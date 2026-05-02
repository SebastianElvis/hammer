# Learner profile

This file tracks what you know, what you're working on, and what tripped you up. It is updated by the tutor at the end of each session. You can edit it by hand too — it's just markdown.

## Currently studying

SQL window functions

## Goal

Be able to write a query that ranks rows within partitions and reason about NULL handling in window frames.

## Known solid

- INNER JOIN semantics on a single key (verified 2026-04-12, 2026-04-20)
- GROUP BY collapsing rows to one per group (verified 2026-04-15, 2026-04-22)

## Shaky

- LEFT JOIN behavior on the right-side rows that don't match (seen 2026-04-18)

## Misconceptions caught

- 2026-04-12: believed JOIN without ON clause errors out; in fact it produces a CROSS JOIN.

## Calibration notes

- 2026-04-25: comfortable with joins and grouping, no prior exposure to window functions or PARTITION BY.
