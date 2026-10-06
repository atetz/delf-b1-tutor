---
name: delf-mock
description: Examen blanc / full timed DELF B1 mock exam. Runs the four papers in exam order and timing with fresh material (listening, reading, writing, then speaking), corrects everything at the end and updates all four scores. About two and a half hours.
argument-hint: "[resume]"
disable-model-invocation: true
---

# Mock exam

Mode: `$ARGUMENTS` (`resume` continues an unfinished mock from `learner/sessions/*-mock.md`).

This skill holds no task material of its own. It borrows each paper's generators and criteria.

## 1. Inputs

1. Read `${CLAUDE_PROJECT_DIR}/reference/exam-format.md` for order, timings and the pass rule.
2. Pick four different themes from `${CLAUDE_PROJECT_DIR}/reference/themes.md`, none used in the last three sessions. A mock does
   **not** target the learner's weak points: it measures.
3. Create `learner/sessions/YYYY-MM-DD-mock.md` with the four papers marked `pending`.
4. Tell the learner the conditions: timer on their side, no dictionary, no questions about the content, phone away.
   The written papers run in one sitting (about 1 h 55). Speaking may follow after a break or on another day.

## 2. Generate the tasks

Generate each paper just before it runs, reading only that paper's task file:

| Order | Paper | Time | Generator |
|---|---|---|---|
| 1 | CO | about 25 min | `${CLAUDE_PROJECT_DIR}/.claude/skills/delf-listening/references/question-types.md`, exam mode in `sources.md` (three documents by text-to-speech). No text-to-speech: radio mode, and say the CO score is less comparable. |
| 2 | CE | 45 min | `${CLAUDE_PROJECT_DIR}/.claude/skills/delf-reading/references/task-types.md`: all three exercises |
| 3 | PE | 45 min | `${CLAUDE_PROJECT_DIR}/.claude/skills/delf-writing/references/genres.md`: one instruction |
| 4 | PO | 10 min preparation + about 15 min | the three files in `${CLAUDE_PROJECT_DIR}/.claude/skills/delf-speaking/references/` (entretien, interaction, point-de-vue) |

## 3. Run it

- Give each paper whole, announce its time limit, and wait. Ask the learner to say how long they actually took.
- Exam conditions: no hints, no rephrasing of instructions, no feedback or scores between papers.
- PO: the preparation for part 3 comes first, as in the exam; then parts 1, 2, 3 in a row, in the examiner role.
- After each paper, save the raw answers in the mock file and mark the paper `done`, so a break loses nothing.

## 4. Correct and score

After the last paper, using each paper's own marking file:
- CO: `delf-listening/references/scoring.md`; CE: `delf-reading/references/scoring.md`;
- PE: `delf-writing/references/correction-format.md` and `criteria.md`;
- PO: the same correction procedure and `delf-speaking/references/criteria.md`.

Present:
1. The four scores, the total /100 and the verdict against the pass rule (50/100, no paper under 5).
2. Timing: which papers ran over, and by how much.
3. Per paper: what cost most marks, in two lines. Full corrected version for PE.
4. Compared with the last mock or placement: what moved by more than two points.
5. The three priorities for the coming week's sessions.

## 5. Record

Follow `${CLAUDE_PROJECT_DIR}/reference/recording.md`: one log row (focus `mock`, score = total /100), all four Latest scores and
Trends, per-criterion rows for PE and PO, weak points (five new rows at most across the whole mock), and the
corrections appended to the mock file.
