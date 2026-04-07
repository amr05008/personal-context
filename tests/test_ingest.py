import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from ingest import parse_frontmatter


def test_parse_frontmatter():
    content = """---
title: "Building products in the age of AI"
description: "A walkthrough of my presentation"
pubDate: 2025-11-28
categories: ["Presentations", "Product Management", "AI"]
heroImage: "/og-images/building-products-age-of-ai.png"
---

I recently had the opportunity to speak at NYU's Product Management Club.
"""
    meta, body = parse_frontmatter(content)
    assert meta["title"] == "Building products in the age of AI"
    assert meta["pubDate"] == "2025-11-28"
    assert "Product Management" in meta["categories"]
    assert body.strip().startswith("I recently had the opportunity")


def test_parse_frontmatter_no_frontmatter():
    content = "Just a plain markdown file with no frontmatter."
    meta, body = parse_frontmatter(content)
    assert meta == {}
    assert body == content


import tempfile
import os
from ingest import load_posts


def test_load_posts_filters_by_cutoff():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Recent post (should be included with cutoff 2024-01-01)
        Path(tmpdir, "recent.md").write_text(
            '---\ntitle: "Recent"\npubDate: 2025-06-15\ncategories: ["AI"]\n---\nRecent content.'
        )
        # Old post (should be excluded with cutoff 2024-01-01)
        Path(tmpdir, "old.md").write_text(
            '---\ntitle: "Old"\npubDate: 2020-01-01\ncategories: ["Tech"]\n---\nOld content.'
        )
        posts = load_posts(Path(tmpdir), cutoff_date="2024-01-01")
        assert len(posts) == 1
        assert posts[0]["meta"]["title"] == "Recent"


def test_load_posts_no_cutoff():
    with tempfile.TemporaryDirectory() as tmpdir:
        Path(tmpdir, "a.md").write_text(
            '---\ntitle: "A"\npubDate: 2020-01-01\ncategories: ["Tech"]\n---\nContent A.'
        )
        Path(tmpdir, "b.md").write_text(
            '---\ntitle: "B"\npubDate: 2025-01-01\ncategories: ["AI"]\n---\nContent B.'
        )
        posts = load_posts(Path(tmpdir))
        assert len(posts) == 2


from ingest import generate_drafts


def test_generate_drafts_creates_files():
    posts = [
        {
            "path": Path("fake/post.md"),
            "meta": {
                "title": "Building products in the age of AI",
                "pubDate": "2025-11-28",
                "categories": ["Presentations", "Product Management", "AI"],
            },
            "body": "I recently had the opportunity to speak at NYU.\n\nThe crux was to get out there and start building.",
        }
    ]
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = Path(tmpdir)
        generate_drafts(posts, output_dir)

        # Should create draft files
        files = list(output_dir.glob("*.md"))
        assert len(files) > 0

        # writing-style draft should exist and contain post excerpts
        writing_style = output_dir / "writing-style.md"
        assert writing_style.exists()
        content = writing_style.read_text()
        assert "Building products in the age of AI" in content
