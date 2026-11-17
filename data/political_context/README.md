# Political context of state legislation: Berlin, Brandenburg, Baden-Württemberg

Election results, governments and party roles for the three German states, structured so that every
dated legislative event can be assigned to its electoral term, government segment and the role
(government / tolerating / opposition) of each parliamentary party.

## Files

| file | content |
|---|---|
| `combined/*.csv` | all three states in one table each |
| `BE/`, `BB/`, `BW/` | the same tables split by state |
| `raw_data.py` | collected input values; every row carries its source (URL) |
| `build.py` | derives all tables from `raw_data.py` (`python build.py` rewrites the CSVs) |
| `CODEBOOK.md` | variable definitions |

## Sources

Values were collected from official statistical reports (Amt für Statistik Berlin-Brandenburg / Landeswahlleiter,
Bundeswahlleiterin, handbooks of the Landtag Brandenburg) where available, otherwise from wahlrecht.de,
the election-data compilations of the Konrad-Adenauer-Stiftung and Wikipedia. The source of every value is
stored in the `source` columns. Data status: October 2026. Events after mid-2026 (Berlin election
2026-09-20, BW government 2026, BB coalition change 2026) are less thoroughly cross-checked.

## Description

**Dataset.** Political context of state legislation: Berlin (BE), Brandenburg (BB), Baden-Württemberg (BW)

**Coverage.** All state elections whose electoral cycle overlaps 1984–2024: BE 1981–2026, BB 1990–2024 (+ events to 2026), BW 1980–2026. Baselines from 1979 (BE) and 1976 (BW) used only for change values of the first election.

**Unit of analysis.** elections = one row per election/cycle | party_results_lists = party list × election (as on ballot) | party_results_harmonised = harmonised party × election (incl. change since previous election) | government_timeline = non-overlapping date segments (split at every election and every change of cabinet/coalition) | party_roles_timeline = segment × seat-holding party with role | cabinets = individual cabinets | legislative_terms = Wahlperioden

**How to merge legislation.** Interval join on date: for a bill dated d in state s, take the government_timeline row with state == s and seg_start <= d <= seg_end (seg_end empty = ongoing). That row gives election cycle, Wahlperiode, cabinet, head of government, government/tolerating/opposition parties, seat shares, minority & caretaker flags. Join to elections via election_id for vote-based context, or to party_roles_timeline via segment_id for party-level roles.

**Election cycle definition.** cycle_start = election day; cycle_end = day before the next election. The parliament's party composition in government_timeline switches on election day (simplification; legally the new Landtag begins at its constituent session, see legislative_terms). Use the caretaker flag to drop/handle the interregnum between election and new government.

**Growth / change measures.** change_pp = vote share minus previous share (percentage points); change_rel_pct = relative growth in % of previous share; change_votes and change_seats in absolute terms. All computed on harmonised parties (e.g. AL/GRÜNE/Bündnis 90 → GRUENE; PDS/Linke.PDS/DIE LINKE → LINKE; FDP/DVP → FDP; BVB/FREIE WÄHLER → FW). Shares computed from absolute votes ÷ valid votes, so they may differ from published one-decimal values by rounding.

**Additional indices.** ENEP (effective number of electoral parties, Laakso-Taagepera; 'Sonstige' excluded), ENPP (effective number of parliamentary parties), Gallagher least-squares disproportionality, Pedersen volatility (harmonised parties; 'Sonstige' treated as one party, so it is a lower bound), largest party, margin first–second, government formation days, number of government changes within cycle.

**Party threshold.** Parties with ≥ 0.5 % (rounded) or seats are listed individually; the remainder is 'Sonstige' (OTHER).

**Seats.** Seats as elected (incl. overhang/compensation). Later changes in group strength (defections, splits, e.g. BSW Brandenburg 2025/26, AfD BB 2014) are NOT reflected. minority_government = government parties hold ≤ 50 % of elected seats.

**Turnout.** `turnout_pct_reported` (official) and `turnout_pct_computed` (voters ÷ electorate); also `invalid_pct`.

