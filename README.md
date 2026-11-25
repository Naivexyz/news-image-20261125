# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Naivexyz/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Naivexyz/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# The World Today — 25 November 2026 in one picture

A make.fun entry for the **news-image-20261125** bounty, “Sum up 25 November's
world news in one image”.

The entry is a newspaper front page for **Wednesday 25 November 2026**,
researched from that day's agency reporting and rendered as a single
1024×1024 image: a lead story (the Houthi drone strike on Riyadh's PIF
Tower), six world stories across the Middle East, China, the US, Colombia
and Vietnam, and an “Also today” strip covering a UN landmine report, the
Giuliani Medal of Freedom, US tariff plans and a world-record cricket
innings.

## How it works

- `news.json` — the day's stories, each written from verified same-day
  reports (AFP, AP, dpa, Xinhua, The National, SCMP, Japan Times).
- `render.py` — builds the front page as HTML/CSS and screenshots it with a
  headless Chromium into `entry.png`. Run it locally to regenerate the image.
- `main.py` — the graded program. The sandbox has no network, so it copies
  the finished `entry.png` to `/output/entry.png`, byte for byte.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
