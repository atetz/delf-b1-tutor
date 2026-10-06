---
name: delf-listening
description: Compréhension de l'oral / DELF B1 listening practice. Either real radio (the learner listens twice to a news bulletin in easy French, summarises, then pastes the transcript) or exam-shaped short recordings read aloud by text-to-speech, followed by questions, correction and a mark out of 25. Use for "CO", "listening", "compréhension orale", "écoute".
argument-hint: "[theme]"
arguments: [theme]
---

# Compréhension de l'oral (CO)

Paths: `references/…` is this skill's own folder; every other path starts at the repository root.

Theme requested: `$theme` (an unfilled placeholder starting with a dollar sign means: take it from the learner's message; empty = choose one; in radio mode the theme is whatever the bulletin covers).

The assistant cannot hear audio. The learner listens; the assistant works from the transcript afterwards (radio mode) or from
a script it wrote (exam mode).

## 1. Inputs

- **Mode:** read `references/sources.md` and choose. Default: `radio`. Use `exam` when the router asks for
  exam timing, in phase 3, or when the learner wants the three-document format, and text-to-speech works.
- **Weak points:** rows of `learner/weak-points.md` whose Seen in contains CO (`comprehension/co-details`,
  `comprehension/co-global`, `lexique/faux-amis`).

## 2. Generate the task

- **Radio:** nothing to generate yet. Give the learner the source and the listening instructions from `sources.md`.
- **Exam:** write three short scripts and their questions following `references/question-types.md`.
  Warn the learner to look away before the scripts appear on screen.

## 3. Run it

**Radio mode**
1. The learner listens once without pausing and notes: how many items, and for each one who, what, where.
2. Second listening, still no pausing: add numbers, dates, causes, consequences.
3. They write a summary in French, 80 to 120 words, plus any words they heard but did not understand.
4. Only then do they paste the transcript (or the part they listened to, about 3 to 5 minutes of it).
5. Write 8 questions from the transcript with `question-types.md`. The learner answers from memory and notes,
   without scrolling back to the transcript.

**Exam mode**
1. Show the questions for document 1 and give one minute to read them.
2. Play the document, pause 30 seconds, play it again, then one minute to finish. Take the answers.
3. Same for documents 2 and 3. No replays beyond the two listenings.

No hints and no vocabulary help until every answer is in.

## 4. Correct and score

1. Mark with `references/scoring.md`. For each wrong answer, quote the exact words of the transcript that
   decide it, and name the trap (number, negation, who did what, a distractor that was mentioned then rejected).
2. Radio mode: compare the summary with the transcript: items caught, items missed, anything misunderstood.
   The summary's French is corrected lightly (three corrections at most); this is a listening session.
3. Go through the words not understood: meaning, and why they were hard to hear (liaison, dropped e, speed).
4. Advise one focused re-listen with the transcript in view, on the passage that caused most errors.

## 5. Record

Follow `reference/recording.md`: log row with the source and date of the bulletin, CO score, weak points
with a `comprehension/` or `lexique/` id, new words in `learner/vocabulary.md`. Do not store the transcript in
the session note: keep the link or date, the questions missed and the deciding quotes only.
