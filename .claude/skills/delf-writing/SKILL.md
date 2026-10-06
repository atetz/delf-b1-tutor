---
name: delf-writing
description: Production écrite / DELF B1 writing practice. Sets one exam-style writing task (forum post, letter, email, article, 160 words minimum, 45 minutes), then corrects it criterion by criterion with an estimated mark out of 25. Use for "PE", "writing", "production écrite", "give me a writing task", or to correct a French text the learner wrote.
argument-hint: "[theme]"
arguments: [theme]
---

# Production écrite (PE)

Paths: `references/…` is this skill's own folder; every other path starts at the repository root.

Theme requested: `$theme` (an unfilled placeholder starting with a dollar sign means: take it from the learner's message; empty = choose one).

## 1. Inputs

From the router's brief, or decide yourself when run directly:
- **Theme:** from `reference/themes.md`, not one of the last three in `learner/log.md`.
- **Difficulty:** `guided` (no timer, plan checked before writing) in phase 1, `exam` (45 min, no help) after.
- **Weak points to weave in:** rows of `learner/weak-points.md` whose Seen in contains PE, due ones first, three at most.

If the learner pasted a text to correct, skip to step 4.

## 2. Generate the task

Read `references/genres.md` and write one fresh instruction in French: a situation, a reader,
a genre, what to include, "160 mots minimum". Vary the genre from the last PE session. Choose a situation that
naturally calls for the weak points (a story in the past for narrative tenses, a complaint for negation), without
naming them.

## 3. Run it

- Give the instruction and the time limit, then wait. No vocabulary help, no plan, no hints unless asked.
- If asked for help in exam mode, give it and note in the session file that the text was assisted.
- Guided mode only: ask for a four-line plan first and comment on it in two lines.

## 4. Correct and score

1. Count the words. Read `references/correction-format.md` and follow it: LanguageTool first when installed,
   then review every hit, then add what it missed, each correction labelled **rule**, **usage** or **style**.
2. Rate the five criteria with `references/criteria.md` (below / B1 / B1+), then the /25 estimate.
3. Present in this order: mark and one-line verdict, criterion table, corrections grouped by topic id, full
   corrected version, then the two changes that would gain most points next time.
4. For the most frequent error type, point to its topic file (ids in `reference/topics.md`)
   and offer a five-minute drill with `fle-grammar` or `fle-vocabulary` if time remains.

Correct the text the learner wrote; do not rewrite it into a different, better text. The corrected version keeps
their ideas, order and level.

## 5. Record

Follow `reference/recording.md`: log row, PE score and per-criterion row in `scores.md`, weak-point rows
(new or reset to day 1), and the session note with the instruction, the original text and the corrected version.
