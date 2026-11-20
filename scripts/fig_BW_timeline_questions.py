"""Figure: written small questions per half-year (by date of submission) in Baden-Württemberg (a) and seat
composition (b). A box lists the questions filed by the AfD (incl. its split group ABW) in each of the
five years after it entered the Landtag (computed in bw_afd_questions.py)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
from bw_afd_questions import afd_questions_per_year
from common import FIG_DIR, DERIVED, PCOL, PN, PARTY_ORDER, fy, load_context, apply_style, panel_letter, draw_seats

st = "BW"
apply_style()
el, gt, pr = load_context()
H = pd.read_csv(DERIVED / "halfyear_series.csv", parse_dates=["b0", "b1"])
H = H[(H.state == st) & (H.b0 >= "1990-01-01")].copy()          # figure starts in 1990
H["x"] = [fy(a + (b - a) / 2) for a, b in zip(H.b0, H.b1)]
full = H[~H.partial]
ed = sorted(pd.to_datetime(el[el.state == st].election_date))
X0, X1 = fy(H.b0.min()), fy(H.b1.max())

fig, AX = plt.subplots(2, 1, figsize=(7.2, 4.0), sharex=True, gridspec_kw=dict(height_ratios=[1.0, 0.75], hspace=0.38))
# a: small questions
ax = AX[0]
for d in ed:
    if X0 < fy(d) < X1:
        ax.axvline(fy(d), color="#999", lw=.7, ls="--", zorder=0)
e16 = [d for d in ed if d.year in (2016, 2021)]                  # 2016-21 term (AfD's first term) shaded
ax.axvspan(fy(e16[0]), fy(e16[1]), color="#e6e6e6", lw=0, zorder=0)
ax.plot(full.x, full.small_q, color="#7F3C8D", lw=1.4, zorder=3)
ax.set_ylim(0, 500)
ax.set_ylabel("Small questions")
ax.set_title("Written small questions per half-year (by date of submission)")
# b: seats
ax = AX[1]
used, _ = draw_seats(ax, st, gt, pr, X0, X1, H.b1.max())
for d in ed:
    if X0 < fy(d) < X1:
        ax.axvline(fy(d), color="#555", lw=.7, ls="--")
ax.set_ylabel("Seats (%)")
ax.set_title("Government (solid) and opposition (faded) seat shares")
ax.set_xlim(X0, X1)
ax.set_xlabel("Year (half-years; dashed = election)")
for a, l in zip(AX, "ab"):
    panel_letter(a, l)

# AfD entry: questions filed by AfD/ABW in each of the first five years (box, bottom right of panel a)
T = afd_questions_per_year()
T.to_csv(DERIVED / "BW_afd_questions_per_year.csv", index=False)
box = "AfD enters parliament:\n" + "\n".join(f"Year {r.year}: +{r.afd_abw_questions}" for r in T.itertuples())
AX[0].text(0.985, 0.035, box, transform=AX[0].transAxes, fontsize=6, fontweight="bold", color="#222",
           ha="right", va="bottom", multialignment="right", linespacing=1.4, zorder=6,
           bbox=dict(boxstyle="square,pad=0.75", fc="white", ec="#999", lw=0.6))

parties = [p for p in PARTY_ORDER if p in used]
fig.legend(handles=[Patch(color=PCOL[p], label=PN.get(p, p)) for p in parties], frameon=False, ncol=len(parties),
           fontsize=6, loc="upper center", bbox_to_anchor=(0.5, -0.42), bbox_transform=AX[1].transAxes)
FIG_DIR.mkdir(exist_ok=True)
fig.savefig(FIG_DIR / "fig_BW_timeline_questions.png", dpi=300, bbox_inches="tight")
print("saved", FIG_DIR / "fig_BW_timeline_questions.png")
