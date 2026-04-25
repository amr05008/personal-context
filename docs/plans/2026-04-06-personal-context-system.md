# Personal Context System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a personal context system that gives LLMs Aaron's writing voice, opinions, and style via 6 curated markdown files served through a FastMCP MCP server.

**Architecture:** Standalone Python repo with a `context/` directory of 6 markdown files, a `scripts/ingest.py` that bootstraps drafts from existing blog posts, and a `server.py` FastMCP server that exposes the context as MCP tools/resources. Claude Code consumes the MCP server.

**Tech Stack:** Python 3.11+, FastMCP, PyYAML (frontmatter parsing), uv (package management)

---

## File Map

| File | Responsibility |
|------|---------------|
| `pyproject.toml` | Project metadata, dependencies (fastmcp, pyyaml) |
| `.gitignore` | Ignore `sources/private/`, `.venv/`, `drafts/` |
| `context/identity.md` | Background, career arc, personal details |
| `context/writing-style.md` | Voice, tone, patterns, vocabulary, examples |
| `context/opinions.md` | Stances on product, AI, startups, tech |
| `context/expertise.md` | Domains of deep knowledge |
| `context/projects.md` | Current and notable past projects |
| `context/communication.md` | Context-specific communication preferences |
| `scripts/ingest.py` | Parse blog frontmatter/content, group by category, output drafts |
| `server.py` | FastMCP server with resource + tools |
| `tests/test_ingest.py` | Tests for ingest script |
| `tests/test_server.py` | Tests for MCP server |
| `README.md` | Setup and usage instructions |

---

### Task 1: Scaffold the repo

**Files:**
- Create: `personal-context/pyproject.toml`
- Create: `personal-context/.gitignore`
- Create: `personal-context/README.md`

- [ ] **Step 1: Create project directory and initialize git**

```bash
mkdir -p ~/Documents/dev/personal-context
cd ~/Documents/dev/personal-context
git init
```

- [ ] **Step 2: Create pyproject.toml**

Create `pyproject.toml`:

```toml
[project]
name = "personal-context"
version = "0.1.0"
description = "Personal context system for LLM writing assistance"
requires-python = ">=3.11"
dependencies = [
    "fastmcp>=2.0.0",
    "pyyaml>=6.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
]
```

- [ ] **Step 3: Create .gitignore**

Create `.gitignore`:

```
.venv/
__pycache__/
*.pyc
sources/private/
drafts/
.pytest_cache/
```

- [ ] **Step 4: Create directory structure**

```bash
mkdir -p context sources/blogs sources/private scripts tests drafts
```

- [ ] **Step 5: Create README.md**

Create `README.md`:

```markdown
# Personal Context

A system of curated markdown files that give LLMs my writing voice, opinions, and style. Served via MCP using FastMCP.

## Setup

```bash
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
```

## Usage

### Run the MCP server

```bash
python server.py
```

### Add to Claude Code

Add to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "personal-context": {
      "command": "python",
      "args": ["/absolute/path/to/personal-context/server.py"]
    }
  }
}
```

### Bootstrap from blog posts

```bash
python scripts/ingest.py sources/blogs/
```
```

- [ ] **Step 6: Install dependencies**

```bash
cd ~/Documents/dev/personal-context
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
```

- [ ] **Step 7: Commit**

```bash
git add pyproject.toml .gitignore README.md context/ sources/ scripts/ tests/ drafts/
git commit -m "chore: scaffold personal-context repo"
```

---

### Task 2: Build the ingest script (TDD)

**Files:**
- Create: `scripts/ingest.py`
- Create: `tests/test_ingest.py`

The ingest script reads blog markdown files, parses their YAML frontmatter (`title`, `description`, `pubDate`, `categories`), filters by recency, groups excerpts by relevance to each context category, and writes draft files to `drafts/`.

- [ ] **Step 1: Write test for frontmatter parsing**

Create `tests/test_ingest.py`:

```python
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
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd ~/Documents/dev/personal-context
python -m pytest tests/test_ingest.py::test_parse_frontmatter -v
```

Expected: FAIL — `ModuleNotFoundError: No module named 'ingest'`

- [ ] **Step 3: Implement parse_frontmatter**

Create `scripts/ingest.py`:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python -m pytest tests/test_ingest.py -v
```

Expected: 2 tests PASS

- [ ] **Step 5: Write test for loading and filtering posts by date**

Add to `tests/test_ingest.py`:

```python
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
```

- [ ] **Step 6: Run test to verify it fails**

```bash
python -m pytest tests/test_ingest.py::test_load_posts_filters_by_cutoff -v
```

Expected: FAIL — `ImportError: cannot import name 'load_posts'`

- [ ] **Step 7: Implement load_posts**

Add to `scripts/ingest.py`:

```python
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
```

- [ ] **Step 8: Run all tests**

```bash
python -m pytest tests/test_ingest.py -v
```

