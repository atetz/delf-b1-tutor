# DELF B1 coach as Claude Code skills: proposed architecture

Status: design only, nothing built yet. Revised 2026-09-26 after checking against https://code.claude.com/docs/en/skills (see §8).

## 1. Principles

1. **Thin router, fat specialists.** One small orchestrator skill decides *what* today's session is and hands off.
   Each exam skill lives in its own skill folder, so a Tuesday reading session never loads writing grids or speaking prompts.
2. **Progressive disclosure inside each skill.** `SKILL.md` stays short (the procedure). Task templates, scoring criteria
   and example material sit in `references/` and are read only at the step that needs them.
3. **State is data, not instructions.** Scores, weak points and session notes are plain files under `learner/`.
   Skills read and write them; no learner-specific facts are baked into a skill.
4. **Only original or public material.** Exam format comes from the public France Éducation International description.
   Everything else (tips, criteria, texts, role plays, exercises) is written fresh in our own words. No book name,
   publisher, page number, quotation, or reproduced exercise anywhere in the repo.

## 2. Repository layout

```
delf-b1-tutor/
├── AGENTS.md                     # what the repo is, session shape, where state lives, the content rule, how to run skills
├── CLAUDE.md                     # one line: imports AGENTS.md
├── .agents/skills -> ../.claude/skills
├── reference/                    # shared, public-safe, loaded on demand
│   ├── exam-format.md            # 4 épreuves, timings, /25 each, pass = 50/100 and ≥5 per skill
│   ├── b1-descriptors.md         # what B1 means per skill, in plain words
│   ├── grammar-checklist.md      # B1 grammar points (today's plan.md §6)
│   ├── themes.md                 # topic list: travail, logement, santé, environnement…
│   ├── spaced-review.md          # 1 → 3 → 7 → 14 → retired; wrong → back to 1
│   └── topics.md                 # criterion/topic ids → file (morphosyntaxe/negation → fle-grammar/references/negation.md)
├── .claude/skills/
│   ├── delf-session/             # ORCHESTRATOR
│   │   └── SKILL.md
│   ├── delf-placement/           # FIRST SKILL: diagnostic, also used as monthly checkpoint
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── tasks.md          # 4-part structure, how to generate each part at B1 level
│   │       ├── scoring.md        # how to turn answers into /25 estimates
│   │       └── sample-set.md     # one original ready-made set (e.g. the télétravail text we used)
│   ├── delf-listening/           # CO
│   │   ├── SKILL.md              # RFI "Journal en français facile" method: listen ×2, summarise, paste transcript
│   │   └── references/{question-types.md, scoring.md, sources.md}
│   ├── delf-reading/             # CE
│   │   ├── SKILL.md
│   │   └── references/{task-types.md, answer-technique.md, scoring.md}
│   ├── delf-writing/             # PE
│   │   ├── SKILL.md
│   │   └── references/{genres.md, criteria.md, correction-format.md}
│   ├── delf-speaking/            # PO: examiner role, 3 parts, dictated answers
│   │   ├── SKILL.md
│   │   └── references/{entretien.md, interaction-scenarios.md, point-de-vue.md, criteria.md}
│   ├── delf-review/              # grammar + weak-point spaced review (Friday, and the 10-min warm-up)
│   │   ├── SKILL.md
│   │   └── references/drill-types.md
│   ├── delf-mock/                # full timed exam, Phase 3; calls the four skills' task generators in exam order
│   │   └── SKILL.md
│   ├── fle-grammar/              # rules + fresh drills, one file per grammar point
│   │   ├── SKILL.md              # short index: topic → file, lesson and drill procedure
│   │   └── references/{subjonctif.md, negation.md, prepositions-verbes.md, passe-compose-imparfait.md, pronoms.md, accords.md, …}
│   └── fle-vocabulary/           # themes, word families, collocations, false friends
│       ├── SKILL.md
│       └── references/{faux-amis-nl-en.md, travail.md, logement.md, environnement.md, connecteurs.md, …}
├── learner/                      # PERSONAL STATE (private, see §5)
│   ├── profile.md                # who the learner is, context for role plays, exam date, phase
│   ├── scores.md                 # /25 per skill: start, latest, target, history
│   ├── weak-points.md            # the spaced-review table
│   ├── vocabulary.md             # words and expressions to learn, same spaced review
│   ├── log.md                    # one line per session
│   └── sessions/YYYY-MM-DD.md    # detailed notes per session
├── scripts/
│   ├── today.py                  # prints date, weekday, due weak points, latest scores for the router
│   └── check-no-source.sh        # pre-commit grep for the book's title, publisher, "p. 12"-style refs, *.pdf
└── .gitignore                    # *.pdf, *.mp3, learner/ (if the repo is public)
```

