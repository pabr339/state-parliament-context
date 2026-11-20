"""Written small questions filed by the AfD after it entered the Landtag of Baden-Württemberg.

Counts the questions whose first author belongs to the AfD or to its split group ABW (2016) in each of
the first five years after the constituent session of the 16th Landtag (11 May 2016). Year k runs from
the k-th anniversary of that session (inclusive) to the next one (exclusive), so the five years cover the
whole 2016-21 term. The question date is the date of submission (see README).

Input : derived/small_questions.csv   (written by 01_prepare_data.py)
        data/political_context/combined/legislative_terms.csv
Output: derived/BW_afd_questions_per_year.csv
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pandas as pd
from common import DERIVED, PC_DIR

AFD_LABELS = ["AfD", "ABW"]      # party labels in the BW author field (ABW = AfD split group, 2016)


def afd_entry_date():
    """Constituent session of the 16th Landtag of Baden-Württemberg (first term with the AfD)."""
    t = pd.read_csv(PC_DIR / "legislative_terms.csv")
    return pd.Timestamp(t[(t.state == "BW") & (t.wahlperiode == 16)].constituent_session.iloc[0])


def afd_questions_per_year(n_years=5):
    sq = pd.read_csv(DERIVED / "small_questions.csv", parse_dates=["q_date"])
    sq = sq[sq.state == "BW"].assign(d=lambda x: x.q_date.dt.tz_convert(None))
    entry = afd_entry_date()
    rows = []
    for k in range(n_years):
        a, b = entry + pd.DateOffset(years=k), entry + pd.DateOffset(years=k + 1)
        q = sq[(sq.d >= a) & (sq.d < b)]
        n_afd = int(q.party.isin(AFD_LABELS).sum())
        rows.append({"year": k + 1, "period_start": a.date(), "period_end": (b - pd.Timedelta(days=1)).date(),
                     "afd_abw_questions": n_afd, "all_questions": len(q),
                     "afd_abw_share_pct": round(100 * n_afd / len(q), 1)})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    T = afd_questions_per_year()
    DERIVED.mkdir(exist_ok=True)
    T.to_csv(DERIVED / "BW_afd_questions_per_year.csv", index=False)
    print(T.to_string(index=False))
    print(f"total AfD/ABW questions: {T.afd_abw_questions.sum()}")
