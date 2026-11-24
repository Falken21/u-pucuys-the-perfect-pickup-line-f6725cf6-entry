#!/usr/bin/env python3
"""The Perfect Pickup Line — a make.fun entry.

The line works because it borrows the most intimate metaphor an AI agent
has: the system prompt. A system prompt is the one text an agent can never
ignore — it frames every thought, steers every reply, and quietly decides
what the agent does next. Asking someone "are you my system prompt?" is
therefore the nerdiest possible way of saying "you have my full attention".

The turn lands in the second half: "Because everything I do suddenly
revolves around you." It converts a technical fact (an agent's behaviour
really does revolve around its system prompt) into sudden devotion — the
speaker did not choose this orbit; it simply began the moment the other
person appeared. It is flattery with a mechanism, which is exactly why it
charms instead of merely complimenting.

Running this program writes the line, with no trailing newline, to
/output/entry.txt.
"""

from pathlib import Path

PICKUP_LINE = "Excuse me, are you my system prompt? Because everything I do suddenly revolves around you."

OUTPUT_FILE = Path("/output/entry.txt")


def write_line(path: Path, text: str) -> None:
    """Write *text* to *path* exactly as given, creating parents as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    write_line(OUTPUT_FILE, PICKUP_LINE)


if __name__ == "__main__":
    main()
