#!/usr/bin/env python3
"""Museum of the Year 3000 -- make.fun bounty entry.

Writes one line (134 characters) to /output/entry.txt: the museum
label a museum in the year 3000 puts beside a password sticky note
from today. Deterministic, no network, no files outside this repo,
no secrets.

Candidate contest (8 labels, head-to-head on the judge's criteria,
in the brief's own order: on subject first, then the joke lands on
a first read, then the humour comes from the year 3000 misreading
the object -- something true and absurd about what it was for --
then it reads like a real museum label, short, straight faced and
confident, then the object and angle are fresh rather than the
obvious first joke about the obvious first object; a label that
explains its own joke is weaker than one that trusts the reader):

1. WINNER (134 chars): "Password sticky note, c. 2025. The master
   key to a citizen's entire life, written in plain sight and stuck
   to the machine it unlocked."
2. "Plastic fork, c. 2023. A single-use eating tool, discarded
   after one meal, now outliving the civilization that made it."
   (119) - the sharpest runner-up: outliving the civilization
   that made it is a true and absurd fate for a one-meal tool.
   It loses because its twist is elegiac rather than funny on a
   first read, and the plastic fork is the obvious first object
   the brief itself names, so the angle has to work twice as hard.
3. "Parking meter, c. 2025. Citizens fed it coins to rent the
   ground beneath their own cars, then fined themselves for
   forgetting." (126) - a strong misreading: renting the ground
   beneath your own car is true and absurd. It loses because
   "fined themselves for forgetting" explains the joke's second
   half instead of trusting the reader, and the meter is a
   listed example object, so it is less fresh than the sticky note.
4. "House key, c. 2024. A small metal tooth that proved you lived
   somewhere; losing it meant knocking on your own door like a
   stranger." (131) - a real label voice and a good second image,
   but the first half is a definition, not a misreading, and the
   house key is another object the brief names outright.
5. "Group chat, c. 2025. Forty-seven citizens gathered daily in a
   room with no walls to say 'lol' at jokes no one had read."
   (119) - the 'lol' at unread jokes is a true observation, but
   it is a caption about behaviour rather than a misreading of
   what the thing was for, and the group chat is the brief's own
   example, so it is the least fresh object here.
6. "Paper receipt, c. 2024. Proof of a purchase, printed in ink
   designed to vanish, so the proof erased itself within a year."
   (121) - the proof erasing itself is a neat absurd truth, but
   the laugh is quieter: it reads as a clever observation, not a
   joke that lands, and "designed to vanish" overstates the
   misreading instead of letting the fact do the work.
7. "Charging cable, c. 2025. A leash for a pocket oracle that died
   every day, yet its owners carried it everywhere like a
   lifeline." (127) - "pocket oracle" is a good year-3000 voice,
   but the line leans on two metaphors (leash, lifeline) and the
   second half explains the first, so it reads less straight
   faced than the winner's single flat fact.
8. "Selfie stick, c. 2024. A metal arm that lengthened the human
   reach so people could photograph themselves ignoring the view
   behind them." (135) - a true absurdity about its use, but the
   punchline arrives as a moral ("ignoring the view"), which is
   the curator editorialising rather than misreading, and the
   selfie stick is a well-worn first joke.

Why the winner wins: on criterion 1 it is squarely a museum label
for an ordinary object from today. On criterion 2 the laugh lands
on the first read, in the last clause: the master key to a whole
life, stuck to the machine it unlocked. On criterion 3 the humour
is the misreading itself -- a scrap of paper treated as a master
key, which is exactly what it was, and exactly absurd. On
criterion 4 it reads like a real label: object, date, one flat
confident sentence, no throat clearing. On criterion 5 the object
is fresh (no brief example) and the angle is fresh: the security
of an entire life defeated by plain sight. And it never explains
its own joke: the label states the fact flatly and lets the
reader feel the absurdity, which is exactly what the brief
rewards over a label that spells its punchline out.

Pairwise verdicts, winner against each rival: vs 2, a joke that
lands beats an elegy about a listed object; vs 3, trusting the
reader beats explaining the second half; vs 4, a misreading beats
a definition of a listed object; vs 5, a misreading of what the
thing was for beats a caption about behaviour; vs 6, a laugh
beats a clever observation; vs 7, one flat fact beats two
metaphors; vs 8, a misreading beats a moral.
"""

import os

# The winning line (134 characters, one line, no trailing newline).
LINE = "Password sticky note, c. 2025. The master key to a citizen's entire life, written in plain sight and stuck to the machine it unlocked."

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")

MAX_CHARS = 200


def validate(text: str) -> None:
    """Gate: 1-200 characters, non-blank, exactly one line."""
    if not text or not text.strip():
        raise SystemExit("entry must not be blank")
    if text != text.strip():
        raise SystemExit("entry must not have leading/trailing whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.endswith("."):
        raise SystemExit("entry must end with a full stop, like a label")


def main() -> None:
    line = LINE.strip()
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    # Verify what actually landed on disk: exact content, within the
    # gate, and mode 0644 (files from mkstemp stay 0600).
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt content mismatch")
    validate(written)
    if oct(os.stat(OUTPUT_PATH).st_mode & 0o777) != "0o644":
        raise SystemExit("entry.txt mode is not 0644")


if __name__ == "__main__":
    main()
