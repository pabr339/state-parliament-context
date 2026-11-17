# Event logs (not included)

Place the three **preprocessed** event logs of Hillmann et al. (2025) in this folder.
They can be downloaded from
<https://github.com/pjhi/coPM-German-State-Parliament-Data/tree/main/eventLogs>:

| file | state |
|---|---|
| `berlin-all-preprocessed.xes.zip` | Berlin (BE) |
| `brandenburg-all-preprocessed.xes.zip` | Brandenburg (BB) |
| `baden-württemberg-all-preprocessed.xes.zip` | Baden-Württemberg (BW) |

The zip files can stay zipped; `scripts/01_prepare_data.py` reads either the `.xes.zip` or an unpacked `.xes`
file with the same name. Only the *preprocessed* logs are used (not the `-all.xes` raw logs).
