# Personal Context System — Design Spec

## Context

Aaron does a lot of writing — blog posts, work docs, Slack messages, emails — across personal and professional contexts. LLMs are a core part of his workflow (primarily Claude Code), but they don't know his voice, opinions, or communication style. The goal is a portable personal context system that makes LLMs write more like him.

Phase 1 focuses on writing assistant context. Phase 2 (future) will extend to work productivity at ManyChat.

## Inspirations

- [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — persistent wiki with LLM-curated markdown, index/log files, lint checks
- [nlwhittemore's Personal Context Portfolio](https://github.com/nlwhittemore/personal-context-portfolio) — modular markdown portfolio with interview protocols and MCP wiring

## Approach: Flat Portfolio (v1)

A standalone repo with 6 curated markdown context files, an ingest script to bootstrap from existing content, and a FastMCP server to expose it to LLMs.

### Why This Approach

- Simplest path to value — 6 files, one server, done
- Aligns with manual curation preference
- MCP layer makes it portable across tools
- Easy to evolve toward wiki-style (Karpathy) later if needed

## Repo Structure

```
personal-context/
├── context/                    # The curated context files
│   ├── identity.md             # Background, career arc, personal details
│   ├── writing-style.md        # Voice, tone, patterns, vocabulary
│   ├── opinions.md             # Stances on topics (product, AI, startups, tech)
│   ├── expertise.md            # Domains of deep knowledge
│   ├── projects.md             # Current and notable past projects
│   └── communication.md        # Context-specific communication preferences
├── sources/                    # Raw material for bootstrapping
│   ├── blogs/                  # Symlink or copy of blog markdown
│   └── private/                # Work emails, etc. (GITIGNORED)
├── scripts/
│   └── ingest.py               # Processes sources → draft context
├── server.py                   # FastMCP server
├── .gitignore                  # Ignores sources/private/
├── pyproject.toml              # Python project config (fastmcp dependency)
└── README.md
```

### Privacy Boundary

- `context/` — public, committed to git
- `sources/blogs/` — public, committed or symlinked
- `sources/private/` — gitignored, never committed (work emails from Teachable/ManyChat)

## Context File Format

Each file uses this structure:

```markdown
---
last_updated: YYYY-MM-DD
source_refs:
  - blogs/some-post.md
  - private/some-email.txt
---

# [Category Name]

## [Subsection]
[Curated content]

## Examples
[Representative excerpts with annotations]
```

- `last_updated` tracks freshness
- `source_refs` tracks provenance (which sources informed this file)
- Body is free-form markdown with clear headers
- No rigid schema — optimized for readability by both humans and LLMs

### The 6 Context Files

**identity.md** — Who Aaron is. Background, career arc (3D printing → fintech → ManyChat), personal details (Brooklyn, cyclist, father). Bootstrapped from memory + interview.

**writing-style.md** — The primary deliverable. Voice characteristics, sentence patterns, vocabulary preferences, tone. Extracted from recent blog posts (last 2 years weighted higher). Includes context-specific variations (blog vs. Slack vs. formal docs) and annotated examples.

**opinions.md** — Stances on topics Aaron writes about: product strategy, AI/LLMs, startups, developer tools, PLG. Partially extractable from blogs, interview fills gaps on unwritten-about topics.

**expertise.md** — Domains of deep knowledge: 3D printing/hardware, product-led growth, chatbot platforms, AI tooling. Derived from blog topic distribution + work history.

**projects.md** — Current active projects and notable past ones. Includes personal projects (scheduled-agents, aaronroy.com) and work context. Updated manually as projects change.

**communication.md** — How Aaron communicates in different contexts. Slack style, email style, doc writing style, meeting communication. Mostly populated via interview since this isn't well-represented in blogs.

## FastMCP Server

Minimal server with three capabilities:

```python
from fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("personal-context")
CONTEXT_DIR = Path(__file__).parent / "context"

@mcp.resource("context://{filename}")
def get_context(filename: str) -> str:
    """Read a specific personal context file."""
    return (CONTEXT_DIR / filename).read_text()

@mcp.tool
def get_all_context() -> dict[str, str]:
    """Get all personal context files at once."""
    return {f.name: f.read_text() for f in CONTEXT_DIR.glob("*.md")}

@mcp.tool
def get_writing_style() -> str:
    """Get writing style context — the most commonly needed file."""
    return (CONTEXT_DIR / "writing-style.md").read_text()
```

1. **`context://{filename}` resource** — individual file access by name
2. **`get_all_context` tool** — bulk retrieval for full context loading
3. **`get_writing_style` tool** — convenience shortcut for the primary use case

### Claude Code Integration

Add to `~/.claude/settings.json` MCP config:

```json
{
  "mcpServers": {
    "personal-context": {
      "command": "python",
      "args": ["/path/to/personal-context/server.py"]
    }
  }
}
```

## Ingest Script

`scripts/ingest.py` is a bootstrapping helper, not an automated pipeline.

**What it does:**
- Reads markdown files from `sources/blogs/` and optionally `sources/private/`
- Weights content by recency (last 2 years prioritized)
- Groups extracted content by relevance to each of the 6 context categories
- Generates draft `.md` files with extracted quotes, patterns, and observations
- Outputs drafts to `context/` for manual review and curation

**What it doesn't do:**
- No automatic updates — you run it manually when adding new source material
- No LLM calls in v1 — it extracts frontmatter, groups posts by topic/date, and collates excerpts. Actual style analysis happens during the interview step with Claude.
- No overwriting — warns if context files already exist, outputs to a `drafts/` directory instead

## Bootstrapping Flow

1. **Scaffold** — create repo, install dependencies, set up directory structure
2. **Import blogs** — symlink or copy recent blog posts into `sources/blogs/`
3. **Run ingest** — generate draft context files from blog content
4. **Interview** — go through each context file, review blog-extracted content, ask targeted questions to fill gaps
5. **Curate** — Aaron reviews and edits all 6 files into their final form
6. **Stand up MCP** — configure FastMCP server, wire into Claude Code
7. **Test** — use the MCP in a real writing task to validate the system works

## Verification

- [ ] All 6 context files exist and contain meaningful content
- [ ] FastMCP server starts without errors
- [ ] `get_writing_style` tool returns writing-style.md content
- [ ] `get_all_context` tool returns all 6 files
- [ ] MCP is accessible from a new Claude Code session
- [ ] Real-world test: ask Claude to write a blog post intro using the context, compare voice match
