---
name: delf-session
description: Séance du jour / daily one-hour DELF B1 session. Picks today's focus from the weekday, the phase and the lowest score, runs the warm-up review, then hands over to one exam skill. Use when the learner says "session", "let's practise", "on commence", "what's today" or asks what to work on.
argument-hint: "[CO|CE|PE|PO|review]"
allowed-tools: Bash(python3 scripts/*) Bash(python3 ${CLAUDE_PROJECT_DIR}/scripts/*)
---

# Daily session router

This skill only decides and hands over. It holds no exercises, criteria or tips: those live in the specialist skills.

## Today's state

!`python3 ${CLAUDE_PROJECT_DIR}/scripts/today.py || true`

If the block above is empty or shows the command itself, read instead: `learner/profile.md`, `learner/scores.md`,
the rows of `learner/weak-points.md` whose Next review is today or earlier, and the last 5 rows of `learner/log.md`.

Focus requested by the learner: `$ARGUMENTS` (empty = choose).

## Procedure

1. **No scores yet** (or no `learner/` folder): stop here and ask the learner to type `/delf-placement`.
   Only they can start it.
2. **Pick the focus**, first rule that applies:
   - the learner's requested focus;
   - phase 3 (last weeks before the exam) on a Saturday: ask them to type `/delf-mock` instead;
   - Saturday: the paper with the lowest Latest score;
   - a paper not practised in the last 7 days of the log;
   - the weekday rhythm: Mon CO, Tue CE, Wed PE, Thu PO, Fri review, Sun rest (offer a short review only).
3. **Pick a theme** from `reference/themes.md` not used in the last three sessions, and up to three weak points
   to weave in: the due ones whose "Seen in" contains today's paper.
4. **Say the plan** in three lines (warm-up, main task, timing: 10 + 35 + 10 + 5 minutes) and start. Do not ask
   for approval of the plan; the learner can redirect.
5. **Warm-up, 10 min:** invoke `delf-review` on the due items. Nothing due: skip it and say so.
6. **Main task, 35 + 10 + 5 min:** invoke exactly one skill with a one-line brief, for example
   `delf-writing: theme logement, exam timing, weave in morphosyntaxe/accords and morphosyntaxe/negation`.
   CO → `delf-listening`, CE → `delf-reading`, PE → `delf-writing`, PO → `delf-speaking`.
   Friday: the main task is `delf-review` in full-session mode, which calls `fle-grammar` or `fle-vocabulary`.
7. **Check the bookkeeping:** today's row exists in `learner/log.md` and the score is in `learner/scores.md`.
   If the specialist skipped it, do it now following `reference/recording.md`.

One session = one conversation. Tomorrow, start a fresh conversation so today's skill material is not carried along.
