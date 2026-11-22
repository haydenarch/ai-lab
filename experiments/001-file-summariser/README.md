# Experiment: 001-file-summariser

**Date:** 2026-11-22
**Phase:** Phase 0 — Foundations, Days 5–7

## What I tried

A script that reads a text file and asks the local llama3.2:3b model
(via Ollama) to summarise it in 5 bullet points, plus key names,
dates, and numbers. Same OpenAI-compatible call pattern as
`chat_local.py`, but one shot instead of a chat loop.

Run from the ai-lab folder, with the `.venv` active:

```bash
python experiments/001-file-summariser/summarise.py <file>
```

## What happened

Tested first on the ai-lab README.md — 5 bullets, mostly accurate
(one soft spot: it read "Oct 2026 → Mar 2027" as two deadlines
instead of a range). Then used it on a real document: the Florane
campaign ledger (Delayed-Release 60B Probiotic). The file is ~9.4 KB,
so the script trimmed it to the first 6,000 characters and said so.
The summary got the product, the mechanism, the audience (40–70+),
and all the numbers right (60B CFU, 150 mg, 30 capsules, $39, 88–92%
margin).

## What broke

The first run looked frozen — blank screen, no output. That was the
script waiting for the whole summary before printing anything, plus
Ollama loading the model after three weeks idle. Nothing was wrong;
it just needed a minute. Long files are trimmed at 6,000 characters
by design, so a summary only covers the start of a long document.

## What I learned

The model has no memory — the script sends the whole document each
time, just like chat_local.py sent the whole conversation history
each time. And: check a small model's summary against the original
before trusting it. This one added "increased energy" as a benefit
that isn't anywhere in the ledger — plausible-sounding, but invented.

## Next

Days 8–10: structured JSON output instead of prose.