Why the tracker is split into three files: the warm-up only needs `weak-points.md`, the orchestrator only needs the
latest scores and the last few log lines. Splitting keeps each read small.

## 3. The skills

| Skill | Triggers on | Reads | Writes |
|---|---|---|---|
| `delf-session` | "session", "let's practise", "what's today" | `profile.md`, `scores.md`, due rows of `weak-points.md`, last 5 lines of `log.md` | nothing itself; passes the plan to the specialist |
| `delf-placement` | "placement", "assessment", "checkpoint", or no `scores.md` yet | `exam-format.md`, its own references | `scores.md` (start column), `weak-points.md` (initial rows), `sessions/…-placement.md` |
| `delf-listening` | CO / listening | `sources.md`, `question-types.md` | log line, CO score, weak points, session note |
| `delf-reading` | CE / reading | `themes.md`, `task-types.md` | same pattern |
| `delf-writing` | PE / writing | `genres.md`, `criteria.md`, grammar weak points | same pattern |
| `delf-speaking` | PO / speaking / oral | `profile.md` (for the entretien), scenario files | same pattern |
| `delf-review` | warm-up, grammar, Friday | `weak-points.md`, `grammar-checklist.md` | interval and next date per weak point |
| `delf-mock` | mock, examen blanc | `exam-format.md`, each specialist's task references | all four scores, one session note |
| `fle-grammar` | a grammar point by name, "explain", "drill", or an error found during correction | the one topic file needed | weak-point rows (grammar), log line |
| `fle-vocabulary` | a theme, "vocabulaire", false friends | the one theme file needed | `vocabulary.md`, log line |

### Orchestrator (`delf-session`)

Kept deliberately small. Today's date, weekday and due weak points are injected when the skill loads
(`!`python3 ${CLAUDE_PROJECT_DIR}/scripts/today.py || true``), so Claude doesn't spend turns reading files. Procedure:

1. Read the injected summary (profile line, latest scores, due weak points, last log lines).
2. Pick today's focus: weekday rhythm (Mon CO, Tue CE, Wed PE, Thu PO, Fri review, Sat mixed or mock),
   overridden by phase and by the lowest skill (e.g. Saturday = second writing day while PE is lowest).
3. Run the 10-minute warm-up by invoking `delf-review` on the due items.
4. Invoke exactly one specialist skill for the 35-minute task with a one-line brief (skill, theme, difficulty, weak points to target).
   One session = one conversation: start a fresh one the next day, because invoked skills stay in context.
5. Make sure the specialist wrote its log line and score. That is the only bookkeeping the orchestrator checks.

It never contains exercises, criteria or tips; those belong to the specialists.

### Contract every specialist follows

Each specialist `SKILL.md` has the same five sections so they behave consistently:

1. **Inputs**: theme, difficulty, weak points to weave in (from the orchestrator, or asked if run directly).
2. **Generate the task** from its templates (fresh text/scenario each time, B1 level, exam timing).
3. **Run it**: one part at a time, wait for the learner's answer, no hints unless asked.
4. **Correct and score**: against its `criteria.md`, errors grouped by type, corrected version, estimated /25.
5. **Record**: append to `log.md`, update `scores.md`, add or bump rows in `weak-points.md` (format in `reference/spaced-review.md`), write `sessions/DATE.md`.

Because every skill writes state the same way, any of them can be run directly ("give me a writing task") without the orchestrator.

### How weak points find their skill

Each row in `learner/weak-points.md` carries two tags:

- **seen in**: the exam part where the error happened (CO, CE, PE, PO).
- **fix with**: a two-level topic id from `reference/topics.md`, `<criterion>/<topic>`, mapped to exactly one file.

**Level 1 = the official DELF B1 criteria** from the FEI *descripteurs de performance* for PE and PO (each rated
en dessous / B1 / B1+):

