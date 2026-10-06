#!/usr/bin/env python3
"""Prints what the session router needs: date, weekday focus, profile, scores, due reviews, recent log.

Usage: python3 scripts/today.py [YYYY-MM-DD]   (the date argument is for testing)
Read-only. Never fails loudly: a missing or empty learner/ folder is reported in the output.
"""
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEARNER = ROOT / "learner"
RHYTHM = {
    0: "CO, listening (delf-listening)",
    1: "CE, reading (delf-reading)",
    2: "PE, writing (delf-writing)",
    3: "PO, speaking (delf-speaking)",
    4: "review: grammar and weak points (delf-review)",
    5: "mixed: lowest skill again, or a mock in phase 3",
    6: "rest day (optional catch-up or review)",
}


def rows(path):
    """Yields the rows of every markdown table in a file as dicts keyed by that table's header."""
    if not path.exists():
        return
    header = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = cells
        elif not all(re.fullmatch(r":?-+:?", c) for c in cells):
            yield dict(zip(header, cells))


def due(path, today):
    """Rows whose next review is today or earlier (or not set yet) and that are not retired."""
    out = []
    for row in rows(path):
        if row.get("Status", "").lower() == "retired":
            continue
        try:
            when = dt.date.fromisoformat(row.get("Next review", ""))
        except ValueError:
            when = today
        if when <= today:
            out.append(row)
    return out


def main():
    today = dt.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else dt.date.today()
    print(f"Date: {today.isoformat()} ({today.strftime('%A')})")
    print(f"Weekday focus: {RHYTHM[today.weekday()]}")

    if not LEARNER.is_dir():
        print("\nNo learner/ folder yet. Create it with: cp -r learner.example learner, then run /delf-placement.")
        return

    print("\nProfile:")
    profile = LEARNER / "profile.md"
    lines = profile.read_text(encoding="utf-8").splitlines() if profile.exists() else []
    for line in lines:
        if line.startswith("- "):
            print(line)

    print("\nScores (/25):")
    scores = [r for r in rows(LEARNER / "scores.md") if "Skill" in r and (r.get("Start") or r.get("Latest"))]
    if scores:
        for r in scores:
            print(f"- {r['Skill']}: start {r.get('Start') or '-'}, latest {r.get('Latest') or '-'}, "
                  f"target {r.get('Target') or '-'}, trend {r.get('Trend') or '-'}")
    else:
        print("- none yet: run /delf-placement first")

    criteria = [r for r in rows(LEARNER / "scores.md") if "Paper" in r]
    if criteria:
        print("\nLatest criterion ratings:")
        for r in criteria[-2:]:
            print("- " + ", ".join(f"{k}: {v}" for k, v in r.items() if v))

    weak = due(LEARNER / "weak-points.md", today)
    print(f"\nWeak points due ({len(weak)}):")
    for r in weak:
        print(f"- {r.get('Weak point', '?')} | seen in {r.get('Seen in', '?')} | fix with {r.get('Fix with', '?')} "
              f"| e.g. {r.get('Example of the error', '')} | interval {r.get('Interval') or '-'}")

    vocab = due(LEARNER / "vocabulary.md", today)
    print(f"\nVocabulary due ({len(vocab)}):")
    for r in vocab[:15]:
        print(f"- {r.get('Word / expression', '?')} = {r.get('Meaning', '')} | interval {r.get('Interval') or '-'}")
    if len(vocab) > 15:
        print(f"- ... and {len(vocab) - 15} more")

    log = list(rows(LEARNER / "log.md"))
    print("\nLast sessions:")
    for r in log[-5:]:
        print("- " + " | ".join(r.values()))
    if not log:
        print("- none yet")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # the router must still load when the state files are malformed
        print(f"today.py could not read the learner state ({exc}). Read the files in learner/ directly.")
