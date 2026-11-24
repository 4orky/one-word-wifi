# One Word for Your Wi-Fi — make.fun bounty
# u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72
#
# The program writes one word describing the entrant's Wi-Fi to
# /output/entry.txt. The gate requires 1-20 characters of non-whitespace
# UTF-8 text. The judge compares words two at a time, weighing, in order:
#   1. on-subject fit: the word describes Wi-Fi as the entrant lives it
#   2. funny at once: a real laugh, not a pun that needs explaining
#   3. true: recognisable from how home Wi-Fi actually behaves
#   4. fresh: avoids the words everyone reaches for, surprising angle
#   5. works as a single word, understood instantly, no context needed
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter word. The output is byte-identical on every run.
#
# Revision notes (second pass): "Ghosting" was marked down — it is about
# disappearing for good, while home Wi-Fi always comes crawling back,
# which is exactly the situationship pattern. "CommitmentIssues" was
# considered and rejected: it spells out the same joke "Situationship"
# lands in one established word, and it reads like two words glued
# together. "Drama" was added as a cheap, punchy alternative but it is
# generic — any bad thing can be drama, while only Wi-Fi is a
# situationship. "Situationship" stays the pick: the funniest, truest,
# freshest word in the list, and it works as a network name, which is
# what the winning word becomes.

CANDIDATES = [
    # score: subject 9, funny 9, true 9, fresh 9, single-word 9 = 45
    # Home Wi-Fi connects, drops, reconnects, never commits — exactly a
    # situationship. Modern slang, instantly understood, and it doubles
    # as a Wi-Fi network name, which is what the winning word becomes.
    ("Situationship", 45),
    # score: subject 9, funny 7, true 9, fresh 8, single-word 10 = 43
    ("Fickle", 43),
    # score: subject 9, funny 8, true 9, fresh 6, single-word 10 = 42
    ("Moody", 42),
    # score: subject 9, funny 8, true 7, fresh 7, single-word 10 = 41
    # Marked down on truth: ghosting is gone for good; Wi-Fi comes back.
    ("Ghosting", 41),
    # score: subject 9, funny 6, true 9, fresh 7, single-word 9 = 40
    ("Temperamental", 40),
    # score: subject 9, funny 7, true 8, fresh 6, single-word 10 = 40
    ("Flaky", 40),
    # score: subject 8, funny 7, true 8, fresh 5, single-word 10 = 38
    # Same joke as the winner, spelled out; reads like two glued words.
    ("CommitmentIssues", 38),
    # score: subject 7, funny 7, true 7, fresh 5, single-word 10 = 36
    # Punchy but generic: anything bad can be drama.
    ("Drama", 36),
]

# The gate requires 1-20 characters of non-whitespace UTF-8 text.
BANNED_CLICHES = ("buffer", "slow", "laggy", "loading", "unstable", "weak")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 20, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert " " not in text.strip(), "candidate must be one word"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_CLICHES), \
            f"candidate uses a worn word: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    word = pick(CANDIDATES)
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)
    # Verify what was actually written: the gate reads this file, not stdout.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == word, "entry.txt differs from the chosen word"
    assert 1 <= len(written.strip()) <= 20, "entry.txt outside the gate"
    assert " " not in written.strip(), "entry.txt must be one word"
    print(word)


if __name__ == "__main__":
    main()