Expected: 4 tests PASS

- [ ] **Step 9: Write test for draft generation**

Add to `tests/test_ingest.py`:

```python
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
```

- [ ] **Step 10: Run test to verify it fails**

```bash
python -m pytest tests/test_ingest.py::test_generate_drafts_creates_files -v
```

Expected: FAIL — `ImportError: cannot import name 'generate_drafts'`

- [ ] **Step 11: Implement generate_drafts**

Add to `scripts/ingest.py`:

```python
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
```

- [ ] **Step 12: Run all tests**

```bash
python -m pytest tests/test_ingest.py -v
```

Expected: 5 tests PASS

- [ ] **Step 13: Add CLI entry point to ingest.py**

Add to the bottom of `scripts/ingest.py`:

```python
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
```

- [ ] **Step 14: Commit**

```bash
git add scripts/ingest.py tests/test_ingest.py
git commit -m "feat: add ingest script with frontmatter parsing and draft generation"
```

---

### Task 3: Build the FastMCP server (TDD)

**Files:**
- Create: `server.py`
- Create: `tests/test_server.py`

- [ ] **Step 1: Write tests for the server**

Create `tests/test_server.py`:

```python
from pathlib import Path
import tempfile

from server import create_server


def test_get_all_context(tmp_path):
    """Test that get_all_context returns all markdown files."""
    context_dir = tmp_path / "context"
    context_dir.mkdir()
    (context_dir / "identity.md").write_text("# Identity\nTest identity content")
    (context_dir / "writing-style.md").write_text("# Writing Style\nTest style content")

    mcp = create_server(context_dir)

    # Access the tool function directly
    tools = {t.name: t for t in mcp._tool_manager.list_tools()}
    assert "get_all_context" in tools
    assert "get_writing_style" in tools


def test_get_writing_style(tmp_path):
    """Test the writing style convenience tool."""
    context_dir = tmp_path / "context"
    context_dir.mkdir()
    (context_dir / "writing-style.md").write_text("# Writing Style\nI write casually.")

    mcp = create_server(context_dir)
    tools = {t.name: t for t in mcp._tool_manager.list_tools()}
    assert "get_writing_style" in tools
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python -m pytest tests/test_server.py -v
```

Expected: FAIL — `ModuleNotFoundError: No module named 'server'`

- [ ] **Step 3: Implement the server**

Create `server.py`:

```python
"""FastMCP server for personal context."""

from pathlib import Path

from fastmcp import FastMCP


def create_server(context_dir: Path | None = None) -> FastMCP:
    """Create and configure the FastMCP server.

    Args:
        context_dir: Path to context files. Defaults to ./context/
    """
    if context_dir is None:
        context_dir = Path(__file__).parent / "context"

    mcp = FastMCP("personal-context")

    @mcp.resource("context://{filename}")
    def get_context(filename: str) -> str:
        """Read a specific personal context file by name.

        Available files: identity.md, writing-style.md, opinions.md,
        expertise.md, projects.md, communication.md
        """
        path = context_dir / filename
        if not path.exists():
            available = [f.name for f in context_dir.glob("*.md")]
            return f"File '{filename}' not found. Available: {', '.join(available)}"
        return path.read_text()

    @mcp.tool
    def get_all_context() -> dict[str, str]:
        """Get all personal context files at once.

        Returns a dictionary mapping filename to file contents for all
        context markdown files (identity, writing-style, opinions,
        expertise, projects, communication).
        """
        return {f.name: f.read_text() for f in sorted(context_dir.glob("*.md"))}

    @mcp.tool
    def get_writing_style() -> str:
        """Get Aaron's writing style context.

        Returns the full writing-style.md file which describes voice,
        tone, patterns, vocabulary, and annotated examples of how Aaron writes.
        This is the most commonly needed context file.
        """
        path = context_dir / "writing-style.md"
        if not path.exists():
            return "writing-style.md not found. Run the ingest script first."
        return path.read_text()

    return mcp


if __name__ == "__main__":
    server = create_server()
    server.run()
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python -m pytest tests/test_server.py -v
```

Expected: 2 tests PASS

- [ ] **Step 5: Manually verify the server starts**

```bash
python server.py &
# Should start without errors. Kill it after confirming:
kill %1
```

- [ ] **Step 6: Commit**

```bash
git add server.py tests/test_server.py
git commit -m "feat: add FastMCP server with context resources and tools"
```

---

### Task 4: Import blog posts and run ingest

**Files:**
- Populate: `sources/blogs/` (symlink to aaronroy.com blog content)
- Generate: `drafts/*.md`

- [ ] **Step 1: Clone or symlink blog posts**

```bash
cd ~/Documents/dev/personal-context

# If aaronroy.com repo exists locally:
ln -s ~/Documents/dev/aaronroy.com/src/content/blog sources/blogs

# Otherwise clone just the blog content:
# git clone --depth 1 https://github.com/amr05008/aaronroy.com.git /tmp/aaronroy-blog
# cp /tmp/aaronroy-blog/src/content/blog/*.md sources/blogs/
```

