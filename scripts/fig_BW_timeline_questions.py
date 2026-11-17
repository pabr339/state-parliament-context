"""Figure: written small questions answered per half-year in Baden-Württemberg (a) and seat
composition (b). Newspaper headlines are added only if the screenshots exist in data/images/."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch
from common import FIG_DIR, DERIVED, IMG_DIR, PCOL, PN, PARTY_ORDER, fy, load_context, apply_style, panel_letter, draw_seats

st = "BW"
apply_style()
el, gt, pr = load_context()
H = pd.read_csv(DERIVED / "halfyear_series.csv", parse_dates=["b0", "b1"])
H = H[H.state == st].copy()
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
ax.axvspan(fy(pd.Timestamp("2016-03-13")), fy(pd.Timestamp("2021-03-14")), color="#e6e6e6", lw=0, zorder=0)
ax.plot(full.x, full.small_q, color="#7F3C8D", lw=1.4, zorder=3)
ax.set_ylim(0, 500)
ax.set_ylabel("Questions answered")
ax.set_title("Written small questions answered per half-year")
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

# optional newspaper headlines (see README: not distributed for copyright reasons)
axq = AX[0]
pos = axq.get_position()
W_in, H_in = fig.get_size_inches()
xr, yr = axq.get_xlim(), axq.get_ylim()


def add_img(path, x0, y0, w):
    img = mpimg.imread(path)
    w_in = w / (xr[1] - xr[0]) * pos.width * W_in
    h = w_in * img.shape[0] / img.shape[1] / (pos.height * H_in) * (yr[1] - yr[0])
    if y0 is None:
        y0 = yr[1] - 12 - h
    iax = axq.inset_axes([x0, y0, w, h], transform=axq.transData, zorder=6)
    iax.imshow(img)
    iax.set_xticks([])
    iax.set_yticks([])
    for sp in iax.spines.values():
        sp.set_visible(True); sp.set_color("#999"); sp.set_linewidth(0.6)
    return y0, h


def arrow(xy_from, xy_to):
    axq.annotate("", xy=xy_to, xytext=xy_from, zorder=7,
                 arrowprops=dict(arrowstyle="-|>", color="#555", lw=0.7, shrinkA=0, shrinkB=2))


def peak(a, b):
    w = full[(full.x >= a) & (full.x <= b)]
    r = w.loc[w.small_q.idxmax()]
    return r.x, r.small_q


HEADLINES = [  # file, x0, y0 (None = top), width in years, arrow target
    ("bw_oettinger_headline.png", 1984.4, None, 7.0, lambda: peak(1992.0, 1994.0), "side"),
    ("bw_mappus_headline.png", 1997.6, None, 8.0, lambda: peak(2009.5, 2011.0), "side"),
    ("bw_afd_headline.png", xr[1] - 0.15 - 10.4, 8, 10.4, lambda: tuple(full[full.label == "2017 H1"][["x", "small_q"]].iloc[0]), "up"),
]
for f, x0, y0, w, target, kind in HEADLINES:
    p = IMG_DIR / f
    if not p.exists():
        print(f"note: {p.name} not found - figure drawn without this headline")
        continue
    y0, h = add_img(p, x0, y0, w)
    tx, ty = target()
    arrow((x0 + w, y0 + h / 2) if kind == "side" else (tx, y0 + h), (tx, ty))

parties = [p for p in PARTY_ORDER if p in used]
fig.legend(handles=[Patch(color=PCOL[p], label=PN.get(p, p)) for p in parties], frameon=False, ncol=len(parties),
           fontsize=6, loc="upper center", bbox_to_anchor=(0.5, -0.42), bbox_transform=AX[1].transAxes)
FIG_DIR.mkdir(exist_ok=True)
fig.savefig(FIG_DIR / "fig_BW_timeline_questions.png", dpi=300, bbox_inches="tight")
print("saved", FIG_DIR / "fig_BW_timeline_questions.png")
