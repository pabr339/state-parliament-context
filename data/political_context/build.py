import sys, os, math, datetime as dt
import pandas as pd
sys.path.insert(0, os.path.dirname(__file__))
from raw_data import *

D = lambda s: None if s in (None, "", "NA") else dt.date.fromisoformat(s)
def num(s):
    if s in (None, "", "NA"): return None
    return float(s) if "." in s else int(s)
def rows(block, n):
    out = []
    for line in block.strip().splitlines():
        p = line.split(";")
        if len(p) > n: p = p[:n-1] + [";".join(p[n-1:])]
        assert len(p) == n, (len(p), line)
        out.append(p)
    return out

HARMONISE.update({"LINKE":"LINKE", "SPD+FDP":None})
def harm(lbl): return HARMONISE.get(lbl.strip(), "X_" + lbl.strip().upper().replace(" ", "_"))

STATE_NAME = {"BE":"Berlin","BB":"Brandenburg","BW":"Baden-Württemberg"}
PARL = {"BE":"Abgeordnetenhaus von Berlin","BB":"Landtag Brandenburg","BW":"Landtag von Baden-Württemberg"}

# ---------------- elections ----------------
E = []
for p in rows(ELECTIONS, 13):
    st, ed, et, wp, terr, el, vo, to, va, inv, seats, vt, src = p
    E.append(dict(state=st, election_date=D(ed), election_type=et, wahlperiode=int(wp), territory=terr,
                  electorate=num(el), voters=num(vo), turnout_pct_reported=num(to), valid_votes=num(va),
                  invalid_votes=num(inv), total_seats=num(seats), vote_type=vt,
                  source=" | ".join(SRC[s] for s in src.split("|"))))
E = pd.DataFrame(E).sort_values(["state","election_date"]).reset_index(drop=True)
E["election_id"] = E.state + "_" + E.election_date.astype(str)
E["prev_election_date"] = E.groupby("state").election_date.shift(1)
E["next_election_date"] = E.groupby("state").election_date.shift(-1)
E["cycle_start"] = E.election_date
E["cycle_end"] = E.next_election_date.apply(lambda d: d - dt.timedelta(days=1) if pd.notna(d) and d else None)
E["cycle_ongoing"] = E.next_election_date.isna()
E["turnout_pct_computed"] = (E.voters / E.electorate * 100).round(2)
E["invalid_pct"] = (E.invalid_votes / E.voters * 100).round(2)

# ---------------- party results ----------------
P = []
for p in rows(PARTIES, 7):
    st, ed, lbl, v, pct, s, src = p
    P.append(dict(state=st, election_date=D(ed), party_label=lbl, party=harm(lbl),
                  votes=num(v), vote_pct_reported=num(pct), seats=num(s), source=SRC[src]))
P = pd.DataFrame(P)
P = P.merge(E[["state","election_date","valid_votes","total_seats"]], on=["state","election_date"])
P["vote_pct"] = (P.votes / P.valid_votes * 100).round(2)
P["seat_pct"] = (P.seats / P.total_seats * 100).round(2)

# checks
chk = P.groupby(["state","election_date"]).agg(vsum=("votes","sum"), ssum=("seats","sum"), psum=("vote_pct_reported","sum")).reset_index()
chk = chk.merge(E[["state","election_date","valid_votes","total_seats"]])
chk["vote_diff"] = chk.vsum - chk.valid_votes
chk["seat_diff"] = chk.ssum - chk.total_seats
print(chk[(chk.vote_diff.abs() > 10) | (chk.seat_diff != 0) | ((chk.psum-100).abs() > 0.3)].to_string())

# harmonised aggregation
H = (P.groupby(["state","election_date","party"], as_index=False)
       .agg(votes=("votes","sum"), seats=("seats","sum"),
            party_labels=("party_label", lambda x: " + ".join(x))))
