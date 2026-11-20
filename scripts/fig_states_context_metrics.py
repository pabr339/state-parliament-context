"""Figure: process metrics per electoral term and seat composition for Berlin, Brandenburg and
Baden-Württemberg (one framed block per state; columns = electoral terms)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch, Rectangle
from common import FIG_DIR, DERIVED, NAME, PCOL, PN, PARTY_ORDER, fy, load_context, load_bills, apply_style, draw_seats

apply_style()
el, gt, pr = load_context()
B0 = load_bills()
DATA_END = B0.start.max()
X0, X1 = 1990.0, fy(DATA_END) + 0.3
EXCLUDE_TERMS = {"BE_1989-01-29"}   # West Berlin before unification: different polity
STATES = ["BE", "BB", "BW"]
C_GOV, C_OPP = "#333333", "#B36B00"
ROWS = [("New bills (n)", "n", "{:.0f}"), ("Cycle time, median (d)", "ct_med", "{:.0f}"),
        ("Cycle time, mean (d)", "ct_mean", "{:.0f}"), ("Events, median", "ev_med", "{:g}"),
        ("Events, mean", "ev_mean", "{:.1f}")]
NR = 2 * len(ROWS)

W, H = 7.2, 10.1
fig = plt.figure(figsize=(W, H))
L, R = 1.45 / W, 1 - 0.12 / W
blk_h, gap, tab_h, seat_h = 2.95, 0.18, 1.62, 0.62        # inches
used, tabs = set(), []
for bi, st in enumerate(STATES):
    top = H - 0.1 - bi * (blk_h + gap)
    fig.add_artist(Rectangle((0.08 / W, (top - blk_h) / H), 1 - 0.13 / W, blk_h / H, transform=fig.transFigure,
                             fill=False, lw=0.8, ec="#666"))
    fig.text(0.16 / W, (top - 0.08) / H, NAME[st], fontsize=8, fontweight="bold", va="top", ha="left")
    axT = fig.add_axes([L, (top - 0.32 - tab_h) / H, R - L, tab_h / H])
    axS = fig.add_axes([L, (top - 0.32 - tab_h - 0.36 - seat_h) / H, R - L, seat_h / H], sharex=axT)
    ed = sorted(pd.to_datetime(el[el.state == st].election_date))

    # table: metrics per electoral term, government side vs opposition
    B = B0[(B0.state == st) & B0.init2.isin(["government side", "opposition"]) & ~B0.cyc_id.isin(EXCLUDE_TERMS)]
    TB = B.groupby(["cyc_id", "init2"]).agg(n=("case", "size"), ct_med=("dur_days", "median"), ct_mean=("dur_days", "mean"),
                                           ev_med=("n_events", "median"), ev_mean=("n_events", "mean")).reset_index()
    TB.insert(0, "state", st)
    tabs.append(TB)
    cyc_ids = sorted(TB.cyc_id.unique())
    starts = [pd.Timestamp(c.split("_")[1]) for c in cyc_ids]
    nxt = [next((d for d in ed if d > s), DATA_END) for s in starts]
    ax = axT
    ax.set_ylim(NR, 0)
    for sp in ["left", "bottom"]:
        ax.spines[sp].set_visible(False)
    ax.tick_params(left=False, bottom=False, labelbottom=False)
    ax.set_yticks([])
    tr = mpl.transforms.blended_transform_factory(ax.transAxes, ax.transData)
    k = 0
    for lab, col, fmt in ROWS:
        if (k // 2) % 2 == 0:
            ax.axhspan(k, k + 2, color="#f2f2f2", lw=0, zorder=0)
        for gi, (g, gc) in enumerate([("government side", C_GOV), ("opposition", C_OPP)]):
            y = k + 0.5
            ax.text(-0.01, y, f"{lab} – {'gov.' if gi == 0 else 'opp.'}", transform=tr, ha="right", va="center", fontsize=6, color=gc)
            for c, a, b in zip(cyc_ids, starts, nxt):
                v = TB[(TB.cyc_id == c) & (TB.init2 == g)][col]
                if len(v) and fy(b) > X0 + 0.5:
                    ax.text((max(fy(a), X0) + min(fy(b), X1)) / 2, y, fmt.format(v.iloc[0]), ha="center", va="center", fontsize=7, color=gc)
            k += 1
    ax.axhline(2, color="#999", lw=0.5)
    if fy(starts[0]) > X0 + 0.2:          # period before the first term with data
        ax.axvspan(X0, fy(starts[0]), color="white", zorder=1, lw=0)
    ax.set_title("Process metrics per electoral term (bills; cycle time = first to last event)", fontsize=7)

    # seat composition
    u, _ = draw_seats(axS, st, gt, pr, max(X0, fy(starts[0])), X1, DATA_END)
    used |= u
    axS.set_ylabel("Seats (%)", fontsize=6)
    axS.set_title("Government (solid) and opposition (faded) seat shares", fontsize=7)
    for a in (axT, axS):
        for d in ed:
            if max(X0, fy(starts[0]) - 0.01) <= fy(d) < X1:
                a.axvline(fy(d), color="#555", lw=.8, ls="--", zorder=4)
    axS.set_xlim(X0, X1)
    axS.set_xticks(range(1990, 2026, 5))

fig.text(0.5, 0.48 / H, "Year (dashed vertical lines = elections; columns = electoral terms)", ha="center", fontsize=7)
parties = [p for p in PARTY_ORDER if p in used]
fig.legend(handles=[Patch(color=PCOL[p], label=PN.get(p, p)) for p in parties], frameon=False, ncol=len(parties),
           fontsize=6, loc="lower center", bbox_to_anchor=(0.5, 0.06 / H), handlelength=1.4, columnspacing=1.0)
FIG_DIR.mkdir(exist_ok=True)
pd.concat(tabs).to_csv(DERIVED / "states_metrics_by_term.csv", index=False)
fig.savefig(FIG_DIR / "fig_states_context_metrics.png", dpi=300)
print("saved", FIG_DIR / "fig_states_context_metrics.png")