## Notes and caveats

- **BE**: 1981–1989 = West Berlin only; from 1990-12-02 unified Berlin. Change values for 1990 compare against West Berlin 1989 (territory change!). East Berlin had its own Stadtverordnetenversammlung (elected 1990-05-06) and Magistrat Schwierzina (1990-05-30 to 1991-01-24); between 1990-10-03 and 1991-01-24 Senat and Magistrat governed jointly. Not modelled in the timeline.
- **BE**: 1990: Grüne/AL (5.0 %) and Bündnis 90/Grüne/UFV (4.4 %) ran as separate lists; both harmonised to GRUENE (9.4 %, −2.4 pp).
- **BE**: 2021 election was annulled (Verfassungsgerichtshof, Nov 2022) and repeated 2023-02-12 within the same Wahlperiode 19. Change for 2023 is computed vs 2021 (Wikipedia convention); the official report compares vs 2016.
- **BE**: 1981 and 2001 were early elections. 1981 seat total 132 (party seats sum to 132); wahlrecht.de lists 133 – unresolved.
- **BE**: Electorate/voters missing for 1985, 1990, 1995 (turnout available). Invalid votes missing before 1999.
- **BE**: Senat Diepgen IV start (1996-01-25) and Diepgen V start (1999-12-09) are approximate/unverified; coalition composition (CDU+SPD) is unaffected. Constituent session dates for WP 9, 10, 13, 14 (exact), 20 not found; WP15 start (2001-11-29) inferred.
- **BE**: 2001-06-16 to 2002-01-17: SPD–Grüne minority Senate tolerated by PDS → PDS coded 'tolerating'. 1981-06-11 to 1983-03-17: CDU minority Senate tolerated by (part of) the FDP → FDP coded 'tolerating'.
- **BE**: 2026-09-20 election: final result 153 seats (legal basis of seat number disputed per wahlrecht.de). As of 2026-10-13 Senat Wegner is caretaker; no new Senate found.
- **BB**: 1990: no previous Landtag; change values NA. Electorate/voters for 1990 from secondary sources. Bündnis 90 (gov party) and Grüne (separate list, 2.8 %) both harmonised to GRUENE.
- **BB**: Bündnis 90 left the Ampel coalition in March 1994; exact day not verified → coded 1994-03-01 (precision 'month').
- **BB**: 1994: REP vote (≈1.1 %) only available inside 'Sonstige'. 1999: 89 seats (one SPD overhang seat).
- **BB**: 2024-12-11 SPD–BSW coalition; ended 2026-01-06 after the BSW group split; SPD minority until 2026-03-18; then SPD–CDU (44 of 88 elected seats – formally no majority on election-day seats; group strengths changed via defections).
- **BW**: Until 2021 one-vote system; from 2026 two votes – Zweitstimme reported. 2026 figures from Bundeswahlleiterin; valid votes 5,375,109 (the page shows 5.357.109, apparently a digit swap; party sums confirm 5,375,109).
- **BW**: Späth II–IV start dates set to constituent session (re-election days not verified). WP start/end 'official' dates (1 June / 1 May) partly derived from Art. 30 LV – see legislative_terms.
- **BW**: 1980 change values are back-calculated from the reported change vs 1976; seat changes for 1980 unavailable.
- **BW**: LINKE 2011 is not linked to WASG 2006 (separate harmonised codes); if you want continuity, recode WASG → LINKE.
- **All**: Cross-check: all main-party vote shares and turnout figures were compared against wahlrecht.de long series (BE, BB, BW); all agree within ±0.1 pp except BE 1995 REP (2.72 % here from en.wikipedia votes vs 2.6 % at wahlrecht.de).
- **All**: change_pp for small parties is NA if the party was not listed individually in the previous election (it may have been inside 'Sonstige'). Treat NA ≠ 0.
- **All**: Caretaker segments (election → new government) combine the OLD government with the NEW parliament's seat distribution; gov_seat_pct there shows the outgoing coalition's strength in the new house.

## License

CC BY 4.0 – see `LICENSE` in the repository root.
