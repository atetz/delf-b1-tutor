# Correction procedure and format

Shared by writing, speaking (on the transcript of what was said), the placement and the mock.

## 1. LanguageTool pass (when installed)

Installed means `tools/languagetool/lib/` and `tools/languagetool/target/classes/` exist (setup: `tools/languagetool/README.md`).

1. Save the learner's text, unchanged, to `learner/sessions/lt-input.txt`.
2. Run from the repo root:

   ```sh
   (cd tools/languagetool && JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF-8 java -Dstdout.encoding=UTF-8 \
     -cp "lib/*:target/classes" Check ../../learner/sessions/lt-input.txt)
   ```

3. Output is one line per issue: «text» -> [suggestions] | rule id | message.

Not installed or the run fails: say so in one line, continue without it, and take extra care with what Claude alone
tends to miss: accents (including on capitals: À, É), hyphens, and plural marks.

## 2. Review every hit

For each LanguageTool line decide:
- **keep:** the hit and its suggestion are right.
- **fix:** the hit is real but the suggestion is not the word the learner meant. Work out the intended word from the
  context (LanguageTool tends to offer the nearest spelling, not the nearest meaning).
- **reject:** not an error, or pure noise (optional commas, numbers written as digits). List rejected hits in one
  line at the end so the learner sees the disagreement.

## 3. Add what it misses

Read the text again yourself for what a rule checker rarely sees:
- wrong preposition after a verb or noun, « pas des » for « pas de », wrong relative pronoun;
- tense choice in a story, indicative for subjunctive;
- gender and agreement that depend on meaning;
- calques from Dutch or English, false friends, expressions that are not said;
- register slips and missing parts of the task.

Unsure of a word's gender or spelling: look that one word up (Le Robert or Larousse online) rather than guess.
Do not store the dictionary entry.

## 4. Label each correction

| Label | Meaning | Example |
|---|---|---|
| **rule** | Certain: grammar or spelling, one right answer | « parce que ils » → « parce qu'ils » |
| **usage** | Likely: a French speaker would not say it this way | « rendre une visite à » → « rendre visite à » |
| **style** | Optional: correct, but there is a clearer or more natural wording | repeated « très » → « vraiment », « particulièrement » |

Only **rule** and **usage** count for the mark and for weak points.

## 5. Present

Group by topic id from `reference/topics.md`, costliest group first. One line per correction:

```
morphosyntaxe/accords (3)
- rule: « une vrai problème » → « un vrai problème » (problème is masculine)
- rule: « les moment creatives » → « les moments créatifs »
lexique/expressions (1)
- usage: « chaque 3 mois » → « tous les trois mois »
LanguageTool hits rejected: comma before « mais » (optional), « 3 » in digits.
```

Then the full corrected version, changed words in bold, keeping the learner's ideas, order and level.
After five or more groups, stop detailing: list the remaining ones by name only. A correction the learner cannot
take in is not a correction.
