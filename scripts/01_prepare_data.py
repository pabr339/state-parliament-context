"""Derive the analysis tables from the preprocessed event logs of Hillmann et al. (2025).

Input : data/eventlogs/<state>-all-preprocessed.xes(.zip)   (see README for download)
        data/political_context/combined/*.csv
Output: derived/bills.csv            one row per bill (case containing a 'Gesetzentwurf')
        derived/halfyear_series.csv  bills and written small questions per half-year
"""
import ast, re, sys, tempfile, zipfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
import pandas as pd
import pm4py
from common import LOG_DIR, DERIVED, STATES, load_context

DATA_END = pd.Timestamp("2024-08-31")          # last day covered by the event logs
COLS = ["case:concept:name", "concept:name", "time:timestamp", "@@index", "Wp", "Urheber",
        "DokArtL", "case:VTyp", "case:VTypL"]


# ---------------------------------------------------------------- reading
def read_log(st):
    stem = f"{STATES[st]}-all-preprocessed.xes"
    for p in (LOG_DIR / stem, LOG_DIR / (stem + ".zip")):
        if p.exists():
            break
    else:
        raise FileNotFoundError(f"{stem}(.zip) not found in {LOG_DIR} - see README")
    if p.suffix == ".zip":
        with tempfile.TemporaryDirectory() as tmp, zipfile.ZipFile(p) as z:
            name = [n for n in z.namelist() if n.endswith(".xes") and not n.startswith("__MACOSX")][0]
            z.extract(name, tmp)
            df = pm4py.read_xes(f"{tmp}/{name}")
    else:
        df = pm4py.read_xes(str(p))
    df = df[[c for c in COLS if c in df.columns]].copy()
    df["time:timestamp"] = pd.to_datetime(df["time:timestamp"], utc=True)
    return df


def toks(a):
    """Some activity labels are lists (several document types in one event)."""
    if isinstance(a, str) and a.startswith("["):
        try:
            return list(ast.literal_eval(a))
        except Exception:
            return [a]
    return [a]


# ---------------------------------------------------------------- bills
DRAFT = {"BW": lambda t: t == "Gesetzentwurf", "BE": lambda t: "(Gesetzentwurf" in t, "BB": lambda t: t == "Gesetzentwurf"}
PROMUL = {"BW": lambda t: t in ("Gesetz", "Gesetzblatt für Baden-Württemberg"),
          "BE": lambda t: t == "Gesetz- und Verordnungsblatt", "BB": lambda t: t == "Gesetz"}
FINAL = {"BW": {"Zweite Beratung", "Dritte Beratung", "Beschluss des Landtags in Zweiter Beratung",
                "Beschluss des Landtags in Dritter Beratung", "Gesetzesbeschluss des Landtags"},
         "BE": {"II. Lesung", "III. Lesung", "I. und II. Lesung", "II. Lesung (Basisdokument)"},
         "BB": {"Lesung", "Lesung / Fortsetzung", "Beschluss"}}


def committee_and_readings(st, g):
    """Number of committee documents and plenary-reading events of one case."""
    cn, da = g["concept:name"].astype(str), g["DokArtL"].astype(str)
    if st == "BB":
        comm = (da == "Ausschussprotokoll") | cn.str.contains("Beschlussempfehlung", regex=False)
        read = cn.str.contains("Lesung", regex=False)
    elif st == "BE":
        comm = (da == "Ausschussprotokoll") | cn.str.contains("Beschlussempfehlung|Ausschussbericht")
        read = cn.str.contains("Lesung", regex=False)
    else:
        comm = (da == "Ausschussprotokoll") | cn.str.contains("Beschlussempfehlung", regex=False)
        read = (da == "Plenarprotokoll") & cn.str.contains("Beratung", regex=False)
    return int(comm.sum()), int(read.sum())


