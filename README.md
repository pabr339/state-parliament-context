# State parliament processes in their political context

Data and scripts accompanying the paper on how electoral cycles and government–opposition
constellations shape long-term legislative process behaviour in three German state parliaments:
Berlin (BE), Brandenburg (BB) and Baden-Württemberg (BW). Electoral terms are used as temporal
brackets; comparing process metrics across brackets reveals shifts that a single-period view hides
(e.g. the change in how opposition bills are handled in Brandenburg from 1999).

This repository contains

1. **`data/political_context/`** – a new dataset on the political context of the three parliaments
   (elections, vote and seat shares, cabinets, government segments, party roles), 1980–2026, with the
   source of every value; see its [README](data/political_context/README.md) and [codebook](data/political_context/CODEBOOK.md).
2. **`scripts/`** – the code to recompute the figures of the paper.

## Legislation data: Hillmann et al. (2025)

The legislative process data (event logs) are **not** part of this repository. They stem from the
repository of

> P.-J. Hillmann, S. A. Fahrenkrog-Petersen, J. Mendling (2025). *Cross-Organizational Analysis of
> Parliamentary Processes: A Case Study.* 7th International Conference on Process Mining (ICPM 2025).
> DOI: [10.1109/ICPM66919.2025.11220746](https://doi.org/10.1109/ICPM66919.2025.11220746)

Repository: <https://github.com/pjhi/coPM-German-State-Parliament-Data> (processed datasets licensed
CC BY 4.0). The logs were built by Hillmann et al. from the parliamentary documentation services of the
Landtag von Baden-Württemberg, the Abgeordnetenhaus Berlin and the Landtag Brandenburg.

**To use them with this repository**, download the three *preprocessed* event logs from the folder
`eventLogs/` of that repository and place them, unchanged, in `data/eventlogs/`:

```
data/eventlogs/berlin-all-preprocessed.xes.zip
data/eventlogs/brandenburg-all-preprocessed.xes.zip
data/eventlogs/baden-württemberg-all-preprocessed.xes.zip
```

No further preprocessing is needed. `scripts/01_prepare_data.py` uses the following attributes of the
logs: `case:concept:name`, `concept:name`, `time:timestamp`, `Wp`, `Urheber`, `DokArtL`, `case:VTyp`
and `case:VTypL`.

## Reproducing the figures

```bash
pip install -r requirements.txt
cd scripts
python 01_prepare_data.py                  # event logs -> derived/bills.csv, derived/halfyear_series.csv (~1 min)
python fig_states_context_metrics.py       # figures/fig_states_context_metrics.png
python fig_BW_timeline_questions.py   # figures/fig_BW_timeline_questions.png
python fig_BB_oppositionbills.py      # figures/fig_BB_oppositionbills.png
```

The figure scripts also write the numbers they plot to `derived/`.
The Baden-Württemberg figure in the paper contains three newspaper headlines; these screenshots are not
distributed (publishers' copyright). The script draws the figure without them – see
[`data/images/README.md`](data/images/README.md).

## Definitions used in the scripts

- **Bill**: a case of process type `Gesetz` that contains a draft bill (`Gesetzentwurf`). Each bill is
  assigned to the electoral term and government segment in force on its introduction date.
- **Initiator**: from the author field (`Urheber`) of the draft. *Government side* = state government
  or parliamentary groups of the governing (or tolerating) parties; *opposition* = groups of opposition
  parties only; joint bills of both camps (*cross-camp*) and unclear authors are excluded from the
  government/opposition comparisons.
- **Outcome**: *promulgated* (law gazette event), *final vote* (case ends ≤ 60 days after its last
  final plenary event), *lapsed* (term ended), *censored* (term still running at the end of the data,
  31 Aug 2024).
- **Cycle time**: days from the first to the last event of a case. **Draft → decision**: days from
  introduction to promulgation or final plenary vote (decided bills only).
- **Rejected at first reading (Brandenburg)**: opposition bill, not promulgated, exactly one plenary
  reading event (activity label contains `Lesung`) and no committee document (`Ausschussprotokoll` or
  `Beschlussempfehlung`). The plenary vote itself is not recorded in the logs; rejection is inferred
  from this pattern.
- **Written small questions**: cases starting with a *Kleine Anfrage* (BE also *Schriftliche Anfrage*;
  BW *Kleine Anfrage und Antwort*), counted by the date of the answer.

## Repository structure

```
data/political_context/   political context dataset (CSV) + build scripts
data/eventlogs/           place the Hillmann et al. event logs here (not included)
data/images/              optional newspaper screenshots (not included)
scripts/                  data preparation and figure scripts
```

## License

Code: MIT. Political context dataset: CC BY 4.0. See [`LICENSE`](LICENSE) for details and for the
terms of the third-party data used. Note that the scripts use [pm4py](https://pm4py.fit.fraunhofer.de/),
which is licensed under AGPL-3.0.
