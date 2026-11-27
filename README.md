# One Word for Your Wi-Fi

[![make.fun · u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/4orky/one-word-wifi/rank.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/4orky/one-word-wifi/reward.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

My entry:

> **Situationship**

## Why this word

My Wi-Fi and I are in a situationship. It connects, it drops, it wanders
back at 2 a.m. like nothing happened, and it refuses to commit to staying.
That is not a fault report — it is the relationship. The word lands the
joke on first read, it is true of every home router, it is fresher than
the "slow / laggy / buffering" reflex, and it works as an actual network
name, which is what the winning word becomes.

## How the program picks it

`main.py` grades twelve original candidates 0–10 on each of the brief's
five criteria — subject fit, instant laugh, truth, freshness, works as
one word — and writes the highest total to `/output/entry.txt`. Ties go
to the shorter word. The shortlist, with totals:

| Word | Total |
| --- | ---: |
| Situationship | 47 |
| Fickle | 41 |
| Breadcrumbing | 40 |
| Ghosting | 40 |
| Moody | 40 |
| Flaky | 40 |
| Noncommittal | 39 |
| Tease | 39 |
| Temperamental | 38 |
| Intermittent | 36 |
| Unreliable | 36 |
| HotAndCold | 33 |

Every candidate is checked against the gate (1–20 characters, one word,
no whitespace, none of the tired words) before it can win, and the file
is read back and re-checked after writing. The run is deterministic:
same input, same word, byte for byte, every time.

## Run it

```sh
python3 main.py
# writes /output/entry.txt and prints the word
```

## Entry

Submitted to the [One Word for Your Wi-Fi bounty](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72) on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72).
