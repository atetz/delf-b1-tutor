---
name: fle-grammar
description: Grammaire française niveau B1 / French grammar lesson and fresh drills on one point (négation, élision, accords, temps du récit, prépositions, relatifs, subjonctif, pronoms…). Use when the learner names a grammar point, asks "explain", "why is it…", "drill", "exercices de grammaire", or when a correction reveals a recurring grammar error.
argument-hint: "[topic]"
arguments: [topic]
---

# Grammar: one point, rule then drill

Paths: `references/…` is this skill's own folder; every other path starts at the repository root.

Topic requested: `$topic` (an unfilled placeholder starting with a dollar sign means: take it from the learner's message; empty: ask, or take the grammar weak point with the oldest due date).

## Topic files

Each file in `references/` has four parts: rule, typical errors, examples, drill recipe. Read only the one needed.

| Topic (id `morphosyntaxe/…`) | File | Covers |
|---|---|---|
| elision | `elision.md` | qu'il, d'apprendre, l', si/s'il; au, du, aux, des |
| accords | `accords.md` | gender and number of determiners, adjectives, past participles; place of the adjective |
| accord-verbe | `accord-verbe.md` | on, tout le monde, la plupart, qui; verb endings |
| cest-il-est | `cest-il-est.md` | c'est or il est with nouns, adjectives, professions; il y a |
| possessifs-demonstratifs | `possessifs-demonstratifs.md` | son/sa/ses, leur/leurs, le mien; ce/cet/cette, celui qui, celui de |
| pronominaux | `pronominaux.md` | se lever, se souvenir de; place of the pronoun, être, agreement |
| temps-du-recit | `temps-du-recit.md` | passé composé, imparfait, plus-que-parfait in a story; être or avoir |
| negation | `negation.md` | ne…pas/plus/jamais/rien/personne, pas de, place of the negation |
| prepositions | `prepositions.md` | verb + à/de, avoir besoin de, demander à qqn de, countries and time |
| relatifs | `relatifs.md` | qui, que, où, dont, ce qui, ce que; la raison pour laquelle |
| subjonctif | `subjonctif.md` | forms and the B1 triggers |
| pronoms | `pronoms.md` | le/la/les, lui/leur, y, en, order and place |
| questions | `questions.md` | est-ce que, inversion, qui/que/quoi, quel, lequel; indirect questions |
| indefinis | `indefinis.md` | tout/tous/toutes, chaque, quelques, plusieurs, quelque chose de + adjective |
| adverbes | `adverbes.md` | -ment, bon/bien, mauvais/mal; place of the adverb |
| present | `present.md` | stems and endings of irregular verbs in the present |
| futur | `futur.md` | futur proche, futur simple, quand + futur; venir de, être en train de |
| conditionnel | `conditionnel.md` | politeness, advice, wish; conditionnel passé for regret |
| hypothese | `hypothese.md` | the three si patterns; si or quand |
| imperatif | `imperatif.md` | forms, negation, pronouns after the verb |
| gerondif | `gerondif.md` | en + -ant; when English -ing is an infinitive |
| passif | `passif.md` | être + participle, par; on and pronominal alternatives |
| discours-rapporte | `discours-rapporte.md` | que, si, ce que, de + infinitive; tense shift after a past verb |
| comparaison | `comparaison.md` | plus/moins/aussi/autant, meilleur/mieux, superlative |
| expressions-de-temps | `expressions-de-temps.md` | depuis, il y a, pendant, pour, en, dans; avant de, après avoir |
| articles | `articles.md` | definite, indefinite, partitive; de after negation and quantity; no article |

A loose name (« passé composé », « past tenses », « pas de ») maps to the nearest file. No file for the point
(see `reference/grammar-checklist.md`): teach it with the same four parts from your own knowledge, then
offer to save it as a new file and add its id to `reference/topics.md`.

## Procedure

1. **Past errors first.** Show the rows of `learner/weak-points.md` whose Fix with is this topic, with the
   learner's own wrong sentences. They are the starting point of the lesson.
2. **Rule, 3 minutes.** Explain from the topic file in English, examples in French. Start from the learner's
   errors, then the rule, then the cases that trap Dutch and English speakers. Write new example sentences on a
   theme the learner cares about; the file's examples are models, not a script.
3. **Check.** Ask the learner to correct two of their own past errors, or two sentences in that pattern.
4. **Drill, 6 to 8 items,** generated fresh from the file's drill recipe (types in
   `.claude/skills/delf-review/references/drill-types.md`). Give them in two batches; wait for answers each time.
5. **Correct.** Right or wrong per item, the corrected form, one line of why for wrong ones. Then the score out of the total.
6. **Record.**
   - 80% or more right: the topic's weak-point rows move one interval forward.
   - Less: rows go back to Interval 1, Next review tomorrow.
   - Point not yet in `weak-points.md` and under 80%: add a row (Seen in: the paper where it last appeared, or PE).
   - Log row in `learner/log.md` (focus `grammar`, task = topic) and a short note in today's session file,
     unless this was called inside another skill's session, in which case add one line to that skill's note.
   Formats: `reference/recording.md` and `reference/spaced-review.md`.

Called from a correction (writing or speaking) with five minutes left: do steps 2 and 4 only, with 4 items.

## Extra practice outside the session

For more exercises in a browser, the learner can search the point on Le Point du FLE (https://www.lepointdufle.net),
a directory of free exercises sorted by topic and level. Link only: nothing from those sites is copied here.