def bill_table(st, df):
    recs = []
    for cid, g in df[df["case:VTyp"] == "Gesetz"].groupby("case:concept:name", sort=False):
        g = g.sort_values(["time:timestamp", "@@index"])
        T = [toks(a) for a in g["concept:name"]]
        flat = [t for tt in T for t in tt]
        if not any(DRAFT[st](x) for x in flat):
            continue
        ts = list(g["time:timestamp"])
        dmask = [any(DRAFT[st](x) for x in tt) for tt in T]
        if st == "BE":
            gov = g.loc[dmask, "concept:name"].str.contains("Vorlage zur Beschlussfassung", regex=False).any()
        else:
            gov = "Landesregierung" in " ".join(g.loc[dmask, "Urheber"].dropna().astype(str))
        tp = next((t for tt, t in zip(T, ts) if any(PROMUL[st](x) for x in tt)), pd.NaT)
        fin = [t for tt, t in zip(T, ts) if any(x in FINAL[st] for x in tt)]
        isd = g["concept:name"].astype(str).str.contains("Gesetzentwurf", regex=False)
        u = g.loc[isd, "Urheber"].dropna()
        urh = u.iloc[0] if len(u) else None              # first named author of the draft
        n_comm, n_read = committee_and_readings(st, g)
        recs.append(dict(state=st, case=str(cid), start_ts=ts[0], end_ts=ts[-1], wp=int(g["Wp"].iloc[0]),
                         n_events=len(g), promulgated=pd.notna(tp), promul_ts=tp, dur_days=(ts[-1] - ts[0]).days,
                         gov_initiated=bool(gov), urheber=None if pd.isna(urh) else str(urh),
                         last_final=max(fin).tz_localize(None) if fin else pd.NaT,
                         n_comm_doc=n_comm, n_read_doc=n_read))
    return pd.DataFrame(recs)


# ---------------------------------------------------------------- initiator and electoral term
PAT = [("CDU", r"CDU|Christlich"), ("SPD", r"SPD|Sozialdemokrat"), ("GRUENE", r"GR[ÜU]N|Bündnis 90|B90|Alternative Liste|\bAL\b"),
       ("FDP", r"FDP|Freie Demokrat"), ("LINKE", r"PDS|LINKE|Linke|Sozialismus"), ("AFD", r"AfD|Alternative für Deutschland"),
       ("REP", r"Republikaner|\bREP\b"), ("DVU", r"DVU|Deutsche Volksunion"), ("FW", r"Freie Wähler|BVB|FREIE WÄHLER"),
       ("PIRATEN", r"Piraten"), ("BSW", r"BSW|Wagenknecht")]
PAT = [(p, re.compile(rx, re.I if p == "GRUENE" else 0)) for p, rx in PAT]


def parties_in(u):
    u = "" if u is None or isinstance(u, float) else str(u)
    return sorted({p for p, rx in PAT if rx.search(u)})


def add_context(B, el, gt, pr):
    gt = gt.copy()
    gt["a"] = pd.to_datetime(gt.seg_start)
    gt["b"] = pd.to_datetime(gt.seg_end).fillna(pd.Timestamp("2099-01-01"))
    el = el.copy()
    for c in ["cycle_start", "cycle_end"]:
        el[c] = pd.to_datetime(el[c])
    role = {sid: dict(zip(g.party, g.role)) for sid, g in pr.groupby("segment_id")}

    def initiator(st, d, gov, parties):
        if gov:
            return "government"
        sg = gt[(gt.state == st) & (gt.a <= d) & (gt.b >= d)]
        if not len(sg) or not parties:
            return "unclear"
        rl = role[sg.iloc[0].segment_id]
        r = {("gov" if rl.get(p) in ("government", "tolerating") else "opp" if rl.get(p) == "opposition" else "none") for p in parties}
        if r == {"gov"}:
            return "coalition groups"
        if r == {"opp"}:
            return "opposition"
        if {"gov", "opp"} <= r:
            return "cross-camp"
        return "unclear"

    def cycle(st, d):
        c = el[(el.state == st) & (el.cycle_start <= d) & (el.cycle_end.fillna(pd.Timestamp("2099-01-01")) >= d)].iloc[0]
        return c.election_id, (c.cycle_end + pd.Timedelta(days=1)) if pd.notna(c.cycle_end) else pd.NaT

    B["parties"] = B.urheber.map(lambda u: ",".join(parties_in(u)))
    B["initiator"] = [initiator(s, d, g, p.split(",") if p else []) for s, d, g, p in zip(B.state, B.start, B.gov_initiated, B.parties)]
    B["init2"] = B.initiator.replace({"coalition groups": "government side", "government": "government side", "unclear": "other"})
    cyc = [cycle(s, d) for s, d in zip(B.state, B.start)]
    B["cyc_id"] = [c[0] for c in cyc]
    B["next_el"] = [c[1] for c in cyc]
    return B