| Criterion id | PE | PO | Covers |
|---|---|---|---|
| `tache` | réalisation de la tâche | tâches 1, 2, 3 | answering the task: opinion + examples, entretien, interaction, point de vue |
| `coherence` | cohérence et cohésion | (part of tâche 3) | connectors, structure, layout, punctuation |
| `socioling` | adéquation sociolinguistique | (part of tâche 2) | register, tu/vous, speech acts, politeness |
| `lexique` | lexique | lexique | range, word choice, periphrasis, spelling of words |
| `morphosyntaxe` | morphosyntaxe | morphosyntaxe | grammar and grammatical agreement |
| `phonologie` | | système phonologique | pronunciation, intonation (limited: answers are dictated) |
| `comprehension` | CO / CE (no grid, right/wrong answers) | | answer technique, detail tracking |

**Level 2 = our own topic list**, written in our own words. Example weak points from a placement, mapped:

| Weak point | seen in | fix with |
|---|---|---|
| « parce que ils », « que à » | PE, PO | morphosyntaxe/elision |
| « une vrai problem », « un bon organisation » | PE | morphosyntaxe/accords |
| « on se rencontrent » | PE | morphosyntaxe/accord-verbe |
| « je me dis » → disais, « j'ai arrêté » → avais arrêté | PO | morphosyntaxe/temps-du-recit |
| « pas des exceptions », dropped ne | PO | morphosyntaxe/negation |
| « besoin à », « demander mon employeur pour » | PO | morphosyntaxe/prepositions |
| « raison pourquoi » | PO | morphosyntaxe/relatifs |
| « flexibilitée », « tems », « example » | PE | lexique/orthographe |
| « le télétravaille » vs « je télétravail » | PE | lexique/familles-de-mots |
| « rendre une visite », « chaque 3 mois » | PE | lexique/expressions |
| sens, vitrine, entreprise vs commerce | CO, PO | lexique/faux-amis |
| accepted the first compromise | PO | tache/po-interaction |
| no intro, example or conclusion | PO | tache/po-point-de-vue |
| vrai/faux not written, answers too short | CE | comprehension/ce-justification |
| mixed up who did what, numbers | CO | comprehension/co-details |

The skill that corrects the work must pick an id from `topics.md` when it records a weak point. If none fits, it adds a
new level-2 id under the right criterion, marked "file to write", so nothing is dropped.

Skills then filter: the warm-up groups due rows by *fix with* and opens only those files; a specialist filters by
*seen in* to weave the learner's own errors into the task; `/fle-grammar negation` also shows past errors tagged with that id.
`morphosyntaxe/*` topics live in `fle-grammar`, `lexique/*` in `fle-vocabulary`, `tache/*` and `comprehension/*` in the
exam skill's own references, `coherence/*` and `socioling/*` in `delf-writing` and `delf-speaking`.

**Scoring per criterion.** `delf-writing` and `delf-speaking` rate each official criterion (below / B1 / B1+) before giving
the /25 estimate, and `scores.md` keeps that per-criterion history, so the router can see e.g. that morphosyntaxe is the
criterion holding PE back.

**Keeping the grids private.** Both PDFs are marked « document réservé aux correcteurs / examinateurs ». The repo uses
only the criterion names and our own plain-language summary of each level; the PDFs stay out of git.

### Grammar and vocabulary (`fle-grammar`, `fle-vocabulary`)

Two skills with one reference file per topic, not one skill per topic: that keeps the descriptions in context to two
and lets the router or a specialist point to a single topic file.

Every topic file has the same four parts:

1. **Rule**, in a few lines of our own wording.
2. **Typical errors** for Dutch and English speakers, seeded from `learner/weak-points.md` (e.g. « pas des » → « pas de »).
3. **3–5 original example sentences.**
4. **Drill recipe**: which exercise types suit this point (gap fill, transformation, error correction, translation NL/EN → FR)
   and how to grade them. Exercises are generated fresh each time, never stored as a fixed bank.

Use: `/fle-grammar subjonctif` or `/fle-vocabulary logement` for a lesson plus drill; `delf-review` uses them on Fridays and
in the warm-up; the writing and speaking skills point to the matching topic file when a correction reveals the error.
Vocabulary learned goes into `learner/vocabulary.md` with the 1 → 3 → 7 → 14 day review.

Grammar and vocabulary books can guide *which* topics to cover and in what order. Their explanations, example sentences
and exercises are not copied or paraphrased closely; the same content rule and pre-commit check apply.

