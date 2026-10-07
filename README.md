# DELF B1 tutor

A set of agent skills for preparing the DELF B1 (tout public) French exam with an AI assistant:
a placement test, one-hour daily sessions, practice for the four papers, and spaced review of your own mistakes.

The design is in [`docs/architecture.md`](docs/architecture.md).

## Use

Open the repo in your coding assistant and type:

| Command | What it does |
|---|---|
| `/delf-placement` | First: a two-hour diagnostic of the four papers (can be spread over several sittings). Later: `/delf-placement checkpoint` once a month. |
| `/delf-session` | The daily hour: warm-up review, one exam task, correction, logging. One conversation per day. |
| `/delf-listening`, `/delf-reading`, `/delf-writing`, `/delf-speaking` `[theme]` | One paper directly. |
| `/delf-review` | Spaced review of your own weak points and vocabulary. |
| `/delf-flashcards [date]` | Anki cards (CSV) from a session's errors and new words. |
| `/fle-grammar [topic]`, `/fle-vocabulary [topic]` | A short lesson and fresh drills on one point or theme. |
| `/delf-mock` | A full timed mock exam. |

Built and tested in Claude Code. The skills use the open Agent Skills format, and `AGENTS.md` holds the project
rules, so other assistants can run them too:

| Assistant | Finds the skills in | Start a skill with |
|---|---|---|
| Claude Code | `.claude/skills/` | `/delf-session` |
| Cursor | `.claude/skills/` or `.agents/skills/` | `/delf-session` |
| VS Code with Copilot | `.claude/skills/` or `.agents/skills/` | `/delf-session` |
| Codex | `.agents/skills/` | `$delf-session` |
| Anything else that reads `AGENTS.md` | by path, as `AGENTS.md` explains | "run the delf-session skill" |

`.agents/skills` is a symlink to `.claude/skills`. On Windows, clone with `git config core.symlinks true`
or copy the folder. Outside Claude Code, the argument placeholders and the pre-loaded daily state are not
filled in by the tool; `AGENTS.md` tells the assistant what to do instead.

## Setup

```sh
git clone <this repo> && cd delf-b1-tutor
git config core.hooksPath .githooks   # enables the check that keeps source material out
cp -r learner.example learner         # your personal state; gitignored
```

Optional: list titles, authors or publishers you never want committed in `.source-patterns`
(one regex per line, gitignored).

Optional grammar checker: see [`tools/languagetool`](tools/languagetool/README.md) (needs Java 17+).

## Privacy

`learner/` (your scores, mistakes and notes), PDFs, audio and `.source-patterns` are gitignored.
Keep `learner/` on your machine or in a separate private repository.

## Content

All texts, tasks, explanations and criteria are original. The exam format follows the public description by
France Éducation International. No commercial prep material or restricted examiner documents are included.

## License

MIT, see [LICENSE](LICENSE).
