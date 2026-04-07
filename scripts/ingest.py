"""Ingest blog posts and generate draft context files."""

from __future__ import annotations

import re
from datetime import date, datetime
from pathlib import Path

import yaml


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content.

    Returns (metadata_dict, body_text). If no frontmatter, returns ({}, full_content).
    """
    match = re.match(r"^---\n(.*?\n)---\n(.*)", content, re.DOTALL)
    if not match:
        return {}, content
    raw_meta = match.group(1)
    body = match.group(2)
    meta = yaml.safe_load(raw_meta) or {}
    # Normalize pubDate to string
    if "pubDate" in meta:
        val = meta["pubDate"]
        if isinstance(val, (date, datetime)):
            meta["pubDate"] = val.isoformat()[:10]
    return meta, body


def load_posts(
    source_dir: Path, cutoff_date: str | None = None
) -> list[dict]:
    """Load markdown posts from a directory.

    Returns list of {"path": Path, "meta": dict, "body": str} sorted by pubDate descending.
    If cutoff_date is provided (YYYY-MM-DD), only includes posts on or after that date.
    """
    posts = []
    for md_file in sorted(source_dir.glob("*.md")):
        content = md_file.read_text()
        meta, body = parse_frontmatter(content)
        if not meta:
            continue
        pub_date = meta.get("pubDate", "1970-01-01")
        if cutoff_date and pub_date < cutoff_date:
            continue
        posts.append({"path": md_file, "meta": meta, "body": body})
    posts.sort(key=lambda p: p["meta"].get("pubDate", ""), reverse=True)
    return posts


# Category definitions for grouping posts
CATEGORIES = {
    "writing-style": {
        "title": "Writing Style",
        "description": "Voice, tone, patterns, and vocabulary extracted from blog posts.",
        "instruction": "Review these excerpts for recurring voice patterns, sentence structures, and vocabulary choices.",
    },
    "opinions": {
        "title": "Opinions & Perspectives",
        "description": "Stances on topics drawn from blog posts.",
        "instruction": "Review these excerpts for strong opinions, recommendations, and perspectives.",
    },
    "expertise": {
        "title": "Expertise & Knowledge",
        "description": "Domains of deep knowledge evidenced by blog posts.",
        "instruction": "Review these posts to identify domains of expertise and depth of knowledge.",
    },
    "projects": {
        "title": "Projects",
        "description": "Projects mentioned or described in blog posts.",
        "instruction": "Review these posts for project descriptions, outcomes, and learnings.",
    },
}


def generate_drafts(posts: list[dict], output_dir: Path) -> list[Path]:
    """Generate draft context files from loaded posts.

    Each draft contains excerpts from all posts, grouped for manual curation.
    Returns list of created file paths.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    created = []

    for category_key, category_info in CATEGORIES.items():
        lines = [
            f"---",
            f"last_updated: {date.today().isoformat()}",
            f"source_refs:",
        ]
        for post in posts:
            lines.append(f"  - {post['path'].name}")
        lines.extend([
            f"---",
            f"",
            f"# {category_info['title']}",
            f"",
            f"> **Curation instruction:** {category_info['instruction']}",
            f"",
        ])

        for post in posts:
            title = post["meta"].get("title", post["path"].name)
            pub_date = post["meta"].get("pubDate", "unknown")
            categories = ", ".join(post["meta"].get("categories", []))
            # Take first 500 chars of body as excerpt
            excerpt = post["body"].strip()[:500]
            if len(post["body"].strip()) > 500:
                excerpt += "..."

            lines.extend([
                f"## From: {title} ({pub_date})",
                f"Categories: {categories}",
                f"",
                f"{excerpt}",
                f"",
                f"---",
                f"",
            ])

        out_path = output_dir / f"{category_key}.md"
        out_path.write_text("\n".join(lines))
        created.append(out_path)

    return created


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Ingest blog posts into draft context files")
    parser.add_argument("source_dir", type=Path, help="Directory containing markdown blog posts")
    parser.add_argument(
        "--cutoff",
        type=str,
        default=None,
        help="Only include posts on or after this date (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("drafts"),
        help="Output directory for draft files (default: drafts/)",
    )
    args = parser.parse_args()

    if not args.source_dir.is_dir():
        print(f"Error: {args.source_dir} is not a directory")
        raise SystemExit(1)

    posts = load_posts(args.source_dir, cutoff_date=args.cutoff)
    print(f"Loaded {len(posts)} posts from {args.source_dir}")

    created = generate_drafts(posts, args.output)
    print(f"Generated {len(created)} draft files in {args.output}/")
    for path in created:
        print(f"  - {path.name}")


if __name__ == "__main__":
    main()
