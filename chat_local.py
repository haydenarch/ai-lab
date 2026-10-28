#!/usr/bin/env python3
"""Chat with your local model through Ollama's OpenAI-compatible API.

Usage (inside your .venv, with Ollama running):
    python chat_local.py                 # interactive chat, llama3.2:3b
    python chat_local.py --model qwen2.5:3b
    python chat_local.py --once "Summarise this file for me"

Requires: pip install openai   (and Ollama running: ollama run llama3.2:3b)
"""

import argparse
import sys

try:
    from openai import OpenAI
except ImportError:
    print("The 'openai' package is missing. Run:  pip install openai")
    sys.exit(1)

BASE_URL = "http://localhost:11434/v1"


def make_client() -> OpenAI:
    # Ollama's OpenAI-compatible endpoint. The api_key value is ignored
    # by Ollama, but the client library requires *something* there.
    return OpenAI(base_url=BASE_URL, api_key="ollama")


def ask(client: OpenAI, model: str, messages: list[dict]) -> str:
    resp = client.chat.completions.create(model=model, messages=messages)
    return resp.choices[0].message.content


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="llama3.2:3b",
                    help="Ollama model name (default: llama3.2:3b)")
    ap.add_argument("--once", metavar="PROMPT",
                    help="Ask one question and exit instead of chatting")
    args = ap.parse_args()

    client = make_client()

    # Smoke test: fail fast with a helpful message if Ollama isn't up.
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

    if args.once:
        print(ask(client, args.model,
                  [{"role": "user", "content": args.once}]))
        return

    print(f"Chatting with {args.model} (local). Type 'quit' to stop.\n")
    history: list[dict] = [
        {"role": "system",
         "content": "You are a helpful assistant running locally on the user's Mac."}
    ]
    while True:
        try:
            user = input("you> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if user.lower() in {"quit", "exit"}:
            break
        if not user:
            continue
        history.append({"role": "user", "content": user})
        try:
            reply = ask(client, args.model, history)
        except Exception as e:  # model busy, connection dropped, etc.
            print(f"[error] {e}")
            history.pop()
            continue
        print("ai >", reply, "\n")
        history.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
