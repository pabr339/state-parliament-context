# Codebook

## elections

| variable | definition |
|---|---|
| `election_id` | State_ElectionDate key |
| `state` | BE / BB / BW |
| `election_type` | regular / early / unification / first / repeat / regular (annulled) |
| `territory` | Electoral territory (West Berlin until 1989) |
| `wahlperiode` | Legislative term number |
| `wp_constituent_session` | Date of constituent session of that Wahlperiode (NA if not found) |
| `cycle_start / cycle_end` | Election day / day before next election |
| `cycle_ongoing` | True if no subsequent election yet |
| `in_range_1984_2024` | Cycle overlaps 1984-01-01 – 2024-12-31 |
| `vote_type` | Vote used for shares |
| `electorate` | Wahlberechtigte |
| `voters` | Wähler |
| `turnout_pct_reported` | Official turnout (%) |
| `turnout_pct_computed` | voters/electorate×100 |
| `turnout_change_pp` | Turnout change vs previous election (pp) |
| `valid_votes / invalid_votes / invalid_pct` | Gültige / ungültige Stimmen |
| `n_parties_in_parliament / parties_in_parliament / seat_distribution` | Harmonised parties with ≥1 seat |
| `largest_party / largest_party_pct / margin_first_second_pp` | Plurality winner and lead |
| `enep_votes / enpp_seats` | Effective number of parties (votes / seats) |
| `gallagher_lsq` | Disproportionality index |
| `pedersen_volatility` | Net volatility vs previous election |
| `vote_share_other_unlisted` | Share of 'Sonstige' |
| `gov_formed_date / gov_formation_days` | First new government after election and days from election |
| `first_cabinet / first_head / first_gov_parties / first_gov_seat_pct / first_opposition_parties` | Government formed after the election |
| `n_gov_changes_in_cycle` | Later cabinet/coalition changes in the cycle (incl. head changes) |

## party_results_harmonised

| variable | definition |
|---|---|
| `party` | Harmonised party code |
| `party_labels` | Original list name(s) merged |
| `party_family` | Rough party family |
| `votes / vote_pct / seats / seat_pct` | Result |
| `prev_*` | Previous election values (prev_source if from baseline outside dataset) |
| `change_pp` | Vote share change (pp) |
| `change_rel_pct` | Relative growth of vote share (%) |
| `change_votes / change_seats` | Absolute change |
| `prev_listed` | Party listed individually in previous election |
| `in_parliament / was_in_parliament / entered_parliament` | Parliamentary status |
| `role_initial` | Role in first government formed after the election: government / tolerating / opposition / extra-parliamentary |
| `in_gov_any_time` | In government at any point of the cycle (incl. caretaker periods) |
| `gov_share_of_cycle` | Share of cycle days in government |
| `tolerating_any_time` | Tolerated a minority government at some point |

## party_results_lists

| variable | definition |
|---|---|
| `party_label` | List name as on ballot |
| `party` | Harmonised code |
| `vote_pct` | Computed from votes |
| `vote_pct_reported` | Published (1 decimal) |
| `change_*` | From harmonised table |

## government_timeline

| variable | definition |
|---|---|
| `segment_id` | State_StartDate |
| `seg_start / seg_end` | Inclusive dates; empty seg_end = ongoing |
| `seg_days` | Length in days (to 2026-10-13 if ongoing) |
| `cabinet / head_of_government / head_party` | Executive |
| `government_parties / tolerating_parties / opposition_parties` | Harmonised codes; opposition = seat-holding parties not in government or tolerating |
| `single_party_government / minority_government` | Flags (minority = ≤50 % of elected seats) |
| `gov_seats / gov_seat_pct` | Government seats in currently sitting parliament (as elected) |
| `caretaker` | True between an election and the formation of the next government (outgoing government in office) |
| `date_precision` | Precision of segment boundary dates |

## party_roles_timeline

| variable | definition |
|---|---|
| `role` | government / tolerating / opposition |
| `head_party` | Party of head of government |
| `caretaker_period` | Segment is a caretaker period |