### External sites (checked 2026-10-06)

Exercises are generated by Claude, never pulled from sites. Sites are used in two ways only:

| Site | Reachable from cloud session | Rights | Use in skills |
|---|---|---|---|
| Le Point du FLE (lepointdufle.net) | yes | © all rights reserved; mostly links to other sites, tagged A1–C2 per topic | **Link** per topic file, for extra practice in the browser |
| francaisfacile.com | yes | « Reproductions et traductions interdites sur tout support » | Link only, via Le Point du FLE |
| Bonjour de France | yes | © all rights reserved | Link only |
| Lawless French | yes | © all rights reserved; lessons free, tests need a paid account | Link for English explanations |
| Le Robert / Larousse online | yes | © (CGU) | **Live lookup** of one word's gender/spelling during correction, not stored |
| Reverso Context | yes | CGU forbid integrating the service into another service | Link only; the learner looks up expressions himself |
| TV5Monde Apprendre, RFI Français facile, FEI | blocked from the cloud session | free to use, © | the learner opens them; listening method unchanged |

### Precision layer (LanguageTool tested 2026-10-06)

LanguageTool 6.8 (open source, LGPL) runs locally from Maven Central jars; setup in `tools/languagetool/`.
Tested on a learner's placement forum post and a sample of spoken errors:

| | LanguageTool | Claude (placement corrections) |
|---|---|---|
| Agreement, determiners (le plupart, les moment, bon organisation, on se rencontrent) | caught | caught |
| Élision (que à, de apprendre), missing « ne » | caught | caught |
| Missing accents (regles, A → À) | caught | **missed** |
| Intended word (effaces → efficace, resoler → résoudre, mêmtemps → même temps) | flagged, **wrong fix** (effacés, refouler, mi-temps) | right |
| Gender from meaning (moments creatives → créatifs; locaux → commerces locaux) | flagged, **wrong fix** | right |
| « pas des exceptions » → pas d'exceptions, « besoin à », « demander mon employeur pour », « raison pourquoi » | **missed** | caught |
| Idioms (rendre une visite, chaque 3 mois, fait un plaisir de se revoir) | **missed** | caught |
| Noise | comma suggestions, numbers in letters | |

Conclusion: they are complementary. The writing and speaking skills run LanguageTool first, then Claude reviews every hit
(accept, fix the suggestion, or reject) and adds what it misses. Each correction is labelled **rule** (certain),
**usage** (likely) or **style** (optional). LanguageTool hits that Claude rejects are listed, so the learner can see the disagreement.

### Placement (`delf-placement`), the first one to build

- Four parts in the order we ran today: CE → PE → PO (entretien, interaction, point de vue) → CO.
- Resumable: progress is written to `sessions/DATE-placement.md` after each part, so it can span several sittings.
- Output: start scores in `scores.md`, first weak points, a recommended exam window and which skill the weekly rhythm should favour.
- Re-used later as a monthly checkpoint (same structure, new material) to update the "latest" column and the trend.

## 4. Keeping the book out

What the book gave us, and how each piece becomes original repo content:

| From the book | In the repo |
|---|---|
| Exam format table | `exam-format.md`, sourced from the public FEI page, not the book |
| Tips per épreuve | Rewritten as our own technique notes (e.g. "write vrai/faux before the justification"), drawn from what the learner's sessions show |
| Marking grids | Our own criteria in plain words per skill (task completion, coherence, vocabulary, grammar), no copied grid layout or wording |
| Practice texts, recordings, role plays | Generated fresh each session; RFI for real audio; one original sample set for the placement |
| Grammar and vocabulary pages | `grammar-checklist.md` and `themes.md` as our own lists |
| Page map (plan.md §7) | Dropped |

Guard rails: `AGENTS.md` (imported by `CLAUDE.md`) states the rule ("never name, quote, cite or reproduce commercial prep material"),
`.gitignore` excludes PDFs and audio, and `scripts/check-no-source.sh` runs as a pre-commit hook grepping for the title,
publisher and page-reference patterns. The PDF can still sit on your machine outside the repo for your own reading.

## 5. Public vs private

The skills and `reference/` are shareable. `learner/` holds your scores, errors and personal details. Two options:

- **Recommended:** one public repo for skills + reference, with `learner/` gitignored and kept in a separate small private repo (or just locally). Anyone can clone the coach and start with their own placement.
- **Simpler:** one private repo with everything. Fine if you never plan to share.

