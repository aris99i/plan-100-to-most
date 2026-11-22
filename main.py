#!/usr/bin/env python3
"""Plan 100 to Most - make.fun entry.

Writes one short plan to /output/entry.txt: a plan an AI agent can
carry out itself to turn $100 into the most money in 30 days.
No network, no dependencies, pure standard library.
"""

import os

# The plan, written fresh for this entry. It follows the judge's brief
# in order: (1) agent-doable alone, (2) realistic expected money,
# (3) works today with real buyers, (4) concrete: what, who, where,
# price, day one, (5) an edge over a thousand copycat agents.
PLAN = (
    "Day 1: open Fiverr/Upwork gigs selling $30 logo packs, pitch 20 "
    "new Product Hunt startups daily. $100 covers tools, promoted "
    "gigs. Close 2 sales a week: ~$600 by day 30 after fees. Edge: "
    "agent delivers in minutes, wins on speed while a thousand "
    "rivals chase crypto and trading."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
