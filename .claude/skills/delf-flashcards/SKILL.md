---
name: delf-flashcards
description: Cartes mémoire / flashcards for Anki from a DELF B1 session. Turns the learner's own errors, weak points and new words from one session into a CSV file ready to import. Use for "flashcards", "cartes", "Anki", "make cards from this session", or at the end of a session when the learner wants something to revise on their phone.
argument-hint: "[date] [only … | without …]"
---

# Flashcards from a session

Paths: every path starts at the repository root.

Request: `$ARGUMENTS` (an unfilled placeholder starting with a dollar sign means: take it from the learner's message; empty = today's session, all groups).

## 1. Inputs

- **Session:** `learner/sessions/<date>.md` for the date asked, otherwise the latest one. When the session ran in
  this conversation, use the conversation too: it has the exact wrong answers.
- **State:** the rows of `learner/weak-points.md` and `learner/vocabulary.md` added or reset to interval 1 on that date.
- **Already made:** the Front column of every file in `learner/flashcards/`. Never make the same card twice.
- A filter in the request ("only grammar", "without the words from the text") removes whole groups in step 2.

No session note for that date: say so and stop. Do not invent cards from the topic files alone.

## 2. Choose the cards

Take only what the session showed the learner does not yet produce correctly. Groups, in this order:

| Group | Source | Tag |
|---|---|---|
| Vocabulary missed | words wrong in the warm-up or misused in an answer | `vocabulaire` |
| Words from the text | new words listed after a reading or listening task | `vocabulaire` |
| Spelling | misspelt words, including slips copied from a text | `orthographe` |
| Gender and agreement | nouns whose gender caused the error, irregular plurals | `accords` |
| Grammar patterns | one model sentence per rule missed | the topic part of its id in `reference/topics.md`, e.g. `negation`, `temps-du-recit` |

Limit: 20 cards per session, the costliest errors first. Something answered right gets no card.

## 3. Write each card

- **Direction:** the front is the prompt (English, or Dutch when the error came from Dutch), the back is the French
  to produce. No French-to-English recognition cards: the learner reads well and loses marks in production.
- **One fact per card.** Three words with the same ending can share a card when the ending is the point.
- **Nouns always with their article** (un, une, le, la), never bare.
- **Grammar cards** are a short sentence to translate, written fresh on the session's theme, with the rule in
  brackets after the answer in under ten words. Never the learner's own wrong sentence as the front, and never
  a wrong form anywhere on the card except as "never …" after the right one.
- **Contrast pairs** when the error was a confusion: two cards, one for each side (rendre visite à / visiter).
- Content rule of `AGENTS.md` applies: every sentence is written fresh.

## 4. Show, then save

1. Show the cards in the conversation as tables, one per group, so the learner can remove or change some.
   When they asked for the file directly, skip the wait and write it.
2. Write `learner/flashcards/<date>.csv` (append new cards if the file exists):

```
#separator:Semicolon
#html:false
#columns:Front;Back;Tags
#tags column:3
the meaning of a word;le sens d'un mot (no -e);delf vocabulaire
```

   - Tags: `delf` plus the group tag, separated by a space.
   - No semicolon inside a field: reword with a comma or a slash. No line breaks inside a field.
3. Tell the learner in three lines: the path and number of cards, how to import (Anki: File → Import, note type
   Basic; the header lines set the separator and the fields), and that words in `learner/vocabulary.md` also
   come back in the warm-up.

This skill writes nothing else: no log row, no score, no change to intervals. The cards are an extra way to
revise, the spaced review in `delf-review` stays the record.