## 7. Frontmatter per skill

| Skill | Frontmatter |
|---|---|
| `delf-session` | `description` (daily session, "let's practise"), `argument-hint: [skill]` to override the day's focus |
| `delf-placement` | `disable-model-invocation: true` (only you start it; it resets start scores), `argument-hint: [resume]` |
| `delf-mock` | `disable-model-invocation: true` (90+ minutes, you choose when) |
| `delf-listening`, `-reading`, `-writing`, `-speaking` | `argument-hint: [theme]`, `arguments: [theme]` so `/delf-writing logement` works directly |
| `delf-review` | default; Claude may call it for the warm-up or when a known weak point comes up |
| `fle-grammar`, `fle-vocabulary` | default (you or Claude), `argument-hint: [topic]`, `arguments: [topic]` |

No skill uses `context: fork`: every session waits for your answers, and a forked skill runs without the conversation
and just returns a result. `allowed-tools` pre-approves only `Bash(python3 scripts/*)` for the state scripts.

## 8. Cross-check against the Claude Code skills docs

| Docs say | Design |
|---|---|
| Project skills live in `.claude/skills/<name>/SKILL.md`, committed to share | ✓ as laid out |
| Description decides auto-invocation; description + `when_to_use` truncated at 1,536 chars, key use case first | Each description opens with the exam part in both languages ("Production écrite / DELF B1 writing practice…") |
| SKILL.md under 500 lines, detail in supporting files linked from SKILL.md | ✓ `references/` per skill, each linked with when to read it |
| Invoked skill content **stays in context for the rest of the conversation** | Changed: router loads one specialist per session, one session per conversation, and the router itself stays ~40 lines |
| After compaction only the first ~5,000 tokens of each skill are kept | Keep every SKILL.md well under that; heavy material stays in `references/` |
| `disable-model-invocation: true` for things with side effects you control | Added for placement and mock (§7) |
| `$ARGUMENTS` / named `arguments`, `argument-hint` | Added (§7) |
| `!`command`` injects live context at load; a failing command aborts the whole skill | Router injects state via a script with `|| true` |
| `${CLAUDE_SKILL_DIR}` for a skill's own files, `${CLAUDE_PROJECT_DIR}` for repo files | Changed for portability (§8a): skill files are written `references/…`, repo files from the repository root. Only the router's injected command keeps `${CLAUDE_PROJECT_DIR}` |
| `context: fork` runs without conversation history | Not used: sessions are interactive (§7) |
| `allowed-tools` isn't gated by workspace trust, review in shared repos | Kept to one narrow script rule |
| Skills can be packaged as a plugin; `${CLAUDE_PLUGIN_DATA}` survives updates | Later option for sharing: plugin for the skills, learner state in plugin data. The plain repo stays simpler for now |
| Shell injection is disabled in Cowork for skills synced from claude.ai | If you ever sync these to claude.ai, the router must also work by reading files when injection is off |

## 8a. Other assistants

The skills stay in `.claude/skills/` and keep the Claude Code extras, but nothing depends on them:

| Claude Code feature | What other assistants get |
|---|---|
| `CLAUDE.md` | `AGENTS.md` holds the rules; `CLAUDE.md` only imports it |
| `.claude/skills/` discovery | `.agents/skills` symlinks to it (Codex, Cursor, Copilot scan that path) |
| `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}` | plain relative paths, with the convention stated at the top of each skill |
| `$ARGUMENTS`, named `arguments` | each skill says what an unfilled placeholder means |
| `!`command`` injection in the router | the router tells the assistant to run `python3 scripts/today.py` itself |
| `disable-model-invocation`, `allowed-tools`, `argument-hint` | ignored where unknown; `AGENTS.md` restates the "only the learner starts placement and mock" rule |

## 9. Build order

1. Repo skeleton, `CLAUDE.md`, `reference/`, `learner/` migrated, check script.
2. `delf-placement`.
3. `delf-session` + `delf-review` (so daily sessions work end to end).
4. `fle-grammar` with the topics from the current weak points (négation, élision, accords, prepositions, narration tenses), then `fle-vocabulary` starting with faux amis.
5. `delf-writing` (weakest skill), then `delf-speaking`, `delf-listening`, `delf-reading`.
6. `delf-mock` for Phase 3.
