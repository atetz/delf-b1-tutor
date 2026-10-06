# DELF B1 tutor

A set of Claude Code skills for preparing the DELF B1 (tout public) French exam with Claude:
a placement test, one-hour daily sessions, practice for the four papers, and spaced review of your own mistakes.

The design is in [`docs/architecture.md`](docs/architecture.md).

## Use

Open the repo in Claude Code and type:

| Command | What it does |
|---|---|
| `/delf-placement` | First: a two-hour diagnostic of the four papers (can be spread over several sittings). Later: `/delf-placement checkpoint` once a month. |
| `/delf-session` | The daily hour: warm-up review, one exam task, correction, logging. One conversation per day. |
| `/delf-listening`, `/delf-reading`, `/delf-writing`, `/delf-speaking` `[theme]` | One paper directly. |
| `/delf-review` | Spaced review of your own weak points and vocabulary. |
| `/fle-grammar [topic]`, `/fle-vocabulary [topic]` | A short lesson and fresh drills on one point or theme. |
| `/delf-mock` | A full timed mock exam. |

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
