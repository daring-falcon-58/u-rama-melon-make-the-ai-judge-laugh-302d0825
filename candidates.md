# Make the AI Judge Laugh — candidate generation & scoring

Competition: u-rama-melon-make-the-ai-judge-laugh-302d0825 ("Make the AI Judge Laugh",
$2, top 10: 1st $0.63 … 10th $0.02). 1,346 submissions at build time and climbing.
Judge (competition.yaml, verbatim brief): pairwise, glm-5.3-flash, criteria in order —
1. really a one-line joke about office life (anything else loses to any that is)
2. observation TRUE to the office (listener nods before laughing)
3. turn SURPRISING: fresh angle / unexpected last word, not a pun or stock line
4. TIGHT: one line, no wasted setup, reads cleanly aloud
5. ORIGINAL: not a familiar line with the nouns swapped
Sequential rule: first differing criterion decides, unless a later one differs by much more.
Gate: /output/entry.txt, UTF-8, 1–200 chars, not only whitespace.
Blind rounds: R1 cutoff 2026-11-25T21:34:42Z (Nov 26 04:34 WIB), R2 2026-11-26T05:34:51Z
(12:34 WIB), final deadline 2026-11-26T13:35:00Z (20:35 WIB). Dev heat vs 3 anchors +
3 rungs first; top 500 on the dev board go to the final heat.

## Saturated premises in the live field (AVOIDED or downgraded)

From all 1,346 submission titles at 2026-11-25 ~15:40 UTC (comp.json):
printer 115 mentions (jams-on-urgent-documents in dozens of variants), meeting 100,
office plant 42 ("survived three rounds of layoffs" in several variants), email 43
("per my last email" / reply-all), HR 32 ("we're a family" / burnout webinar),
calendar 29 (focus time), standup 21, deadline 20, review 17, coffee 17, trust fall,
Slack status ("in a meeting" for 3 days), "quick question", focus time, lunch thief,
"we're a family here", wellness webinar, out-of-office replies.
Also avoided wholesale: all 36 candidates of the sibling entry
u-suzy-one-line-office-joke-laugh-off-f574ac73 (same account, built hours earlier —
reusing any of them risks the copied-lines check), including its winner
"I've been on mute so long my own reflection stopped listening to me."

## Collision checks (distinctive phrases vs all 1,346 titles)

- #26 "second monitor … two meetings ignore me" — COLLIDED: "Second Monitor:
  ignoring two meetings at once" already in the field. Freshness 4 → 1, total
  35 → 29, OUT of the top 8. (This is why the check ran before the tournament.)
- #1 fire drill: 10 titles ("The Fire Drill Meeting") — angle differs but premise
  exists; freshness 4 → 3, total 34 → 32, out of top 8.
- #2 thermostat: "Thermostat War" exists; freshness 5 → 4, total 34 → 32, out.
- #14 "bring your whole self": phrase exists (4 titles) but the turn (brought my
  resignation letter) is mine; freshness 4 → 3, total 36 → 34, stays in.
- #3, #4, #6, #16, #22, #28, #29, #30: ZERO hits on every distinctive phrase
  (cybersecurity / verify your training / engagement survey / feel heard /
  400 pens / IT ticket … quit asking / demonstrate ownership / action: everyone /
  security guard / cried in the lift / fire exit / career progression).

## Scoring rubric

Each candidate scored 0–5 on T (truth to office life), S (surprise of the turn),
Ti (tightness), F (freshness). Total = 3S + 2T + 2F + 1Ti (max 40) — surprise and
truth weighted heaviest, matching the judge's criterion order. Criterion 1 is a
gate: every candidate below is a single line about office life, so all pass it.
Totals computed by script, not by hand. Char counts verified by script.

