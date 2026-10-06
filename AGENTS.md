# DELF B1 tutor

Agent skills that coach one learner toward the DELF B1 (tout public) exam: placement, daily one-hour
sessions, the four exam skills, grammar and vocabulary review. Design: `docs/architecture.md`.

## Where things live
- `.claude/skills/`: one skill per job (`delf-session` routes, specialists do the work). The same folder is
  reachable as `.agents/skills/` for tools that look there.
- `reference/`: shared, public-safe facts (exam format, spaced review, topic ids).
- `learner/`: the learner's personal state (profile, scores, weak points, log, sessions). Gitignored.
  Start from `learner.example/` if it does not exist: `cp -r learner.example learner`.

## Session shape (one hour)
10 min review of due weak points, 35 min one exam-style task, 10 min correction, 5 min logging in `learner/`.

## Content rule
Never name, quote, cite, paraphrase closely or reproduce commercial prep books, their exercises, answer keys or
recordings, or restricted examiner documents. Exam format comes from public France Éducation International
information; everything else (texts, tasks, criteria wording, explanations, examples) is written fresh.
Exercises are generated each session, never copied from websites. Linking to a website is fine.

## Corrections
Run `tools/languagetool` first when available, then review every hit (keep, fix, reject) and add what it misses.
Label each correction **rule**, **usage** or **style**.

## Running the skills in any assistant
The skills follow the Agent Skills format (`SKILL.md` with `name` and `description`). Where the tool does not
load them by itself, do it by hand:

- **Starting one.** The learner names a skill (`/delf-session`, `$delf-session`, "run delf-session") or asks for
  what its description covers. Read `.claude/skills/<name>/SKILL.md` and follow it.
- **"Invoke `<skill>`"** inside a skill means: read that skill's `SKILL.md` and continue in the same conversation.
- **Paths.** `references/…` is the skill's own folder; every other path starts at the repository root.
  Work from the repository root.
- **Arguments.** `$ARGUMENTS`, `$topic` and `$theme` are filled in by some tools. Left unfilled, take the value
  from the learner's message, or treat it as empty.
- **Lines starting with `!` and a command in backticks** are run by some tools when the skill loads. Shown as
  plain text, run the command yourself (`python3 scripts/today.py`).
- **`disable-model-invocation: true`** (`delf-placement`, `delf-mock`): start these only when the learner asks
  for them by name. They overwrite scores and take hours.
- Extra frontmatter fields (`argument-hint`, `arguments`, `allowed-tools`) are hints for tools that know them; ignore them otherwise.
