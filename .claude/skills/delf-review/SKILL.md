---
name: delf-review
description: Révision espacée / spaced review of the learner's own weak points and vocabulary for DELF B1. Use for the 10-minute warm-up of a session, the Friday grammar review, "révision", "warm-up", "review my mistakes", or when a known weak point shows up again.
argument-hint: "[warmup|full]"
allowed-tools: Bash(python3 scripts/*) Bash(python3 ${CLAUDE_PROJECT_DIR}/scripts/*)
---

# Spaced review

Paths: `references/…` is this skill's own folder; every other path starts at the repository root.

Mode: `$ARGUMENTS` (an unfilled placeholder starting with a dollar sign means: take it from the learner's message; empty: `warmup` when called inside a session, `full` when it is the day's main task).

## 1. Inputs

The due rows of `learner/weak-points.md` and `learner/vocabulary.md` (Next review today or earlier, not retired).
If the router did not already list them, run `python3 scripts/today.py`.
Rules for intervals: `reference/spaced-review.md`.

## 2. Build the review

- Group the due rows by **Fix with**. Open only the topic files for those ids (paths in
  `reference/topics.md`) and use their drill recipe. No file yet: use
  `references/drill-types.md`.
- **Warm-up (10 min):** at most 5 weak points and 5 words, 2 items each. Oldest due date first.
- **Full (35 min):** all due items, 3 to 4 items each, then one new point: the next unchecked line of
  `reference/grammar-checklist.md` that matches the criterion rated lowest in `learner/scores.md`.
  Teach it by invoking `fle-grammar` (or `fle-vocabulary` for a `lexique/` id) with that topic.
- Every item is new: never reuse the learner's stored example sentence as the question, only its error type.
  Use today's theme when the router gave one.

## 3. Run it

- One block per weak point. Give all its items at once, wait for the answers.
- No rule reminder before the items: the point is to see whether it holds without help.
- Vocabulary: ask for the French from the meaning, then a sentence using it.

## 4. Correct

- Mark each item right or wrong, show the corrected form, and give the rule in one line only for wrong ones.
- A weak point counts as **right** when every item on it is right (a typo outside the point does not count).

## 5. Record

Update each reviewed row in `learner/weak-points.md` and `learner/vocabulary.md`:

| Result | Interval | Next review | Status |
|---|---|---|---|
| right, was 1 | 3 | today + 3 | reviewing |
| right, was 3 | 7 | today + 7 | reviewing |
| right, was 7 | 14 | today + 14 | reviewing |
| right, was 14 | | | retired |
| wrong | 1 | tomorrow | reviewing |

Then end with one line: how many right, how many back to day 1. In full mode, also add the log row and session
note described in `reference/recording.md`. In warm-up mode the main task's skill writes the log row; add a
"Warm-up" line to today's session note only.
