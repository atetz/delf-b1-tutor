# Recording a session

Every skill that runs a task ends by writing state the same way. Dates are `YYYY-MM-DD`.
If `learner/` does not exist, create it first: `cp -r learner.example learner`.

## 1. `learner/log.md`: one row

`| 2026-10-06 | PE | forum post, télétravail | 13/25 | accords and élision again; good structure |`

Focus is CO, CE, PE, PO, review, grammar, vocabulary, placement or mock. Score is empty for lessons and reviews.

## 2. `learner/scores.md`

- Put the new estimate in **Latest** for that paper. Fill **Start** only if it is empty.
- **Trend**: append the score to the short history, oldest first, e.g. `11 → 12.5 → 13`.
- Recompute **Total /100** from the four Latest values when all four exist.
- For PE and PO, add one row to the per-criterion table with below / B1 / B1+ per criterion
  (PO: write the three task ratings in the Tâche cell, e.g. `T1 B1, T2 below, T3 B1`; `-` where not rated).
- An estimate from a part-task (one speaking part, one reading text) goes in the log, not in Latest.

## 3. `learner/weak-points.md`

Row format and intervals: `reference/spaced-review.md`. For each error type found (at most five new rows per
session, the costliest first):

- Already in the table: add the paper to **Seen in** if new, set Interval to 1 and Next review to tomorrow,
  Status `reviewing`. A retired point that comes back is un-retired the same way.
- New: add a row with Status `new`, Interval 1, Next review tomorrow, and the learner's own wrong sentence as example.
- **Fix with** must be an id from `reference/topics.md`. If none fits, add a new id there under the right
  criterion, marked `file to write`.

New words worth keeping go in `learner/vocabulary.md` the same way (Interval 1, Next review tomorrow, Status `new`).

## 4. `learner/sessions/YYYY-MM-DD.md`

Append if the file exists (warm-up and main task share a day). Keep it short enough to reread in two minutes:

```
## PE: forum post, télétravail (35 min)
Task: <the instruction, one or two lines>
Answer: <the learner's text, or the key turns of a spoken task>
Corrected version: <full corrected text for PE; key corrected sentences otherwise>
Corrections: <grouped by topic id, each labelled rule / usage / style>
Score: <per criterion, then /25>
Next time: <one or two things to do differently>
```

## 5. Tell the learner

Finish with three lines: the score, the one thing that would gain most points, and what was recorded.
