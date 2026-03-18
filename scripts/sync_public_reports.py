#!/usr/bin/env python3
import csv
import json
import os
import re
import sys
from datetime import datetime, timezone
from urllib.parse import quote
from urllib.request import Request, urlopen

H1_CSV_URL = "https://raw.githubusercontent.com/reddelexc/hackerone-reports/master/data.csv"
BUGCROWD_ENGAGEMENTS_URL = "https://bugcrowd.com/engagements.json"
UA = "neo-public-reports-sync/1.0"


def fetch_json(url: str):
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch_text(url: str):
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:80] or "report"


def sync_hackerone(limit=500):
    raw = fetch_text(H1_CSV_URL)
    rows = list(csv.DictReader(raw.splitlines()))
    out = []
    for row in rows[:limit]:
        link = (row.get("link") or "").strip()
        if link and not link.startswith("http"):
            link = "https://" + link
        out.append(
            {
                "platform": "hackerone",
                "program": (row.get("program") or "").strip(),
                "title": (row.get("title") or "").strip(),
                "url": link,
                "upvotes": int(float(row.get("upvotes") or 0)),
                "bounty": float(row.get("bounty") or 0),
                "vuln_type": (row.get("vuln_type") or "").strip(),
                "source": "reddelexc/hackerone-reports:data.csv",
            }
        )
    return out


def sync_bugcrowd(max_engagements=120, per_engagement_pages=2):
    engagements = fetch_json(BUGCROWD_ENGAGEMENTS_URL).get("engagements", [])[:max_engagements]
    out = []
    for e in engagements:
        brief = e.get("briefUrl") or ""
        handle = brief.rsplit("/", 1)[-1].strip()
        if not handle:
            continue
        for page in range(1, per_engagement_pages + 1):
            u = f"https://bugcrowd.com/engagements/{quote(handle)}/crowdstream.json?page={page}&filter_by=disclosures"
            try:
                data = fetch_json(u)
            except Exception:
                break
            results = data.get("results") or []
            if not results:
                break
            for r in results:
                disclosure_url = r.get("disclosure_report_url") or ""
                if disclosure_url and disclosure_url.startswith("/"):
                    disclosure_url = "https://bugcrowd.com" + disclosure_url
                out.append(
                    {
                        "platform": "bugcrowd",
                        "program": r.get("engagement_name") or handle,
                        "title": r.get("title") or "(untitled)",
                        "url": disclosure_url,
                        "severity": r.get("priority"),
                        "researcher": r.get("researcher_username"),
                        "amount": r.get("amount"),
                        "target": r.get("target"),
                        "created_at": r.get("created_at"),
                        "disclosed_at": r.get("disclosed_at"),
                        "id": r.get("id"),
                        "source": "bugcrowd crowdstream public endpoint",
                    }
                )
    return out


def write_outputs(base_dir: str, h1: list, bc: list):
    now = datetime.now(timezone.utc)
    day = now.strftime("%Y-%m-%d")
    out_dir = os.path.join(base_dir, "data", day)
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "hackerone.json"), "w", encoding="utf-8") as f:
        json.dump(h1, f, indent=2, ensure_ascii=False)

    with open(os.path.join(out_dir, "bugcrowd.json"), "w", encoding="utf-8") as f:
        json.dump(bc, f, indent=2, ensure_ascii=False)

    # Markdown snapshots for easy reading in GitHub
    h1_md = ["# HackerOne Public Reports Snapshot", "", f"Generated: {now.isoformat()}", ""]
    for i, r in enumerate(h1[:200], 1):
        bounty = f"${r['bounty']:.2f}" if isinstance(r.get("bounty"), float) else "n/a"
        h1_md.append(f"{i}. [{r['title']}]({r['url']})")
        h1_md.append(f"   - Program: {r['program']} | Upvotes: {r['upvotes']} | Bounty: {bounty} | Type: {r['vuln_type']}")

    bc_md = ["# Bugcrowd Public Disclosures Snapshot", "", f"Generated: {now.isoformat()}", ""]
    for i, r in enumerate(bc[:300], 1):
        sev = r.get("severity")
        bc_md.append(f"{i}. [{r['title']}]({r['url'] or 'https://bugcrowd.com'})")
        bc_md.append(f"   - Program: {r['program']} | Severity: P{sev if sev is not None else '?'} | Researcher: {r.get('researcher') or 'hidden'} | Amount: {r.get('amount') or 'n/a'} | Disclosed: {r.get('disclosed_at') or 'n/a'}")

    with open(os.path.join(out_dir, "hackerone.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(h1_md) + "\n")

    with open(os.path.join(out_dir, "bugcrowd.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(bc_md) + "\n")

    latest = {
        "generated_at": now.isoformat(),
        "path": f"data/{day}",
        "counts": {"hackerone": len(h1), "bugcrowd": len(bc)},
    }
    with open(os.path.join(base_dir, "data", "latest.json"), "w", encoding="utf-8") as f:
        json.dump(latest, f, indent=2)

    return latest


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("Syncing HackerOne (public dataset mirror)...")
    h1 = sync_hackerone(limit=int(os.getenv("H1_LIMIT", "500")))
    print(f"  -> {len(h1)} records")

    print("Syncing Bugcrowd (public disclosures)...")
    bc = sync_bugcrowd(
        max_engagements=int(os.getenv("BUGCROWD_MAX_ENGAGEMENTS", "120")),
        per_engagement_pages=int(os.getenv("BUGCROWD_MAX_PAGES", "2")),
    )
    print(f"  -> {len(bc)} records")

    latest = write_outputs(base_dir, h1, bc)
    print("Done:")
    print(json.dumps(latest, indent=2))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        raise
