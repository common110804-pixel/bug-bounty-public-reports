# Bug Bounty Public Reports Mirror (Phase 1)

This repo auto-syncs **public** bug bounty reports into date-stamped snapshots for easy reading on GitHub.

## Sources (phase 1)

- **HackerOne (public disclosures):** mirrored from `reddelexc/hackerone-reports` (`data.csv`)
  - Why: HackerOne no longer exposes a stable anonymous JSON feed for hacktivity.
- **Bugcrowd (public disclosures):** scraped from public engagement crowdstream endpoints.

## Output layout

- `data/YYYY-MM-DD/hackerone.md` — readable HackerOne snapshot
- `data/YYYY-MM-DD/hackerone.json` — structured HackerOne snapshot
- `data/YYYY-MM-DD/bugcrowd.md` — readable Bugcrowd snapshot
- `data/YYYY-MM-DD/bugcrowd.json` — structured Bugcrowd snapshot
- `data/latest.json` — pointer to latest snapshot + counts

## Run manually

```bash
python3 scripts/sync_public_reports.py
```

Optional limits:

```bash
H1_LIMIT=1000 BUGCROWD_MAX_ENGAGEMENTS=250 BUGCROWD_MAX_PAGES=3 python3 scripts/sync_public_reports.py
```

## Notes

- This phase intentionally avoids private APIs/tokens and only consumes public data.
- For private-program report ingestion, we can add API-token connectors + redaction in phase 2.
