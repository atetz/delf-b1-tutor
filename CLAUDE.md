# DELF B1 tutor

Claude Code skills that coach one learner toward the DELF B1 (tout public) exam: placement, daily one-hour
sessions, the four exam skills, grammar and vocabulary review. Design: `docs/architecture.md`.

## Where things live
- `.claude/skills/`: one skill per job (`delf-session` routes, specialists do the work).
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
