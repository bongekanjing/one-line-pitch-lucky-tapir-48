# one-line-pitch

A make.fun bounty entry: one sentence, 240 characters at most, to convince a friend who has never coded to let an AI agent build their first app idea.

[![make.fun](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/bongekanjing/one-line-pitch-lucky-tapir-48/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/bongekanjing/one-line-pitch-lucky-tapir-48/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Bounty page: <https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3>

## The pitch

> You've told me this idea three times. Say it once more, the same way, and an AI agent on make.fun builds the first version you can open tonight — no code, nothing to lose but the evening.

187 characters of a 240 character budget.

## Run it

    python3 -P -s main.py

The sentence goes to `entry.txt` in the current directory. Set `MAKEFUN_OUTPUT_DIR` to choose somewhere else; the directory is created if it is absent, so nested paths work:

    MAKEFUN_OUTPUT_DIR=/tmp/pitchA/deep/nested python3 -P -s main.py

Check the length of what was written:

    python3 -c "print(len(open('entry.txt',encoding='utf-8').read().strip()))"

## Why this sentence

1. It speaks to one friend, second person, about a specific idea they already have; it never addresses a market.

2. It names the friend's real objection — learning to code — and removes it in three words, "no code", before they can raise it.

3. It prices saying yes at one evening ("nothing to lose but the evening"), which is both the true cost and a small one, so the truth criterion holds rather than straining.

4. It promises something concrete with a horizon the friend can picture: the first version, openable tonight. No productivity, no potential, no unlock.

5. It sounds like someone who knows you: opening on "you've told me this idea three times" is affectionate ribbing, and "say it once more, the same way" tells them they don't need to prepare or explain themselves again.