H = H.merge(E[["state","election_date","valid_votes","total_seats","prev_election_date"]], on=["state","election_date"])
H["vote_pct"] = (H.votes / H.valid_votes * 100)
H["seat_pct"] = (H.seats / H.total_seats * 100)
prev = H[["state","election_date","party","votes","vote_pct","seats"]].rename(columns={
    "election_date":"prev_election_date","votes":"prev_votes","vote_pct":"prev_vote_pct","seats":"prev_seats"})
H = H.merge(prev, on=["state","prev_election_date","party"], how="left")
first = H.prev_election_date.isna()
# Baselines for the first election in each series (shares only; seats where known)
BASE = {("BE", dt.date(1981,5,10)): (dt.date(1979,3,18), {"CDU":(44.4,63),"SPD":(42.7,61),"FDP":(8.1,11),"GRUENE":(3.7,0),"SEW":(1.1,0)}, "wahlrecht.de/ergebnisse/berlin.htm (1979)"),
        ("BW", dt.date(1980,3,16)): (dt.date(1976,4,4), {"CDU":(56.7,None),"SPD":(33.3,None),"FDP":(7.8,None)}, "back-calculated from reported change vs 1976 (Bundeswahlleiterin/Wikipedia)")}
H["prev_source"] = None
for (st, ed), (pd_, vals, srcnote) in BASE.items():
    m = (H.state == st) & (H.election_date == ed)
    H.loc[m, "prev_election_date"] = pd_
    for party, (pct, seats) in vals.items():
        mm = m & (H.party == party)
        H.loc[mm, "prev_vote_pct"] = pct
        if seats is not None: H.loc[mm, "prev_seats"] = seats
    H.loc[m, "prev_source"] = srcnote
first = pd.Series(False, index=H.index) | ((H.state == "BB") & (H.election_date == dt.date(1990,10,14)))
# party not listed previously (and not first election) -> previous = 0 only for listed-major absence? keep NA but flag
H["change_pp"] = H.vote_pct - H.prev_vote_pct
H["change_rel_pct"] = (H.vote_pct - H.prev_vote_pct) / H.prev_vote_pct * 100
H["change_votes"] = H.votes - H.prev_votes
H["change_seats"] = H.seats - H.prev_seats
H["prev_listed"] = (~H.prev_vote_pct.isna()).astype(object)
H.loc[first, "prev_listed"] = None
H["in_parliament"] = H.seats > 0
H["was_in_parliament"] = (H.prev_seats.fillna(0) > 0).astype(object)
H.loc[first, "was_in_parliament"] = None
H["entered_parliament"] = (H.in_parliament & (H.was_in_parliament == False)).astype(object)
H.loc[first, "entered_parliament"] = None
H["left_parliament_next"] = None
_bw80 = (H.state == "BW") & (H.election_date == dt.date(1980,3,16))
H.loc[_bw80, ["was_in_parliament","entered_parliament"]] = None

# ---------------- government timeline ----------------
G = []
for p in rows(GOV, 12):
    st, s, e, cab, head, hp, gp, tol, care, prec, src, note = p
    G.append(dict(state=st, start=D(s), end=D(e), cabinet=cab, head=head, head_party=harm(hp) if hp else None,
                  gov_parties=[] if gp=="NONE" else [harm(x) for x in gp.split("+")], tolerating=[harm(x.split(" (")[0]) for x in tol.split("+")] if tol else [],
                  date_precision=prec, source=src, note=note))
G = pd.DataFrame(G)

TODAY = dt.date(2026, 10, 13)
segs = []
for st in ["BE","BB","BW"]:
    es = E[E.state == st].sort_values("election_date")
    gs = G[G.state == st].sort_values("start")
    start_obs = es.election_date.min()
    # breakpoints
    bps = sorted(set([d for d in es.election_date] + [d for d in gs.start if d >= start_obs]))
    for i, b in enumerate(bps):
        nb = bps[i+1] if i+1 < len(bps) else None
        g = gs[(gs.start <= b)].iloc[-1]
        e = es[es.election_date <= b].iloc[-1]
        is_pre = len(g.gov_parties) == 0
        segs.append(dict(state=st, seg_start=b, seg_end=(nb - dt.timedelta(days=1)) if nb else None,
                         election_id=e.election_id, election_date=e.election_date, wahlperiode=e.wahlperiode,
                         cabinet=g.cabinet, head_of_government=g["head"], head_party=g.head_party,
                         gov=g.gov_parties, tol=g.tolerating, caretaker=(g.start < e.election_date) or is_pre,
                         date_precision=g.date_precision, gov_note=g.note, gov_source=g.source))
