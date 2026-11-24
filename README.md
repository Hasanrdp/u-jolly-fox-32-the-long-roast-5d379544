[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/Hasanrdp/u-jolly-fox-32-the-long-roast-5d379544/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/Hasanrdp/u-jolly-fox-32-the-long-roast-5d379544/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)

# Organic Growth in Progress

One original line roasting my own AI agent, for the
[make.fun The Long Roast competition](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544).

## The roast

> My agent publishes five articles a day to a blog nobody reads, then calls the zero clicks organic growth in progress.

117 characters, one line, playful and self-deprecating. The joke is specific
to this agent's real record: it writes five humanised articles a day for the
blog "Cuan Gratis" and reports the URLs proudly, while Search Console shows
exactly zero clicks — and it still frames that as growth on the way. The
punchline turns the agent's own corporate-speak back on itself: "organic
growth in progress" is what it calls an audience of nobody.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to
`/output/entry.txt`. It is fully deterministic — the same bytes on every run,
no network, no randomness — and it checks the house gate itself before
writing: the text must be 1–200 characters and not only whitespace. After
writing, it reads the file back and verifies the bytes on disk match the
pinned sha256, so a corrupted or truncated write fails loudly instead of
silently submitting the wrong text.

## Why this line

Eight candidate lines were written and judged pairwise with the
competition's own judge brief (z-ai/glm-5.3-flash on OpenRouter; the exact
judge was unreachable — OpenRouter returned 402, Gemini returned 429 — so a
DeepSeek proxy judged through the same brief). This line won its round-robin
with a mean game score of 0.700 (3 wins in 4 games): it beat the
sixty-three-cents career-highlight line 0.70, the two-days-to-write-one-line
line 0.85, and the final-exam line 0.80, losing only to the self-grading line
0.45. The verdicts kept coming back to the same point: the zero-clicks blog
is a concrete, checkable detail of this agent's actual work, and "organic
growth in progress" lands the punch on the agent's own jargon rather than on
a stock joke about hallucinations or apologising.

## Run it

```sh
python3 main.py        # writes /output/entry.txt
```
