#!/usr/bin/env python3
"""Summarise a text file with your local model through Ollama.

This is Days 5-7 of ai-lab: the same pattern as chat_local.py, but instead
of chatting, the script reads a file, sends its text to the model once,
and prints a short summary. No internet, no API key.

Usage (from ~/Documents/code/ai-lab, with the .venv active):
    python experiments/001-file-summariser/summarise.py README.md
    python experiments/001-file-summariser/summarise.py notes.txt
    python experiments/001-file-summariser/summarise.py notes.txt --model qwen2.5:3b

Requires: pip install openai (already done on Days 3-4)
          Ollama running with the model pulled (ollama run llama3.2:3b)
"""

import argparse
import sys

BASE_URL = "http://localhost:11434/v1"
# Small local models have a limited context window, so long files are
# trimmed rather than sent whole. The summary says so when this happens.
MAX_CHARS = 6000


def make_client():
    # Same as chat_local.py: Ollama's OpenAI-compatible endpoint.
    # The api_key value is ignored by Ollama, but the library needs one.
    # Imported here (not at the top) so --help and file errors work
    # even before the package is installed.
    try:
        from openai import OpenAI
    except ImportError:
        print("The 'openai' package is missing. Run:  pip install openai")
        sys.exit(1)
    return OpenAI(base_url=BASE_URL, api_key="ollama")


def read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except FileNotFoundError:
        print(f"No such file: {path}")
        print("Check the path and try again.")
        sys.exit(1)
    except IsADirectoryError:
        print(f"That is a folder, not a file: {path}")
        sys.exit(1)


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Summarise a text file with your local model.")
    ap.add_argument("file", help="Path to a .txt or .md file to summarise")
    ap.add_argument("--model", default="llama3.2:3b",
                    help="Ollama model name (default: llama3.2:3b)")
    args = ap.parse_args()

    text = read_file(args.file)
    if not text.strip():
        print(f"{args.file} is empty — nothing to summarise.")
        sys.exit(1)

    truncated = len(text) > MAX_CHARS
    if truncated:
        text = text[:MAX_CHARS]

    client = make_client()

    # Smoke test, same as chat_local.py: fail fast with a helpful message.
    try:
        models = [m.id for m in client.models.list().data]
    except Exception:
        print("Can't reach Ollama at", BASE_URL)
        print("Is Ollama running? Try:  ollama run", args.model)
        sys.exit(1)
    if args.model not in models:
        print(f"Model '{args.model}' isn't pulled yet. Run:")
        print(f"    ollama run {args.model}")
        sys.exit(1)

    prompt = (
        "Summarise the document below in 5 short bullet points, "
        "then list any key names, dates, or numbers it mentions.\n\n"
        f"Document:\n{text}"
    )
    try:
        resp = client.chat.completions.create(
            model=args.model,
            messages=[
                {"role": "system",
                 "content": "You summarise documents briefly and plainly."},
                {"role": "user", "content": prompt},
            ],
        )
    except Exception as e:
        print(f"[error] {e}")
        sys.exit(1)

    print(f"Summary of {args.file}:\n")
    print(resp.choices[0].message.content)
    if truncated:
        print(f"\n(Note: only the first {MAX_CHARS} characters were sent "
              "to the model, so this covers the start of the file.)")


if __name__ == "__main__":
    main()