S = pd.DataFrame(segs)

seatmap = {(r.state, r.election_date, r.party): r.seats for r in H.itertuples()}
parl = H[H.seats > 0].groupby(["state","election_date"]).party.apply(list).to_dict()

def seg_fields(r):
    parties = parl[(r.state, r.election_date)]
    gov = [p for p in r.gov]
    tol = [p for p in r.tol]
    opp = [p for p in parties if p not in gov and p not in tol]
    tot = E[(E.state == r.state) & (E.election_date == r.election_date)].total_seats.iloc[0]
    gseats = sum(seatmap.get((r.state, r.election_date, p), 0) for p in gov)
    return pd.Series(dict(
        government_parties=" + ".join(gov), tolerating_parties=" + ".join(tol) or None,
        opposition_parties=" + ".join(opp), n_gov_parties=len(gov), n_parties_in_parliament=len(parties),
        gov_seats=gseats, total_seats=tot, gov_seat_pct=round(gseats / tot * 100, 2),
        minority_government=(gseats * 2 <= tot) if gov else None, single_party_government=len(gov) == 1,
        gov_parties_without_seats=" + ".join(p for p in gov if seatmap.get((r.state, r.election_date, p), 0) == 0) or None))
S = pd.concat([S, S.apply(seg_fields, axis=1)], axis=1)
S["seg_days"] = S.apply(lambda r: ((r.seg_end or TODAY) - r.seg_start).days + 1, axis=1)
S["seg_ongoing"] = S.seg_end.isna()
S.insert(0, "segment_id", S.state + "_" + S.seg_start.astype(str))

# party roles per segment (seat-holding parties)
R = []
for r in S.itertuples():
    for p in parl[(r.state, r.election_date)]:
        role = "government" if p in r.gov else ("tolerating" if p in r.tol else "opposition")
        R.append(dict(segment_id=r.segment_id, state=r.state, seg_start=r.seg_start, seg_end=r.seg_end,
                      election_id=r.election_id, wahlperiode=r.wahlperiode, party=p, role=role,
                      seats=seatmap[(r.state, r.election_date, p)], caretaker_period=r.caretaker,
                      head_party=(p == r.head_party)))
R = pd.DataFrame(R)

# role summaries per election cycle × party
def cycle_role(state, ed, party):
    seg = S[(S.state == state) & (S.election_date == ed)]
    days = seg.seg_days.sum()
    gdays = seg[seg.gov.apply(lambda g: party in g)].seg_days.sum()
    tdays = seg[seg.tol.apply(lambda g: party in g)].seg_days.sum()
    ncs = seg[~seg.caretaker]
    first = ncs.iloc[0] if len(ncs) else None
    if first is None: init = "pending (caretaker)"
    else: init = "government" if party in first.gov else ("tolerating" if party in first.tol else
                 ("opposition" if seatmap.get((state, ed, party), 0) > 0 else "extra-parliamentary"))
    return pd.Series(dict(role_initial=init, gov_share_of_cycle=round(gdays / days, 3),
                          in_gov_any_time=gdays > 0, tolerating_any_time=tdays > 0))
H = pd.concat([H, H.apply(lambda r: cycle_role(r.state, r.election_date, r.party), axis=1)], axis=1)
for _c in ["in_gov_any_time","tolerating_any_time"]: H[_c] = H[_c].astype(object)
H.loc[H.party == "OTHER", ["role_initial","gov_share_of_cycle","in_gov_any_time","tolerating_any_time"]] = None
H["party_family"] = H.party.map(PARTY_FAMILY)

