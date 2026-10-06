---
name: delf-speaking
description: Production orale / DELF B1 speaking practice. The assistant plays the examiner for the three parts (entretien dirigé, exercice en interaction, expression d'un point de vue); the learner answers by dictation or typing and gets criterion-by-criterion feedback with a mark out of 25. Use for "PO", "speaking", "oral", "production orale", "role play", "jeu de rôle", "monologue".
argument-hint: "[theme]"
arguments: [theme]
---

# Production orale (PO)

Paths: `references/…` is this skill's own folder; every other path starts at the repository root.

Theme requested: `$theme` (an unfilled placeholder starting with a dollar sign means: take it from the learner's message; empty = choose one).

## 1. Inputs

- **Theme and weak points:** from the router's brief, or choose a theme from `reference/themes.md` and take
  the rows of `learner/weak-points.md` whose Seen in contains PO (three at most).
- **Which parts:** all three fit in 35 minutes once the learner knows the format. Early on, or when
  `learner/scores.md` shows one task rated below, run that part twice with different material instead.
- **Profile:** read `learner/profile.md` for the entretien (job, city, reasons for learning) and for how answers
  arrive: dictation or typing.

## 2. Generate the task

Read only the files for the parts you will run:
- part 1: `references/entretien.md`
- part 2: `references/interaction.md`
- part 3: `references/point-de-vue.md`

Write a fresh scenario card for part 2 and a fresh prompt text for part 3 on today's theme.

## 3. Run it

Stay in the examiner role, in French, from « Bonjour, asseyez-vous » to the end of the last part.
- One examiner turn at a time, short, then wait. Never answer for the learner.
- No corrections, hints or English during a part. If the learner is stuck, do what an examiner does: rephrase
  the question once, more simply.
- Part 2: play the other person with a real objection, so there is something to negotiate (see the file).
- Part 3: give the prompt, announce 10 minutes of preparation, wait for « prêt ». Let the monologue run to its
  end, then ask two or three questions.
- Dictated answers: ask the learner not to tidy up the transcript. Hesitations and slips are the material.
- Between parts, announce the next one in one line, as an examiner would.

## 4. Correct and score

1. Step out of the role and say so.
2. Run the correction procedure in `.claude/skills/delf-writing/references/correction-format.md` on the
   learner's turns (LanguageTool first when installed). Ignore dictation artefacts: punctuation, capitals,
   and obvious speech-to-text mishearings (ask when unsure which it is).
3. Rate with `references/criteria.md`: the three tasks, lexique, morphosyntaxe, and phonologie only if it
   can be judged. Then the /25 estimate.
4. Present: mark and verdict, criterion table, corrections grouped by topic id, then for each part one sentence
   the learner said rewritten the way a B1+ speaker would say it.
5. Offer to replay the weakest part once, immediately, with a new scenario. The second try is not scored.

## 5. Record

Follow `reference/recording.md`. In `scores.md`, write the three task ratings in the Tâche cell. Update
Latest only when all three parts were run; otherwise the part estimate goes in the log row. The session note
keeps the scenario, the learner's key turns and their corrected versions.
