"""Shared paths, colours and plotting helpers for all figure scripts."""
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PC_DIR = ROOT / "data" / "political_context" / "combined"   # political context tables
LOG_DIR = ROOT / "data" / "eventlogs"                        # event logs from Hillmann et al. (not included)
DERIVED = ROOT / "derived"                                   # written by 01_prepare_data.py
FIG_DIR = ROOT / "figures"

STATES = {"BE": "berlin", "BB": "brandenburg", "BW": "baden-württemberg"}
NAME = {"BE": "Berlin", "BB": "Brandenburg", "BW": "Baden-Württemberg"}

# party colours (harmonised party codes of the political context data)
PCOL = {"CDU": "#1a1a1a", "SPD": "#E3000F", "GRUENE": "#1AA037", "FDP": "#E6B800", "LINKE": "#BE3075",
        "AFD": "#009EE0", "DVU": "#7B4A12", "FW": "#F28C00", "BSW": "#7D254F", "REP": "#8B5A2B", "PIRATEN": "#FF8800"}
PN = {"GRUENE": "Grüne", "LINKE": "PDS/Linke", "AFD": "AfD", "FW": "Freie Wähler", "PIRATEN": "Piraten", "REP": "Republikaner"}
PARTY_ORDER = ["SPD", "CDU", "LINKE", "GRUENE", "FDP", "AFD", "DVU", "REP", "FW", "PIRATEN", "BSW"]


def fy(d):
    """Date -> fractional year (x-axis unit of all figures)."""
    return d.year + (d.dayofyear - 1) / 365.25


def load_context():
    el = pd.read_csv(PC_DIR / "elections.csv")
    gt = pd.read_csv(PC_DIR / "government_timeline.csv")
    pr = pd.read_csv(PC_DIR / "party_roles_timeline.csv")
    return el, gt, pr


def load_bills():
    B = pd.read_csv(DERIVED / "bills.csv", parse_dates=["start", "end", "promul_date", "outcome_date"])
    B["case"] = B.case.astype(str)
    return B


def apply_style():
    mpl.rcParams.update({
        "font.family": "sans-serif", "font.size": 8, "axes.labelsize": 8, "axes.titlesize": 8,
        "legend.fontsize": 7, "xtick.labelsize": 6, "ytick.labelsize": 6, "axes.linewidth": 0.6,
        "xtick.major.size": 3, "ytick.major.size": 3, "xtick.major.width": 0.6, "ytick.major.width": 0.6,
        "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False,
        "figure.dpi": 200, "savefig.dpi": 300, "savefig.bbox": "tight", "axes.titlelocation": "left",
        "lines.linewidth": 1.2, "pdf.fonttype": 42, "ps.fonttype": 42})


def panel_letter(ax, letter, dx=-0.18, dy=1.02):
    ax.text(dx, dy, letter, transform=ax.transAxes, fontweight="bold",
            fontsize=plt.rcParams["font.size"] + 1, va="bottom", ha="left")


def draw_seats(ax, st, gt, pr, x0, x1, end_date, alpha_fn=None):
    """Stacked seat shares per government segment: government solid, tolerating 0.6, opposition 0.3.
    alpha_fn(role, seg_a, seg_b) may override the opacity. Returns the set of parties drawn and
    a list of (seg_a, seg_b, government seat share) tuples."""
    g = gt[gt.state == st].copy()
    g["a"] = pd.to_datetime(g.seg_start)
    g["b"] = pd.to_datetime(g.seg_end).fillna(end_date)
    used, segs = set(), []
    for r in g.itertuples():
        a, b = max(fy(r.a), x0), min(fy(r.b), x1)
        if b <= a:
            continue
        P = pr[(pr.state == st) & (pr.segment_id == r.segment_id)].copy()
        P["pct"] = 100 * P.seats / P.seats.sum()
        P["o"] = P.role.map({"government": 0, "tolerating": 1, "opposition": 2})
        P = P.sort_values(["o", "pct"], ascending=[True, False])
        y = 0
        for p in P.itertuples():
            alpha = {"government": 1.0, "tolerating": 0.6}.get(p.role, 0.3)
            if alpha_fn is not None:
                alpha = alpha_fn(p.role, a, b, alpha)
            ax.add_patch(mpl.patches.Rectangle((a, y), b - a, p.pct, color=PCOL.get(p.party, "#888"), alpha=alpha, lw=0))
            y += p.pct
            used.add(p.party)
        segs.append((a, b, P[P.role == "government"].pct.sum()))
        ax.axvline(a, color="white", lw=0.8)
    ax.axhline(50, color="white", lw=1, ls="--")
    ax.set_ylim(0, 100)
    ax.set_yticks([0, 50, 100])
    return used, segs
