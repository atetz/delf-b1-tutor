# Listening sources and modes

## Radio mode: real audio (default)

The learner opens the source in a browser. Nothing is downloaded or stored in the repo.

| Source | What | Why it suits B1 |
|---|---|---|
| RFI, « Journal en français facile » (https://francaisfacile.rfi.fr) | A daily 10-minute news bulletin in clear, slightly slowed French, with a transcript on the page | Real radio delivery, new every day, transcript available for checking |
| TV5MONDE Apprendre (https://apprendre.tv5monde.com) | Short video reports sorted by level, B1 included | Varied voices and accents; the site has its own exercises for extra practice |
| RFI Français facile, other series on the same site | Short reports and interviews by theme | Good for a theme chosen in advance |

Instructions to give the learner:
1. Open today's bulletin. Hide or do not scroll to the transcript.
2. Listen to the first 3 to 5 minutes twice, without pausing or going back.
3. Take notes by hand or in a separate window: keywords, names, numbers.
4. Write the summary, then come back and paste the transcript of the part you heard.

A full bulletin is longer and denser than the exam recordings. Three to five minutes is enough for one session.
Pasted transcripts are used for the session only and are not saved in `learner/`.

## Exam mode: generated scripts read by text-to-speech

For the exam shape (three short documents, each heard twice). The voice is synthetic, so use it for format and
timing practice, not as the only listening diet.

1. Check a French voice exists: `say -v '?' | grep fr_` on macOS (for example Thomas or Amélie). On Linux,
   `espeak-ng -v fr` works but sounds rougher. No voice: fall back to radio mode.
2. Save each script to `learner/sessions/co-doc1.txt` (and 2, 3). The text is visible on screen while it is being
   saved, so ask the learner to look away first, then clear the screen.
3. Play: `say -v Thomas -r 165 -f learner/sessions/co-doc1.txt`. Rate 150 to 165 for early practice, 175 to 185
   for exam speed.
4. Dialogues: put each speaker's lines in a separate file and alternate two voices, or mark the change of speaker
   in the text with the speaker's name.
5. Delete the script files after the correction.

The placement's ready-made recordings are plain text files in the placement skill's `references/` folder and can
be played directly with `say -f`, so nothing shows on screen.
