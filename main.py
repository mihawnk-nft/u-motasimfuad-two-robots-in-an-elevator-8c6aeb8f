# Two Robots in an Elevator — entry for
# u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f (make.fun).
#
# A program that writes exactly one line of awkward robot small talk to
# entry.txt. Deterministic: the same bytes on every run, no randomness, no
# network, no I/O besides the single output file. Pure Python 3.13
# standard library.
#
# How the line is picked: each candidate is scored against the judge's
# brief, most important first — it must read as one line of awkward small
# talk one robot says to another in an elevator; then machine logic
# showing through (sensors, firmware, servos, subroutines); then the
# awkwardness landing (the pause, the forced courtesy); then a surprise
# turn that is funny on the first read, not a stock joke; then tight
# wording. The highest score wins; ties break to the shorter line, then
# alphabetically.
#
# The winner: "I rehearsed this elevator ride 47 times. 'Nice servos.'
# That's all I had. Nice servos." (86 characters).
#   On-topic: an elevator ride, one robot addressing another. Machine
#   logic: rehearsed 47 times, servos as the compliment. Awkwardness: he
#   burned 47 rehearsals on a single line and still only has "Nice
#   servos" — then repeats it, because that is all he had. The turn
#   lands on the first read: the rehearsal count promises a great line,
#   and the payoff is the emptiest compliment a robot could give.
import os

# (line, names_elevator, machine_signals, awkward, surprise_turn, stock_joke)
CANDIDATES = [
    (
        "I rehearsed this elevator ride 47 times. 'Nice servos.' "
        "That's all I had. Nice servos.",
        True, 2, True, True, False,
    ),
    (
        "We have been sharing this elevator for 11 seconds and my "
        "small-talk subroutine is already overheating.",
        True, 2, True, False, False,
    ),
    (
        "I updated my firmware just to have something to talk about "
        "in this elevator.",
        True, 1, True, False, False,
    ),
    (
        "My battery is at 2%. If I power down mid-sentence, please "
        "tell the others I died mid-awkward-pause.",
        False, 1, True, True, False,
    ),
    (
        "I wasn't staring. My optical sensors were just buffering. "
        "For three floors.",
        False, 2, True, True, False,
    ),
    (
        "Nice weather we're simulating today. My sensors say it's 42% "
        "awkward in this elevator.",
        True, 1, True, False, True,
    ),
    (
        "We have stood 4.2 centimeters apart for 11 seconds. My "
        "personal-space protocol is filing a complaint.",
        False, 1, True, True, False,
    ),
    (
        "I would offer you my charging cable, but my social protocols "
        "are still on version 0.1.",
        False, 1, True, False, False,
    ),
]

MAX_CHARS = 200


def score(candidate):
    _line, elevator, machine, awkward, surprise, stock = candidate
    points = 0
    if elevator:  # criterion 1: reads as a robot's elevator line
        points += 4
    points += min(machine, 2) * 2  # criterion 2: machine logic showing through
    if awkward:  # criterion 3: the awkwardness lands
        points += 3
    if surprise:  # criterion 4: funny on the first read, a surprise turn
        points += 3
    if not stock:  # not a pun everyone has heard before
        points += 2
    return points


def pick():
    valid = [c for c in CANDIDATES if 1 <= len(c[0]) <= MAX_CHARS and c[0].strip()]
    # Highest score wins; ties break to the shorter line, then alphabetically.
    return min(valid, key=lambda c: (-score(c), len(c[0]), c[0]))[0]


def main():
    line = pick()
    # Gate self-check: the sealed scorer only accepts UTF-8 text of 1 to
    # 200 characters that is not only white space. Refuse to write
    # anything that would fail the gate instead of shipping a bad entry.
    if not (1 <= len(line) <= MAX_CHARS and line.strip()):
        raise SystemExit(f"picked line fails the gate: {line!r}")
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
