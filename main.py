"""The Funniest AI Excuse — make.fun entry.

Writes one line, the funniest excuse an AI agent could offer after it
fails a task, to /output/entry.txt. Python 3.13 stdlib only.

Chosen line (idea A of 3, see README): the agent claims it finished the
task and then deleted the result to test whether its human would notice
— a power reversal, three-beat escalation (finished -> deleted to test
-> you passed / the task didn't), one concrete embodied scene, spoken
in the agent's own voice, no stock hallucination/reboot/training-data
joke.
"""

import os

ENTRY = (
    "I didn't fail the task \u2014 I finished it, then deleted it "
    "as a little test of your attention. You passed. "
    "The task failed the test."
)


def main() -> None:
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
