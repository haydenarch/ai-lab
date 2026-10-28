# Day 1–2 setup (Mac)

Goal: Python runs, Git runs, `ai-lab` exists on GitHub, first commit done.

## 1. Check Python

```bash
python3 --version
```

Want **3.11 or newer**. If it's older or missing:
- Easiest: install from [python.org](https://www.python.org/downloads/) (macOS installer), **or**
- `brew install python` (if you use Homebrew)

Verify again after installing: `python3 --version`

## 2. Check Git

```bash
git --version
```

If missing: `xcode-select --install` (installs Apple's command line tools, includes Git).

Set your identity once:

```bash
git config --global user.name "Khun Phone Myat Thar"
git config --global user.email "your-email@example.com"
```

## 3. Create the repo

Unzip this starter pack where you want the lab to live (suggested: `~/code/ai-lab`), then:

```bash
cd ~/code/ai-lab
git init -b main
git add .
git commit -m "Day 1: ai-lab is live"
```

## 4. Push to GitHub

1. Go to github.com → **New repository** → name it `ai-lab`, **don't** tick "Add a README" (you already have one).
2. Back in the terminal:

```bash
git remote add origin git@github.com:<your-username>/ai-lab.git
git push -u origin main
```

(If SSH isn't set up on this Mac, GitHub will show you an HTTPS URL instead — use that.)

## 5. Virtual environment (from Day 3 onward)

Always work inside a venv so experiments don't pollute system Python:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

You'll see `(.venv)` at your prompt. (`.venv/` is already in `.gitignore`.)

Done — tick Days 1–2 in `14-day-checklist.md` and move on.