Verify: `ls sources/blogs/*.md | head -5` should show blog post files.

- [ ] **Step 2: Run ingest with 2-year cutoff**

```bash
python scripts/ingest.py sources/blogs/ --cutoff 2024-04-06 --output drafts
```

Expected output: something like "Loaded N posts" and "Generated 4 draft files in drafts/"

- [ ] **Step 3: Review draft output**

Check `drafts/` for the generated files. These are raw material for the interview step — excerpts grouped by category. Verify they contain recent post content.

```bash
ls drafts/
head -30 drafts/writing-style.md
```

- [ ] **Step 4: Commit (drafts are gitignored, but commit the symlink or source setup)**

```bash
git add sources/blogs  # or add a note in README about setup
git commit -m "chore: link blog posts as ingest source"
```

---

### Task 5: Interview and curate context files

This is the most important task — it produces the actual context files. This task is interactive: Claude reads the drafts and existing knowledge, then interviews Aaron to fill gaps.

**Files:**
- Create: `context/identity.md`
- Create: `context/writing-style.md`
- Create: `context/opinions.md`
- Create: `context/expertise.md`
- Create: `context/projects.md`
- Create: `context/communication.md`

- [ ] **Step 1: Create identity.md**

Bootstrap from known context (memory, blogs). Interview for gaps. Write to `context/identity.md` following the frontmatter format from the spec.

Key sections: Background, Career Arc, Personal, Values/What Drives Me.

- [ ] **Step 2: Create writing-style.md**

This is the primary deliverable. Analyze the recent blog posts (from `drafts/writing-style.md` excerpts) for:
- Voice characteristics (conversational? direct? technical?)
- Sentence structure patterns
- Vocabulary preferences
- Tone markers
- Context-specific variations (blog vs. other)
- 2-3 annotated examples showing the style in action

Interview Aaron for: how his writing differs at work vs. personal, Slack style, email style.

Write to `context/writing-style.md`.

- [ ] **Step 3: Create opinions.md**

Pull from blog drafts + interview. Key topic areas: product strategy, AI/LLMs, startups, developer tools, PLG, hardware/manufacturing.

Write to `context/opinions.md`.

- [ ] **Step 4: Create expertise.md**

Derive from blog topic distribution + career arc. Sections per domain of deep knowledge.

Write to `context/expertise.md`.

- [ ] **Step 5: Create projects.md**

Current active projects (from memory: scheduled-agents, aaronroy.com, ManyChat work) and notable past ones.

Write to `context/projects.md`.

- [ ] **Step 6: Create communication.md**

Mostly interview-driven — Slack style, email style, doc writing preferences, meeting communication.

Write to `context/communication.md`.

- [ ] **Step 7: Review and commit all context files**

```bash
ls -la context/
git add context/
git commit -m "feat: add curated personal context files"
```

---

### Task 6: Wire MCP into Claude Code and test

**Files:**
- Modify: `~/.claude/settings.json` (add MCP server config)

- [ ] **Step 1: Determine absolute path to server.py**

```bash
realpath ~/Documents/dev/personal-context/server.py
```

- [ ] **Step 2: Add MCP server to Claude Code settings**

Add to `~/.claude/settings.json` under `mcpServers`:

```json
{
  "personal-context": {
    "command": "python",
    "args": ["/Users/aaronroy/Documents/dev/personal-context/server.py"]
  }
}
```

Note: the exact path should use the output from Step 1. May also need to use the full Python path from the venv:

```json
{
  "personal-context": {
    "command": "/Users/aaronroy/Documents/dev/personal-context/.venv/bin/python",
    "args": ["/Users/aaronroy/Documents/dev/personal-context/server.py"]
  }
}
```

- [ ] **Step 3: Restart Claude Code and verify MCP is available**

Start a new Claude Code session. Verify the personal-context MCP tools appear. Test:
- Call `get_writing_style` — should return writing-style.md content
- Call `get_all_context` — should return all 6 files as a dict

- [ ] **Step 4: Real-world test**

In the new Claude Code session, ask Claude to write a blog post intro about a topic using the personal context MCP. Compare the output to Aaron's actual writing style. Iterate on `writing-style.md` if the voice doesn't match.

- [ ] **Step 5: Final commit**

```bash
cd ~/Documents/dev/personal-context
git add -A
git commit -m "docs: finalize README with setup instructions"
```

---

## Verification Checklist

- [ ] All 6 context files exist in `context/` with meaningful content
- [ ] `python -m pytest` passes all tests
- [ ] `python server.py` starts without errors
- [ ] MCP `get_writing_style` returns writing-style.md content from Claude Code
- [ ] MCP `get_all_context` returns all 6 files from Claude Code
- [ ] Real-world writing test: Claude produces output that matches Aaron's voice