def add_outcome(B):
    """promulgated | final_vote (case ends <=60 days after a final plenary event) | lapsed | censored (term still open)."""
    concl = B.last_final.notna() & ((B.end - B.last_final).dt.days <= 60)
    B["outcome"] = np.select([B.promulgated, concl], ["promulgated", "final_vote"], "lapsed")
    B["outcome_date"] = pd.to_datetime(np.select([B.promulgated, concl], [B.promul_date, B.last_final], B.next_el))
    cur = B.next_el > DATA_END
    B.loc[cur & (B.outcome == "lapsed"), "outcome"] = "censored"
    B.loc[B.outcome == "censored", "outcome_date"] = DATA_END
    B["T_days"] = (B.outcome_date - B.start).dt.days.clip(lower=0)
    return B


# ---------------------------------------------------------------- written small questions
SQ_TYPES = {"BW": ["Kleine Anfrage und Antwort"], "BE": ["Kleine Anfrage", "Schriftliche Anfrage"], "BB": ["Kleine Anfrage"]}


def small_questions(st, df):
    a = df[df["case:VTypL"] == "Anfrage"].sort_values(["case:concept:name", "time:timestamp"])
    first = a.groupby("case:concept:name")["concept:name"].first()
    a = a[a["case:concept:name"].isin(first[first.isin(SQ_TYPES[st])].index)]
    qd = a.groupby("case:concept:name")["time:timestamp"].min()
    if st == "BW":       # question and answer form one document in BW
        ad = qd
    else:
        ad = a[a["concept:name"].astype(str).str.startswith("Antwort")].groupby("case:concept:name")["time:timestamp"].min()
    return pd.DataFrame({"q_date": qd, "a_date": ad}).assign(state=st).reset_index()


def halfyear_series(st, Bst, Q):
    end = pd.Timestamp(DATA_END, tz="UTC")
    start = min(Bst.start_ts.min(), Q.q_date.min())
    edges = [pd.Timestamp(f"{y}-{m:02d}-01", tz="UTC") for y in range(start.year, DATA_END.year + 1) for m in (1, 7)]
    edges.append(pd.Timestamp(f"{DATA_END.year + 1}-01-01", tz="UTC"))
    E = pd.DataFrame({"b0": edges[:-1], "b1": [e - pd.Timedelta(seconds=1) for e in edges[1:]]})
    E = E[(E.b1 >= start) & (E.b0 <= end)].reset_index(drop=True)
    Qa = Q[Q.a_date.notna()]
    E["label"] = [f"{d.year} H{1 if d.month == 1 else 2}" for d in E.b0]
    E["open"] = [int(((Bst.start_ts <= b1) & (Bst.end_ts >= b0)).sum()) for b0, b1 in zip(E.b0, E.b1)]
    E["new"] = [int(((Bst.start_ts >= b0) & (Bst.start_ts <= b1)).sum()) for b0, b1 in zip(E.b0, E.b1)]
    E["promulgated"] = [int(((Bst.promul_ts >= b0) & (Bst.promul_ts <= b1)).sum()) for b0, b1 in zip(E.b0, E.b1)]
    E["small_q"] = [int(((Qa.a_date >= b0) & (Qa.a_date <= b1)).sum()) for b0, b1 in zip(E.b0, E.b1)]
    E["partial"] = (E.b1 > end) | (E.b0 < start)
    E["state"] = st
    E["b0"], E["b1"] = E.b0.dt.date, E.b1.dt.date
    return E


if __name__ == "__main__":
    el, gt, pr = load_context()
    bills, series = [], []
    for st in STATES:
        print(f"reading {st} ...", flush=True)
        df = read_log(st)
        Bst = bill_table(st, df)
        series.append(halfyear_series(st, Bst, small_questions(st, df)))
        bills.append(Bst)
    B = pd.concat(bills, ignore_index=True)
    for a, b in [("start_ts", "start"), ("end_ts", "end"), ("promul_ts", "promul_date")]:
        B[b] = pd.to_datetime(B[a].dt.date)          # calendar day (UTC) of the event
    B = add_outcome(add_context(B, el, gt, pr))
    DERIVED.mkdir(exist_ok=True)
    cols = ["state", "case", "wp", "start", "end", "n_events", "dur_days", "promulgated", "promul_date", "gov_initiated",
            "urheber", "parties", "initiator", "init2", "cyc_id", "n_comm_doc", "n_read_doc", "last_final",
            "outcome", "outcome_date", "T_days"]
    B[cols].to_csv(DERIVED / "bills.csv", index=False)
    pd.concat(series).to_csv(DERIVED / "halfyear_series.csv", index=False)
    print(f"wrote {len(B)} bills and {sum(len(s) for s in series)} half-year rows to {DERIVED}")
