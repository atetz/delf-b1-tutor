---
name: delf-placement
description: Test de positionnement / DELF B1 placement test and monthly checkpoint. A shortened run of the four papers (reading, writing, speaking, listening) that sets the start scores, the first weak points and a recommended exam window. Resumable over several sittings.
argument-hint: "[resume|checkpoint]"
disable-model-invocation: true
---

# Placement and checkpoint

Mode: `$ARGUMENTS`
- empty: first placement. Fills the **Start** column and the first weak points.
- `resume`: continue an unfinished placement or checkpoint.
- `checkpoint`: monthly re-test with new material. Updates **Latest** and Trend, never Start.

## 1. Inputs

1. No `learner/` folder: `cp -r learner.example learner`.
2. Fill `learner/profile.md` with the learner if lines are empty (ask all the questions in one message). The
   entretien and the role plays use it.
3. Look for `learner/sessions/*-placement.md` with unfinished parts.
   - Found: say which parts are done and continue from the next one, whatever the mode.
   - Not found and Start scores already exist and mode is empty: say that a placement was already done and that
     `checkpoint` is the mode that keeps the start scores. Continue only if the learner confirms a reset.
4. Create `learner/sessions/YYYY-MM-DD-placement.md` with four headings (CE, PE, PO, CO), each marked `pending`.
5. Tell the learner the plan: four parts, about 2 hours in total, any part can wait for another day. No
   dictionary, no translator, no help: a flattering score makes a worse plan.

## 2. Generate the tasks

Read `${CLAUDE_SKILL_DIR}/references/tasks.md`.
- First placement: use the ready-made set in `${CLAUDE_SKILL_DIR}/references/sample-set.md`.
- Checkpoint, or the learner has already seen the sample set: generate new material with the same structure,
  on a theme not used in the last three sessions.

## 3. Run it, one part per turn, in this order

| Part | Time | What |
|---|---|---|
| CE | 20 min | one article, ten questions |
| PE | 45 min | one text, 160 words minimum |
| PO | 15 min | entretien, interaction, point of view (10 min preparation before the third) |
| CO | 15 min | two recordings heard twice, or the radio method |

- No hints, no corrections, no scores between parts: correction comes at the end, so one part does not colour the next.
- After each part, save the learner's raw answers under that part's heading in the placement file and mark it
  `done`. Then ask whether to continue now or stop here; `/delf-placement resume` picks it up.

## 4. Correct and score

When all four parts are done, read `${CLAUDE_SKILL_DIR}/references/scoring.md` and follow it: mark CE and CO, rate PE and PO per
criterion, estimate each paper out of 25, then derive the weak points, the phase, the weekly emphasis and the exam window.

Present, in this order: the four scores and total with the pass rule, the two strongest things, the weak points
table (at most ten rows, costliest first), the recommendation. Keep detailed corrections for PE and PO to the
five groups that cost most; the rest is listed by name.

## 5. Record

Follow `${CLAUDE_PROJECT_DIR}/reference/recording.md`, with these differences:
- `scores.md`: first placement writes **Start** and **Latest** (same value) and sets **Target** with the learner
  (default 15 per paper). Checkpoint writes Latest and Trend only.
- `weak-points.md`: up to ten rows on a first placement, spread over the next days: the five costliest get
  Next review tomorrow, the others the day after.
- `profile.md`: set « Current phase » and note the recommended exam window and the paper to favour.
- The placement file gets the scores, the corrections and the recommendation appended under the raw answers.
- `log.md`: one row, focus `placement` or `checkpoint`, score = total /100.

End by telling the learner that daily sessions now start with `/delf-session`, in a new conversation.
