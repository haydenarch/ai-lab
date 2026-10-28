# 14-day checklist — Phase 0: Foundations

Tick as you go. Busy week? Shrink the session, don't skip the phase.

## Days 1–2: The lab exists

- [ ] Python 3.11+ runs (`python3 --version`)
- [ ] Git runs and identity is set
- [ ] `ai-lab` repo on GitHub, this starter pack committed and pushed
- [ ] You can open the repo on github.com and see the README

## Days 3–4: A model on your machine

- [ ] Ollama installed (ollama.com → Download for Mac), `ollama --version` works
- [ ] A small model pulled and chatting: `ollama run llama3.2:3b` (try Qwen too: `ollama run qwen2.5:3b`)
- [ ] From Python (inside `.venv`), chat with the local model via its OpenAI-compatible API at `http://localhost:11434/v1`

## Days 5–7: First real script

- [ ] `experiments/001-file-summariser/` exists with a README
- [ ] Script reads a text file and prints a summary using the local model
- [ ] Used it on a **real** document (class notes, shop FAQ, anything real)
- [ ] Committed and pushed

## Days 8–10: Make output usable

- [ ] Script returns **structured JSON** you can use in code (not just prose)
- [ ] One few-shot improvement: show the model 1–2 examples of good output, compare before/after
- [ ] Note what got better and what didn't (in the experiment README)

## Days 11–14: Spec your first automation

Pick ONE for Phase 1, then write a one-paragraph spec: **input → steps → output → success test**.

- [ ] Chosen: ICT prep helper / inbox-notes digest / shop caption helper
- [ ] Spec written (one paragraph, concrete)
- [ ] Phase 1 begins — the automation must run on the real task for 7 days

**Milestone 1 = that automation, used for a week, with a learning note.** That's the proof this direction is real.
