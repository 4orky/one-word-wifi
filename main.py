#!/usr/bin/env python3
"""One word for my Wi-Fi.

The brief asks for a single word that names home Wi-Fi the way the
entrant actually lives with it, judged head to head on five things:
does it fit the subject, does it land a laugh at once, is it true to
real behaviour, is the angle fresh, and does it read as one word with
no explaining needed. The winning word also becomes the sponsor's
network name, so it has to sound like something you would actually
see in a Wi-Fi list.

My router and I have an understanding: it shows up, it vanishes, it
wanders back at 2 a.m. like nothing happened, and it will not commit
to staying. That is not a technical fault. That is a situationship.

So I drafted a dozen one-word candidates, graded each one 0-10 on the
five brief criteria, and let the numbers pick. The table below is the
whole method: no randomness, no network, no hidden input. The same
run always writes the same word.

Revision pass (second draft): "Breadcrumbing" first scored higher on
freshness than it deserved — it is a good word for a situationship,
but it describes the router's flirting, not the relationship itself,
so its subject-fit mark came down and it falls out of contention.
"Unreliable" lost a point on freshness for the same reason every
support ticket already uses it. "HotAndCold" reads as three words
glued together, so its single-word mark dropped. None of that moves
the winner: "Situationship" is still the only candidate that is the
joke, the truth, and a plausible network name all at once. A second
hardening in the same pass: every card now validates its own marks on
construction (all five criteria present, each 0-10), so a typo in the
table fails loudly instead of silently skewing the ranking.
"""

import re
from dataclasses import dataclass
from pathlib import Path

ENTRY_PATH = Path("/output/entry.txt")
GATE_MIN = 1
GATE_MAX = 20

# Words every entrant reaches for first. If a candidate leans on one
# of these, it is not fresh enough to win, whatever its other marks.
TIRED_WORDS = ("buffer", "slow", "lag", "load", "unstable", "weak", "drop")

# Criterion order matches the brief: fit, laugh, truth, freshness, one word.
CRITERIA = ("fit", "laugh", "truth", "fresh", "one_word")


@dataclass(frozen=True)
class WordCard:
    """One candidate word with a hand-graded mark per criterion."""

    word: str
    marks: dict
    why: str

    def __post_init__(self):
        missing = [c for c in CRITERIA if c not in self.marks]
        assert not missing, f"{self.word!r} is missing marks for: {missing}"
        for criterion, mark in self.marks.items():
            assert 0 <= mark <= 10, (
                f"{self.word!r} mark out of range: {criterion}={mark}"
            )

    @property
    def total(self) -> int:
        return sum(self.marks[c] for c in CRITERIA)


def build_shortlist() -> list:
    """Twelve original candidates, graded against the brief."""
    return [
        WordCard(
            "Situationship",
            {"fit": 10, "laugh": 9, "truth": 10, "fresh": 9, "one_word": 9},
            "Wi-Fi connects, drops, returns, never commits. The relationship "
            "is the joke, and it doubles as a network name.",
        ),
        WordCard(
            "Breadcrumbing",
            {"fit": 7, "laugh": 8, "truth": 8, "fresh": 9, "one_word": 8},
            "The router keeps tossing just enough signal to keep you hooked. "
            "Clever, but it names the flirting, not the relationship.",
        ),
        WordCard(
            "Fickle",
            {"fit": 9, "laugh": 6, "truth": 9, "fresh": 7, "one_word": 10},
            "Accurate and tidy, but it reads like a dictionary entry rather "
            "than a laugh.",
        ),
        WordCard(
            "Ghosting",
            {"fit": 8, "laugh": 8, "truth": 7, "fresh": 7, "one_word": 10},
            "Close, but ghosting means gone for good. Wi-Fi always comes "
            "crawling back, which is the whole situationship pattern.",
        ),
        WordCard(
            "Noncommittal",
            {"fit": 9, "laugh": 6, "truth": 9, "fresh": 7, "one_word": 8},
            "True to the behaviour, yet it sounds like a personality test "
            "result, not a punchline.",
        ),
        WordCard(
            "Moody",
            {"fit": 9, "laugh": 7, "truth": 9, "fresh": 5, "one_word": 10},
            "Every household has said it about the router. True, but the "
            "first word anyone reaches for.",
        ),
        WordCard(
            "Flaky",
            {"fit": 9, "laugh": 7, "truth": 8, "fresh": 6, "one_word": 10},
            "A solid everyday word for it. Loses on freshness: it could "
            "describe a friend, a plan, anything.",
        ),
        WordCard(
            "Temperamental",
            {"fit": 9, "laugh": 5, "truth": 9, "fresh": 6, "one_word": 9},
            "Precise and a little stiff. Nobody laughs at a word this long.",
        ),
        WordCard(
            "Tease",
            {"fit": 8, "laugh": 7, "truth": 7, "fresh": 7, "one_word": 10},
            "Short and punchy, but a tease wants your attention on purpose. "
            "The router is just unreliable.",
        ),
        WordCard(
            "Intermittent",
            {"fit": 9, "laugh": 3, "truth": 10, "fresh": 5, "one_word": 9},
            "The most accurate word here and the least funny. Reads like a "
            "status page.",
        ),
        WordCard(
            "Unreliable",
            {"fit": 9, "laugh": 4, "truth": 10, "fresh": 4, "one_word": 9},
            "True, and already written on a thousand support tickets. "
            "Freshness is gone.",
        ),
        WordCard(
            "HotAndCold",
            {"fit": 8, "laugh": 6, "truth": 8, "fresh": 6, "one_word": 5},
            "Captures the on-off rhythm, but it is three words in a "
            "trench coat. Fails the one-word test.",
        ),
    ]


def gate_ok(word: str) -> bool:
    """The sealed gate: 1-20 chars, not only whitespace, one word."""
    if not GATE_MIN <= len(word) <= GATE_MAX:
        return False
    if not word.strip():
        return False
    if not re.fullmatch(r"\S+", word):
        return False
    lowered = word.casefold()
    if any(tired in lowered for tired in TIRED_WORDS):
        return False
    return True


def choose_entry(shortlist: list) -> str:
    """Highest total wins; a tie goes to the shorter word."""
    ranked = sorted(
        shortlist,
        key=lambda card: (card.total, -len(card.word)),
        reverse=True,
    )
    for card in ranked:
        assert gate_ok(card.word), f"top candidate fails the gate: {card.word!r}"
    return ranked[0].word


def write_entry(word: str) -> None:
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(word, encoding="utf-8")
    reread = ENTRY_PATH.read_text(encoding="utf-8")
    assert reread == word, "entry file does not match the chosen word"
    assert gate_ok(reread), "entry file fails the gate on re-read"


if __name__ == "__main__":
    entry = choose_entry(build_shortlist())
    write_entry(entry)
    print(entry)
