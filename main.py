#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply (132 characters) to /output/entry.txt.

The reply:
  I'm on vacation, so this reply was written by my out-of-office reply,
  which is also on vacation. Please hold while nobody helps you.

Why it works: the joke is recursion — the auto-reply itself has gone on
vacation and delegated to itself. The machine voice carries the joke
(an out-of-office reply talking about its own out-of-office reply),
the turn is surprising on first read, and it stays a clean, believable
one-line auto-reply with no beach / inbox / back-soon cliche.
"""

import os
from pathlib import Path

REPLY = (
    "I'm on vacation, so this reply was written by my out-of-office reply, "
    "which is also on vacation. Please hold while nobody helps you."
)


def main() -> None:
    assert 1 <= len(REPLY) <= 160, f"reply is {len(REPLY)} chars, must be 1-160"
    assert REPLY.strip(), "reply must not be only whitespace"
    assert "\n" not in REPLY, "reply must be a single line"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write exactly the reply, no trailing newline, so the byte count
    # stays 132 and the gate sees exactly the judged text.
    (out_dir / "entry.txt").write_text(REPLY, encoding="utf-8")
    print(f"Wrote {len(REPLY)}-character reply to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
