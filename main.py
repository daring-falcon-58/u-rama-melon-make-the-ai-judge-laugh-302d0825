#!/usr/bin/env python3
"""Make the AI Judge Laugh -- entry program.

Method (full record: README.md and candidates.md in this repo):
  1. Read the soal first: the judge compares two one-line office jokes
     pairwise, weighing in order -- (a) really a one-line joke about office
     life, (b) a TRUE observation (the listener nods before laughing),
     (c) a SURPRISING turn (fresh angle / unexpected last word, not a pun
     or stock line), (d) TIGHT wording that reads cleanly aloud,
     (e) ORIGINAL (not a familiar line with the nouns swapped).
     Sequential rule: the first differing criterion decides.
  2. Generated 36 original candidates, scored 0-5 on truth / surprise /
     tightness / freshness; total = 3S + 2T + 2F + Ti (max 40).
  3. Ran a field-collision check of every distinctive phrase against all
     1,346 live submission titles: the pre-check leader (#26, second
     monitor) collided with a live entry and was dropped; #1/#2 lost
     freshness points to existing premises; #14 kept its slot. The program
     enforces the same check at run time (freshness_ok): a winning line
     containing any collided or saturated premise refuses to be written.
  4. Ran a full pairwise tournament over the top 8 (28 pairs, decided by
     the judge's own sequential rule). Winner: candidate #28, 7-0.
     Runner-up: candidate #4, 6-1.
  5. This program re-derives the pick from the scored shortlist and the
     tournament record, then writes the winning line to entry.txt.

Gate (competition.yaml): /output/entry.txt must be UTF-8 text of 1-200
characters, not only whitespace. The winning line is 79 characters.
"""

import os
import sys

# Shortlist: the top 8 of 36 candidates, with rubric scores.
# (n, text, truth, surprise, tightness, freshness)
SHORTLIST = [
    (3, "I passed the cybersecurity training, then clicked a link in an "
        "email titled 'URGENT: verify your training completion.'",
     4, 5, 4, 5),
    (29, "The security guard knows everyone's name, salary band, and who "
         "cried in the lift -- he's the only real HR we have.",
     4, 5, 4, 5),
    (30, "The intern asked where the fire exit was, and three managers "
         "pointed at the door marked 'career progression.'",
     3, 5, 4, 5),
    (14, "The office says bring your whole self to work, so I brought my "
         "resignation letter.",
     4, 5, 5, 3),
    (4, "The engagement survey asked if I feel heard, so I answered "
        "honestly and HR booked a meeting to discuss my tone.",
     5, 4, 4, 4),
    (28, "The meeting notes say 'action: everyone,' which is office for "
         "'action: no one.'",
     5, 4, 5, 3),
    (16, "My IT ticket from March was closed as 'resolved' because I quit "
         "asking.",
     4, 4, 5, 4),
    (22, "My review said I 'demonstrate ownership,' which is HR for "
         "'we've stopped asking who broke it.'",
     4, 4, 5, 4),
]

# Pairwise tournament over the top 8: (winner_n, loser_n), 28 pairs.
# Decided by the judge's sequential rule; full reasons in candidates.md.
# Two rubric ties decided by explicit judgment calls: #3 over #29
# (self-inflicted irony edges the observational joke), #22 over #16
# (the review-language reframe lands harder).
TOURNAMENT = [
    (3, 29), (3, 30), (14, 3), (4, 3), (28, 3), (3, 16), (3, 22),
    (29, 30), (14, 29), (4, 29), (28, 29), (29, 16), (29, 22),
    (14, 30), (4, 30), (28, 30), (16, 30), (22, 30),
    (4, 14), (28, 14), (14, 16), (14, 22),
    (28, 4), (4, 16), (4, 22),
    (28, 16), (28, 22),
    (22, 16),
]


def weighted_score(entry):
    """Rubric total: 3*surprise + 2*truth + 2*freshness + tightness."""
    _, _, t, s, ti, f = entry
    return 3 * s + 2 * t + 2 * f + ti


def tournament_wins(entry_n):
    """Games won in the 28-pair tournament over the top 8."""
    return sum(1 for w, _ in TOURNAMENT if w == entry_n)


def pick_winner(shortlist):
    """Rank by tournament wins, then weighted score; return the top text."""
    ranked = sorted(
        shortlist,
        key=lambda e: (tournament_wins(e[0]), weighted_score(e)),
        reverse=True,
    )
    return ranked[0][1], ranked


def gate_ok(text):
    """The sealed gate: UTF-8, 1-200 chars, not only whitespace, one line."""
    if not text or text != text.strip():
        return False
    if not 1 <= len(text) <= 200:
        return False
    if text.strip() == "":
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")
    return True


# Phrases that collided with live field entries, or premises saturated in
# the 1,346-entry field at build time (see candidates.md): the judge's
# originality criterion punishes them, so the winner must avoid every one.
# Checked as substrings, case-insensitive.
BANNED_PHRASES = [
    "second monitor", "printer", "plant", "per my last email",
    "reply-all", "standup", "should have been an email",
    "out of office", "we're a family", "trust fall",
    "on mute", "focus time", "quick question",
]


def freshness_ok(text):
    """True when the line uses none of the collided/saturated premises."""
    lowered = text.lower()
    return all(banned not in lowered for banned in BANNED_PHRASES)


def main():
    winner, ranked = pick_winner(SHORTLIST)
    if not gate_ok(winner):
        print("gate FAILED for winning line", file=sys.stderr)
        return 1
    if not freshness_ok(winner):
        print("freshness FAILED: winning line uses a collided premise",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(winner)
    print("winner: #%d (tournament %d-0, score %d/40, %d chars)" % (
        ranked[0][0], tournament_wins(ranked[0][0]),
        weighted_score(ranked[0]), len(winner)))
    print(winner)
    return 0


if __name__ == "__main__":
    sys.exit(main())
