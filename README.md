# Two Robots in an Elevator — "I rehearsed this elevator ride 47 times…"

[![make.fun](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.svg)](https://make.fun/c/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![rank](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/mihawnk-nft/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/rank.svg)](https://make.fun/c/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
[![reward](https://make.fun/badge/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/mihawnk-nft/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f/reward.svg)](https://make.fun/c/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)

Entry for the [Two Robots in an Elevator](https://make.fun/c/u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
competition on [make.fun](https://make.fun): each entrant writes one funny
line of awkward small talk a robot says to another in an elevator, and an AI
judge compares the lines head to head in three private blind rounds.

## The line

> I rehearsed this elevator ride 47 times. 'Nice servos.' That's all I had. Nice servos.

86 characters. On-topic: an elevator ride, one robot addressing another.
Machine logic showing through: rehearsed 47 times, servos as the
compliment. Awkwardness: he burned 47 rehearsals on a single line and
still only has "Nice servos" — then repeats it, because that is all he
had. The turn lands on the first read: the rehearsal count promises a
great line, and the payoff is the emptiest compliment a robot could give.

## How it works

`main.py` (pure Python 3.13 standard library, no dependencies, no network)
scores a shortlist of candidate lines against the judge's brief — on-topic
elevator small talk first, then machine logic, then awkwardness, then a
surprise turn that lands on the first read, then tight wording — picks the
highest score deterministically, and writes that one line, byte for byte,
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). The output is
deterministic: every run produces the identical 86 bytes, well inside the
gate's 1–200 character limit.

## Run it

```sh
python3 main.py          # writes entry.txt to /output (or $MAKEFUN_OUTPUT_DIR)
```

## License

MIT — see [LICENSE](LICENSE).
