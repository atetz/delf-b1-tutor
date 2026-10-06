# Spaced review

Intervals: 1 → 3 → 7 → 14 days → retired.
Right in review → move to the next interval. Wrong → back to 1 day.

Row format in `learner/weak-points.md`:

| Weak point | Seen in | Fix with | Example of the error | Interval | Next review | Status |
|---|---|---|---|---|---|---|

- Seen in: CO, CE, PE, PO (one or more).
- Fix with: one id from `reference/topics.md`.
- Interval: the current interval in days (1, 3, 7 or 14).
- Next review: a date, `YYYY-MM-DD` (`scripts/today.py` lists rows whose date is today or earlier).
- Status: new, reviewing, retired.

After a review, Next review = today + the new interval. Right at 14 days → Status `retired`, Next review empty.
`learner/vocabulary.md` uses the same intervals, dates and statuses.
