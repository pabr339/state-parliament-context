"""Figure: Brandenburg - share of opposition bills rejected at first reading and median days from
draft to decision, per half of each electoral term (a), with seat composition (b).

Rejected at first reading = opposition bill, not promulgated, exactly one plenary reading event
(activity label contains 'Lesung') and no committee document (Ausschussprotokoll or Beschlussempfehlung).
Draft -> decision = days from introduction to promulgation or final plenary vote (decided bills only)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D
from matplotlib.patches import Patch, Rectangle
from scipy.interpolate import PchipInterpolator
from common import FIG_DIR, DERIVED, PCOL, PN, PARTY_ORDER, fy, load_context, load_bills, apply_style, panel_letter, draw_seats

st = "BB"
C_REJ, C_DAYS = "#1a1a1a", "#E69F00"
apply_style()
el, gt, pr = load_context()
B = load_bills()
B = B[B.state == st].copy()
B["srr"] = (~B.promulgated) & (B.n_comm_doc == 0) & (B.n_read_doc == 1)
B["decided"] = B.outcome.isin(["promulgated", "final_vote"])
B["party1"] = B.parties.fillna("").str.split(",").str[0]
B["t"] = B.start.map(fy)
op = B[B.init2 == "opposition"]
ed = sorted(pd.to_datetime(el[el.state == st].election_date))
dmax = B.start.max()
X0, X1 = fy(pd.Timestamp("1990-10-14")) - 0.3, fy(dmax) + 0.5

# values for the first and second half of every electoral term
terms = sorted(op.cyc_id.unique())
rows = []
for c in terms:
    a0 = fy(pd.Timestamp(c.split("_")[1]))
    a1 = next((fy(d) for d in ed if fy(d) > a0 + 0.1), fy(dmax))
    mid = (a0 + a1) / 2
    for h, (lo, hi) in enumerate([(a0, mid), (mid, a1)], 1):
        o = op[(op.cyc_id == c) & (op.t >= lo) & (op.t < hi)]
        d = o[o.decided]
        rows.append(dict(term=c, half=h, x0=lo, x1=hi, x=(lo + hi) / 2, n=len(o), first_reading_rejection_pct=100 * o.srr.mean(),
                         n_decided=len(d), median_draft_to_decision_days=d.T_days.median()))
R = pd.DataFrame(rows)
R.to_csv(DERIVED / "BB_rejection_days_half.csv", index=False)


def draw(ax, col, color, log=False):
    """Points + monotone piecewise-cubic (PCHIP) interpolation through them (no overshoot)."""
    Q = R.dropna(subset=[col])
    y = np.log(Q[col].values) if log else Q[col].values
    xs = np.linspace(Q.x.min(), Q.x.max(), 400)
    ys = PchipInterpolator(Q.x.values, y)(xs)
    ax.plot(xs, np.exp(ys) if log else ys, color=color, lw=1.5, zorder=3)
    ax.plot(Q.x, Q[col], ls="none", marker="o", ms=3.2, color=color, zorder=4)


fig, AX = plt.subplots(2, 1, figsize=(7.2, 4.4), sharex=True, gridspec_kw=dict(height_ratios=[1.3, 0.75], hspace=0.55))
ax = AX[0]
for d in ed:
    if X0 < fy(d) < X1:
        for a in AX:
            a.axvline(fy(d), color="#999", lw=.7, ls="--", zorder=0)
draw(ax, "first_reading_rejection_pct", C_REJ)
ax.set_ylim(0, 105)
ax.set_yticks([0, 20, 40, 60, 80, 100])
ax.set_ylabel("Opposition bills rejected at\nfirst reading without committee (%)")
axr = ax.twinx()
draw(axr, "median_draft_to_decision_days", C_DAYS, log=True)
axr.set_yscale("log")
axr.set_ylim(8, 600)
axr.set_yticks([10, 20, 50, 100, 200])
axr.yaxis.set_major_formatter(mpl.ticker.FuncFormatter(lambda v, _: f"{v:g}"))
axr.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
axr.spines["right"].set_visible(True)
axr.spines["right"].set_color("#B36B00")
axr.set_ylabel("Opposition bills: draft → decision,\nmedian days (log scale)", color="#B36B00")
axr.tick_params(axis="y", colors="#B36B00")
ax.axvspan(fy(ed[2]), fy(ed[3]), color="#e6e6e6", lw=0, zorder=0)          # 1999-2004 term
ax.set_title("From 1999, swift change in handling opposition bills")
t3 = op[op.cyc_id == "BB_1999-09-05"].groupby("party1").agg(n=("case", "size"), k=("srr", "sum"))
lab = "Rejected at first\nreading, 1999–2004:\n" + "\n".join(
    f"{PN.get(p, p)}: {100 * t3.loc[p, 'k'] / t3.loc[p, 'n']:.0f}% ({int(t3.loc[p, 'k'])}/{int(t3.loc[p, 'n'])})" for p in ["LINKE", "DVU"])
ax.text(fy(ed[2]) + 1.0, 42, lab, ha="left", va="center", fontsize=6, color="#333", zorder=6,
        bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="#bbb", lw=0.6))

# b: seats, 1999-2004 in focus (all parties solid, government framed), other terms shaded
ax = AX[1]
fa, fb = fy(ed[2]), fy(ed[3])
in_focus = lambda a, b: a >= fa - 0.01 and b <= fb + 0.01
used, segs = draw_seats(ax, st, gt, pr, X0, X1, dmax,
                        alpha_fn=lambda role, a, b, alpha: 1.0 if (role == "government" or in_focus(a, b)) else 0.3)
foc = [s for s in segs if in_focus(s[0], s[1])]
ax.add_patch(Rectangle((min(s[0] for s in foc) + 0.05, 0.6), max(s[1] for s in foc) - min(s[0] for s in foc) - 0.1,
                       max(s[2] for s in foc) - 1.2, fill=False, ec="#E69F00", lw=1.6, zorder=6))
for d in ed:
    if X0 < fy(d) < X1:
        ax.axvline(fy(d), color="#333", lw=.8, ls="--", zorder=5)
for a0, a1 in [(X0, fa), (fb, X1)]:
    ax.axvspan(a0, a1, color="white", alpha=0.55, lw=0, zorder=4)
ax.set_ylabel("Seats (%)")
ax.set_title("Seat shares (government solid, opposition faded); 1999–2004 in focus, government framed in orange")
ax.set_xlim(X0, X1)
ax.set_xlabel("Year (bills by introduction date; dashed = election)")
for a, l in zip(AX, "ab"):
    panel_letter(a, l)
fig.legend(handles=[Line2D([], [], color=C_REJ, lw=1.6, label="rejected at first reading (%, left axis)"),
                    Line2D([], [], color=C_DAYS, lw=1.6, label="draft → decision (median days, right axis)")],
           frameon=False, ncol=2, fontsize=6, loc="upper center", bbox_to_anchor=(0.5, -0.04), bbox_transform=AX[0].transAxes)
parties = [p for p in PARTY_ORDER if p in used]
fig.legend(handles=[Patch(color=PCOL[p], label=PN.get(p, p)) for p in parties], frameon=False, ncol=len(parties),
           fontsize=6, loc="upper center", bbox_to_anchor=(0.5, -0.42), bbox_transform=AX[1].transAxes)
FIG_DIR.mkdir(exist_ok=True)
fig.savefig(FIG_DIR / "fig_BB_oppositionbills.png", dpi=300, bbox_inches="tight")
print("saved", FIG_DIR / "fig_BB_oppositionbills.png")