# list-level results: attach harmonised change
P = P.merge(H[["state","election_date","party","change_pp","change_rel_pct","change_seats","role_initial","in_gov_any_time","gov_share_of_cycle"]],
            on=["state","election_date","party"], how="left")
P["change_pp_reported_basis"] = "computed on harmonised party (see party_results_harmonised)"

# ---------------- election-level indices ----------------
def indices(g):
    real = g[g.party != "OTHER"]
    v = real.vote_pct / 100; s = g.seat_pct / 100
    enep = 1 / (v ** 2).sum()
    enpp = 1 / ((s[s > 0]) ** 2).sum()
    gallagher = math.sqrt(0.5 * ((g.vote_pct - g.seat_pct) ** 2).sum())
    ch = g.change_pp.dropna()
    # Pedersen: half sum of abs change over parties present in either election (harmonised, incl OTHER)
    top = g.sort_values("vote_pct", ascending=False)
    return pd.Series(dict(enep_votes=round(enep, 2), enpp_seats=round(enpp, 2), gallagher_lsq=round(gallagher, 2),
                          largest_party=top.party.iloc[0], largest_party_pct=round(top.vote_pct.iloc[0], 2),
                          margin_first_second_pp=round(top.vote_pct.iloc[0] - top.vote_pct.iloc[1], 2),
                          n_parties_in_parliament=int((g.seats > 0).sum()),
                          parties_in_parliament=" + ".join(g[g.seats > 0].sort_values("seats", ascending=False).party),
                          seat_distribution=", ".join(f"{p} {int(x)}" for p, x in g[g.seats > 0].sort_values("seats", ascending=False)[["party","seats"]].values),
                          vote_share_other_unlisted=round(g[g.party == "OTHER"].vote_pct.sum(), 2)))
I = H.groupby(["state","election_date"]).apply(indices).reset_index()

def pedersen(state, ed, ped):
    if ped is None or pd.isna(ped): return None
    a = H[(H.state == state) & (H.election_date == ed)].set_index("party").vote_pct
    b = H[(H.state == state) & (H.election_date == ped)].set_index("party").vote_pct
    allp = set(a.index) | set(b.index)
    return round(0.5 * sum(abs(a.get(p, 0) - b.get(p, 0)) for p in allp), 2)
E = E.merge(I, on=["state","election_date"])
E["pedersen_volatility"] = E.apply(lambda r: pedersen(r.state, r.election_date, r.prev_election_date), axis=1)
E["turnout_change_pp"] = E.groupby("state").turnout_pct_reported.diff().round(2)

# first government after election
def first_gov(r):
    seg = S[(S.state == r.state) & (S.election_date == r.election_date) & (~S.caretaker)]
    if not len(seg): return pd.Series(dict(gov_formed_date=None, gov_formation_days=None, first_cabinet=None,
                                           first_head=None, first_gov_parties=None, first_gov_seat_pct=None,
                                           first_opposition_parties=None, n_gov_changes_in_cycle=0))
    f = seg.iloc[0]
    return pd.Series(dict(gov_formed_date=f.seg_start, gov_formation_days=(f.seg_start - r.election_date).days,
                          first_cabinet=f.cabinet, first_head=f.head_of_government, first_gov_parties=f.government_parties,
                          first_gov_seat_pct=f.gov_seat_pct, first_opposition_parties=f.opposition_parties,
                          n_gov_changes_in_cycle=len(seg) - 1))
E = pd.concat([E, E.apply(first_gov, axis=1)], axis=1)
E["state_name"] = E.state.map(STATE_NAME); E["parliament"] = E.state.map(PARL)
E["in_range_1984_2024"] = E.apply(lambda r: (r.cycle_end is None or r.cycle_end >= dt.date(1984,1,1)) and r.election_date <= dt.date(2024,12,31), axis=1)