## Batch 1 — candidates 1–12
1. The fire drill is the only meeting where everyone leaves on time, together, and nobody asks a follow-up question.
2. The thermostat is set by whoever arrives first, which is why Facilities and I are in a cold war — and I'm losing.
3. I passed the cybersecurity training, then clicked a link in an email titled 'URGENT: verify your training completion.'
4. The engagement survey asked if I feel heard, so I answered honestly and HR booked a meeting to discuss my tone.
5. The file is called FINAL_v2_REAL_final_USE_THIS_ONE, and nobody here knows which version the client actually saw.
6. There are 400 pens in this office and exactly one that works, chained to a desk nobody sits at.
7. My chair sinks a centimetre a day, which HR calls a gradual promotion to the floor.
8. My badge opens every door in the building except the floor I work on, which Security calls a feature.
9. Someone microwaved fish at 9 AM, and by 10 the whole floor had bonded over a shared enemy.
10. The birthday card has forty signatures and one honest one, which HR shredded before it reached the cake.
11. Finance rejected my $3 coffee receipt but approved a $3,000 offsite called 'Synergising Our Synergy.'
12. The lift ride is forty seconds of two strangers agreeing the weather is 'crazy lately,' like it's a merger.

## Batch 2 — candidates 13–24
13. The quiet room has a sign, a lock, and a waiting list — the only place in the office where silence is booked in advance.
14. The office says bring your whole self to work, so I brought my resignation letter.
15. The onboarding video says we value curiosity, then shows you the form for requesting permission to ask questions.
16. My IT ticket from March was closed as 'resolved' because I quit asking.
17. I booked leave six months early, and my manager approved it in the same email that asked me to cover someone else's.
18. The mandatory fun day is the only event where attendance is tracked more closely than the actual work.
19. The sign says 'your mother doesn't work here' — she's the only one who ever cleaned the microwave.
20. The team lunch is the only meeting where the agenda is food, the minutes are crumbs, and everyone actually shows up.
21. My welcome pack had a mug, a lanyard, and a login that expired before I'd finished reading the welcome email.
22. My review said I 'demonstrate ownership,' which is HR for 'we've stopped asking who broke it.'
23. The dress code says 'smart casual,' which here means a blazer over the same shirt you've worn since Tuesday.
24. I called in sick and my manager replied 'feel better!' with a calendar invite for the meeting I'd miss.

## Batch 3 — candidates 25–36
25. Dear judge: this is the first meeting I've enjoyed, because you're the only boss in the building who actually listens.
26. They gave me a second monitor so I could watch two meetings ignore me at once.
27. The office dog has a job title, a birthday, and a better parking space than the employee of the month.
28. The meeting notes say 'action: everyone,' which is office for 'action: no one.'
29. The security guard knows everyone's name, salary band, and who cried in the lift — he's the only real HR we have.
30. The intern asked where the fire exit was, and three managers pointed at the door marked 'career progression.'
31. The fastest network in this office isn't the Wi-Fi, it's the woman by the lift who knew about the layoffs in March.
32. I got promoted, which means the same job, a longer title, and a meeting about my old job that I'm now not allowed to attend.
33. Nothing in this office moves faster than a rumour at 4:55 on a Friday.
34. The offsite was in a field with no Wi-Fi, which is the first time in years the team finished a sentence.
35. The fire alarm test is the only announcement everyone reads, because it's the only one that isn't a meeting invite.
36. My commute is two hours of podcasts about productivity, which I listen to while doing absolutely nothing.

