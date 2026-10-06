---
name: fle-vocabulary
description: Vocabulaire français niveau B1 / French vocabulary lesson and fresh drills on one theme or word problem (travail, logement, environnement, connecteurs, faux amis for Dutch and English speakers, word families, set expressions, spelling). Use when the learner names a theme, says "vocabulaire", "words for…", "false friends", "faux amis", "how do you say…", or when a correction reveals a word-choice or spelling problem.
argument-hint: "[topic]"
arguments: [topic]
---

# Vocabulary: one theme or one word problem

Paths: `references/…` is this skill's own folder; every other path starts at the repository root.

Topic requested: `$topic` (an unfilled placeholder starting with a dollar sign means: take it from the learner's message; empty: ask, or take the `lexique/` weak point with the oldest due date, or today's session theme).

## Topic files

Each file in `references/` has four parts: core content, typical errors, examples, drill recipe. Read only the one needed.

| Topic | File | Id |
|---|---|---|
| False friends, Dutch and English → French | `faux-amis.md` | `lexique/faux-amis` |
| Word families (noun, verb, adjective of one root) | `familles-de-mots.md` | `lexique/familles-de-mots` |
| Set expressions and calques | `expressions.md` | `lexique/expressions` |
| Spelling of common words, accents | `orthographe.md` | `lexique/orthographe` |
| Connectors | `connecteurs.md` | `coherence/connecteurs` |
| Theme: work | `travail.md` | |
| Theme: housing | `logement.md` | |
| Theme: environment | `environnement.md` | |

Other themes are listed in `reference/themes.md`. No file for the theme: build the lesson on the spot with
the same four parts (20 to 25 words and expressions, sorted nouns with article / verbs with their preposition /
adjectives / ready-made phrases for giving an opinion on the theme), then offer to save it as a new file.

## Procedure

1. **Past errors first.** Show the rows of `learner/weak-points.md` with this topic's id and any rows of
   `learner/vocabulary.md` on the theme.
2. **Find out what is known.** Ask for a one-minute brain-dump: every French word the learner has for the theme.
   Teach around what is missing, not the whole sheet.
3. **Teach 10 to 12 items, no more.** Nouns always with un/une, verbs with their preposition, each item inside a
   short sentence written fresh. Group by meaning, not alphabetically. Point out false friends and family
   members as they come.
4. **Drill, 8 items,** fresh, from the file's recipe: recall from a definition, gap fill, then two or three
   sentences of the learner's own that could go straight into a writing or speaking task on the theme.
5. **Correct.** Word, gender, spelling and preposition each count. Give the corrected sentence.
6. **Record.**
   - Add the items that were new or missed to `learner/vocabulary.md` (word with article, meaning, the learner's
     corrected example sentence, Interval 1, Next review tomorrow, Status `new`). Ten at most per session.
   - A recurring problem (same false friend again, spelling pattern) gets or resets a row in
     `learner/weak-points.md` with its `lexique/` id.
   - Log row in `learner/log.md` (focus `vocabulary`, task = topic), unless called inside another skill's session.
   Formats: `reference/recording.md` and `reference/spaced-review.md`.

Unsure of a gender or a spelling: look that one word up (Le Robert or Larousse online) instead of guessing.
For expressions in context, the learner can search Reverso Context themself; nothing from those sites is stored here.