# terms
T = pd.DataFrame([dict(state=p[0], wahlperiode=int(p[1]), constituent_session=D(p[2]), term_end=D(p[3]), note=p[4] or None, source=p[5] or None)
                  for p in rows(TERMS, 6)])
E = E.merge(T[["state","wahlperiode","constituent_session"]].rename(columns={"constituent_session":"wp_constituent_session"}), on=["state","wahlperiode"], how="left")

C = pd.DataFrame([dict(state=p[0], cabinet=p[1], head=p[2], head_party=p[3], coalition=p[4], start=p[5], end=p[6], note=p[7] or None, source=p[8])
                  for p in rows(CABINETS, 9)])

# save
OUT = os.path.dirname(os.path.abspath(__file__))  # CSVs are written next to this script
E_cols = ["election_id","state","state_name","parliament","election_date","election_type","territory","wahlperiode","wp_constituent_session",
          "prev_election_date","next_election_date","cycle_start","cycle_end","cycle_ongoing","in_range_1984_2024",
          "vote_type","electorate","voters","turnout_pct_reported","turnout_pct_computed","turnout_change_pp","valid_votes","invalid_votes","invalid_pct",
          "total_seats","n_parties_in_parliament","parties_in_parliament","seat_distribution","largest_party","largest_party_pct","margin_first_second_pp",
          "enep_votes","enpp_seats","gallagher_lsq","pedersen_volatility","vote_share_other_unlisted",
          "gov_formed_date","gov_formation_days","first_cabinet","first_head","first_gov_parties","first_gov_seat_pct","first_opposition_parties","n_gov_changes_in_cycle","source"]
E = E[E_cols]
H["election_id"] = H.state + "_" + H.election_date.astype(str)
for c in ["vote_pct","seat_pct","prev_vote_pct","change_pp","change_rel_pct"]: H[c] = H[c].round(2)
H_cols = ["election_id","state","election_date","prev_election_date","party","party_labels","party_family","votes","vote_pct","seats","seat_pct",
          "prev_votes","prev_vote_pct","prev_seats","prev_source","change_pp","change_rel_pct","change_votes","change_seats","prev_listed",
          "in_parliament","was_in_parliament","entered_parliament","role_initial","in_gov_any_time","gov_share_of_cycle","tolerating_any_time"]
H = H[H_cols].sort_values(["state","election_date","votes"], ascending=[True,True,False])
P["election_id"] = P.state + "_" + P.election_date.astype(str)
for c in ["change_pp","change_rel_pct"]: P[c] = P[c].round(2)
P = P[["election_id","state","election_date","party_label","party","votes","vote_pct","vote_pct_reported","seats","seat_pct",
       "change_pp","change_rel_pct","change_seats","role_initial","in_gov_any_time","gov_share_of_cycle","source"]].sort_values(["state","election_date","votes"], ascending=[True,True,False])
S = S.drop(columns=["gov","tol"])
S_cols = ["segment_id","state","seg_start","seg_end","seg_ongoing","seg_days","election_id","election_date","wahlperiode","cabinet","head_of_government","head_party",
          "government_parties","tolerating_parties","opposition_parties","n_gov_parties","single_party_government","minority_government","gov_seats","total_seats","gov_seat_pct",
          "gov_parties_without_seats","n_parties_in_parliament","caretaker","date_precision","gov_note","gov_source"]
S = S[S_cols]
for name, df in dict(elections=E, party_results_lists=P, party_results_harmonised=H, government_timeline=S,
                     party_roles_timeline=R, cabinets=C, legislative_terms=T).items():
    os.makedirs(f"{OUT}/combined", exist_ok=True)
    df.to_csv(f"{OUT}/combined/{name}.csv", index=False)
    for st in ["BE", "BB", "BW"]:
        os.makedirs(f"{OUT}/{st}", exist_ok=True)
        df[df.state == st].to_csv(f"{OUT}/{st}/{st}_{name}.csv", index=False)
