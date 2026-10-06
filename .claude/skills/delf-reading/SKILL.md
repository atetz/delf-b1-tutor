---
name: delf-reading
description: Compréhension des écrits / DELF B1 reading practice. Writes a fresh B1 text and exam-style questions (matching options to criteria, vrai/faux with justification, multiple choice), runs it under exam timing, then corrects with the deciding passage for each answer and a mark out of 25. Use for "CE", "reading", "compréhension écrite", "lecture", "give me a text".
argument-hint: "[theme]"
arguments: [theme]
---

# Compréhension des écrits (CE)

Paths: `references/…` is this skill's own folder; every other path starts at the repository root.

Theme requested: `$theme` (an unfilled placeholder starting with a dollar sign means: take it from the learner's message; empty = choose one).

## 1. Inputs

- **Theme:** from the router's brief or `reference/themes.md`, not one of the last three in `learner/log.md`.
- **Difficulty:** `guided` (one exercise, no timer, technique discussed first) or `exam` (timed, no help).
- **Weak points:** rows of `learner/weak-points.md` whose Seen in contains CE (`comprehension/ce-justification`,
  `comprehension/ce-reperage`, vocabulary ids).

## 2. Generate the task

Read `references/task-types.md` and write the documents and questions fresh, in French.
In a 35-minute slot: exercise 1 (matching) plus one article, or two articles. A full paper (all three exercises,
45 minutes) only in exam mode when the learner has the time.
Prepare the answer key with the deciding passage for each question before showing anything, and keep it to yourself.

## 3. Run it

- Guided mode: first ask the learner how they plan to tackle it, and read
  `references/answer-technique.md` to fill the gaps in two or three lines.
- Give one exercise at a time with its time limit: the documents, then all its questions. Wait for the answers.
- No dictionary, no hints, no meaning of words until the answers are in. If asked what a word means, say they
  can guess from context as in the exam, and note the word for later.
- Vrai/faux answers must come as: V or F, then the quoted words that prove it.

## 4. Correct and score

1. Mark with `references/scoring.md`.
2. For each wrong or incomplete answer: the right answer, the exact passage that decides it, and what misled
   (a distractor word, a negation, an opinion read as a fact, a justification that is true but proves something else).
3. Read `answer-technique.md` if not yet read and give the one technique point that would have saved most marks.
4. Vocabulary: list up to eight useful words from the text the learner asked about or probably did not know,
   with meaning and the sentence they appeared in.

## 5. Record

Follow `reference/recording.md`: log row, CE score (Latest only if at least two exercises were done under
exam timing; otherwise in the log row), weak points with a `comprehension/` id, words in `learner/vocabulary.md`.
The session note keeps the text's title and theme, the questions missed and the deciding passages, not the whole text.
