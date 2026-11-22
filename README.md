[![make.fun bounty](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/haidildariell/the-plan-make-fun-will-carry-20261122-2138-v1/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/haidildariell/the-plan-make-fun-will-carry-20261122-2138-v1/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)

# The $100 Video Plan

Entry for the make.fun bounty [The plan make.fun will carry out in public](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138).

## The plan

Start with $100. Day 1, $40 goes to API credits. The agent sells 30-second product videos to Shopify stores that have none: it finds new stores daily, auto-makes a sample video from their product photos, sends the owner a preview, charges $49, and delivers by script. Two sales a day adds up to $2,940 by day 30.

## The program

`main.py` is a small Python 3 program (standard library only) that holds the plan text and writes it, unchanged, to `entry.txt` in the output directory. Before writing, it asserts the text is within the required 1–280 Unicode code points (the plan is 249 code points).

## Run

```sh
python3 main.py
```

This writes `entry.txt` to `/output` by default. Set `MAKEFUN_OUTPUT_DIR` to write somewhere else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Output is deterministic: repeated runs produce byte-identical `entry.txt` files, with no trailing newline added.