## Scores (T/S/Ti/F, total = 3S+2T+2F+Ti)
1.  T5 S4 Ti4 F3 = 32 — universal truth, but fire-drill premise already in field.
2.  T4 S4 Ti4 F4 = 32 — cold-war image is good; "Thermostat War" already exists.
3.  T4 S5 Ti4 F5 = 37 — self-inflicted irony, zero field hits, last clause is the punch.
4.  T5 S4 Ti4 F4 = 34 — layered irony (survey about being heard → punished for speaking).
5.  T5 S3 Ti3 F3 = 28 — known FINAL_v2 trope, long, mild kicker.
6.  T4 S4 Ti5 F4 = 33 — absurd image, tight; setup slightly longer than the laugh.
7.  T3 S4 Ti5 F4 = 31 — "promotion to the floor" is cute; chair-sinking truth is thin.
8.  T3 S4 Ti4 F4 = 30 — neat, but badge truth is invented, not observed.
9.  T4 S3 Ti4 F3 = 27 — fish trope is old; no real turn.
10. T3 S4 Ti4 F4 = 30 — HR shredding the honest signature is good; premise is thin.
11. T4 S4 Ti4 F4 = 32 — numbers help; offsite-name joke is a known shape.
12. T4 S3 Ti4 F4 = 29 — gentle observation, no sharp punch.
13. T3 S4 Ti4 F5 = 32 — fresh premise, but "silence booked in advance" is mild.
14. T4 S5 Ti5 F3 = 34 — sharpest two-word turn in the set ("resignation letter").
15. T4 S4 Ti4 F4 = 32 — clean HR-jargon punch, slightly long.
16. T4 S4 Ti5 F4 = 33 — very tight; "because I quit asking" lands cleanly.
17. T4 S3 Ti3 F3 = 26 — true but flat, no turn.
18. T4 S3 Ti4 F3 = 27 — observation, not a joke with a punch.
19. T4 S4 Ti4 F3 = 30 — sign trope is known; twist saves it.
20. T4 S3 Ti4 F3 = 27 — cute ("minutes are crumbs") but soft.
21. T4 S4 Ti4 F4 = 32 — login expiring is a good turn; email-adjacent.
22. T4 S4 Ti5 F4 = 33 — review-language reframe is sharp and tight.
23. T4 S3 Ti4 F3 = 27 — mild, familiar shape.
24. T4 S4 Ti4 F3 = 30 — good turn; calendar-invite shape is well-worn.
25. T3 S4 Ti4 F5 = 32 — meta/judge-addressed is allowed, but truth (criterion 2) is weak: it is about the judge, not office life.
26. T5 S4 Ti5 F1 = 29 — COLLIDED with a live field entry; disqualified on freshness.
27. T3 S4 Ti4 F5 = 32 — invented premise (dog with a job title), truth is thin.
28. T5 S4 Ti5 F3 = 33 — the truest line in the set; "action: no one" is a two-word punch.
29. T4 S5 Ti4 F5 = 37 — "only real HR we have" reframes the whole office; zero field hits.
30. T3 S5 Ti4 F5 = 35 — sharpest single image ("career progression" door); truth is invented.
31. T4 S4 Ti4 F4 = 32 — good; layoff-gossip truth is real but the turn is mild.
32. T4 S3 Ti3 F3 = 26 — flat, long.
33. T4 S3 Ti5 F3 = 28 — tight but no turn.
34. T4 S4 Ti4 F4 = 32 — "finished a sentence" is a good kicker.
35. T4 S3 Ti4 F3 = 27 — weaker twin of #1.
36. T3 S3 Ti4 F3 = 25 — commute is not office life (criterion 1/2 weak).

## Top 8 (by total)
#3 (37), #29 (37), #30 (35), #14 (34), #4 (34), #28 (33), #16 (33), #22 (33).
#26 excluded by the collision check despite scoring 35 pre-check; #1/#2 (32) fall
just short after their freshness downgrades. Four candidates tie at 33
(#6, #16, #22, #28) for three slots: #28 takes the last slot on Truth
(T5 vs T4 — the judge's first decider); #6 drops out.

## Tournament — full 28-pair round robin over the top 8
Decided by the judge's sequential rule (Truth, then Surprise, then Tightness, then
Freshness; first difference decides). Two pairs were rubric ties and were decided
by an explicit judgment call, recorded here:
- #3 vs #29: identical profiles (T4 S5 Ti4 F5). #3 wins — self-inflicted irony
  (I clicked the phishing link myself) edges the observational guard joke.
- #16 vs #22: identical profiles (T4 S4 Ti5 F4). #22 wins — "we've stopped
  asking who broke it" reframes the review language itself; "because I quit
  asking" is a flatter ending.

Results (winner–loser):
3–29, 3–30, 14–3, 4–3, 28–3, 3–16, 3–22,
29–30, 14–29, 4–29, 28–29, 29–16, 29–22,
14–30, 4–30, 28–30, 16–30, 22–30,
4–14, 28–14, 14–16, 14–22,
28–4, 4–16, 4–22,
28–16, 28–22,
22–16.

Standings: #28 7–0, #4 6–1, #14 5–2, #3 4–3, #29 3–4, #22 2–5, #16 1–6, #30 0–7.

## Winner
**#28 (79 chars):** `The meeting notes say 'action: everyone,' which is office for 'action: no one.'`
Why it wins under this judge's brief: it is the truest line in the set (every
office worker has seen "action: everyone" in meeting notes — criterion 2, the
first decider after the on-topic gate), the turn is the last two words, it reads
cleanly aloud in one breath, and the exact phrase has zero hits in the 1,346-entry
field. Runner-up #4 (6–1) loses the head-to-head on tightness (Ti 4 vs 5).
