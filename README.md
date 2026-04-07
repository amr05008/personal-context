# Personal Context

A minimal system for giving LLMs your writing voice, opinions, and style. Curated markdown files served via [MCP](https://modelcontextprotocol.io/) using [FastMCP](https://gofastmcp.com/).

Inspired by [Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) and [nlwhittemore's Personal Context Portfolio](https://github.com/nlwhittemore/personal-context-portfolio).

## How It Works

```
context/*.md  →  FastMCP server  →  MCP  →  Claude Code (or any MCP client)
```

You maintain 6 markdown files about yourself. A FastMCP server exposes them as tools. When you ask an LLM to write something, it can pull your context and match your voice.

### The 6 Context Files

| File | What It Captures |
|------|-----------------|
| `identity.md` | Background, career arc, personal details |
| `writing-style.md` | Voice, tone, sentence patterns, vocabulary, annotated examples |
| `opinions.md` | Stances on topics you write about |
| `expertise.md` | Domains of deep knowledge |
| `projects.md` | Current and notable past projects |
| `communication.md` | How you communicate in different contexts (Slack, email, docs) |

Each file has YAML frontmatter tracking `last_updated` and `source_refs` (which source materials informed the content).

## Getting Started

### Use this as a template

1. Fork or clone this repo
2. Delete everything in `context/` — those are my files, not yours
3. Install dependencies and start filling in your own context

### Setup

```bash
git clone <this-repo> personal-context
cd personal-context
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
```

### Bootstrap from existing writing (optional)

If you have a folder of markdown blog posts or writing samples, the ingest script can generate draft context files:

```bash
# Copy or symlink your markdown files
ln -s /path/to/your/blog/posts sources/blogs

# Generate drafts (--cutoff filters by date in frontmatter)
python scripts/ingest.py sources/blogs/ --cutoff 2024-01-01 --output drafts
```

This creates draft files in `drafts/` with excerpts grouped by category. Review them, extract what's useful, and write your curated versions into `context/`.

The ingest script expects markdown files with YAML frontmatter containing `title`, `pubDate`, and optionally `categories`. If your files don't have frontmatter, you can skip this step and write context files manually.

### Write your context files manually

If you don't have existing writing to ingest, just create the 6 files in `context/` yourself. Use this template:

```markdown
---
last_updated: 2026-04-06
source_refs: []
---

# Writing Style

## Voice
[How do you write? Conversational? Formal? Technical? Direct?]

## Patterns
[Recurring structures, transitions, vocabulary choices]

## Examples
[2-3 representative excerpts from your actual writing, with annotations]
```

A good approach: start a Claude Code session and ask it to interview you. Share writing samples and let it draft context files for you to review and edit.

### Connect to Claude Code

The MCP server runs **entirely locally** — Claude Code spawns it as a subprocess on your machine, and it just reads markdown files from disk. No data is sent to external services beyond the normal Claude API calls.

The config lives at `~/.claude/.mcp.json`, which is a **user-level** config. This means the tools are available in every Claude Code session on that machine, regardless of which project you're working in.

Add to `~/.claude/.mcp.json` (create the file if it doesn't exist):

```json
{
  "mcpServers": {
    "personal-context": {
      "command": "/absolute/path/to/personal-context/.venv/bin/python",
      "args": ["/absolute/path/to/personal-context/server.py"]
    }
  }
}
```

Restart Claude Code. The MCP tools will be available in every session.

### Setting up on another machine

To use the same context on a work machine or second computer:

1. Clone the repo: `git clone <your-fork> personal-context`
2. Install: `cd personal-context && uv venv && source .venv/bin/activate && uv pip install -e .`
3. Add the same config block to `~/.claude/.mcp.json` on that machine (update the paths to match where you cloned it)
4. Restart Claude Code

That's it — same context files, same tools, works in any repo you open. If you keep your context files committed, `git pull` on either machine keeps them in sync.

### Test it

In a new Claude Code session:
- Ask Claude to use your writing style to draft something
- It should automatically call `get_writing_style` or `get_all_context`
- Compare the output to how you actually write and iterate on your context files

## Adding Context Over Time

This system is manually curated — you update the files, not an automated pipeline.

### When to update

- **After publishing new writing** — review if it reveals patterns not yet captured in `writing-style.md`
- **After changing jobs/projects** — update `projects.md` and `identity.md`
- **After noticing the LLM gets your voice wrong** — the gap between output and expectation tells you what's missing
- **After adding new source material** — drop files in `sources/private/` (gitignored) or `sources/blogs/`, re-run ingest if helpful

### How to update

1. Edit the relevant `context/*.md` file directly
2. Update the `last_updated` date in frontmatter
3. Add any new source refs to `source_refs`
4. Commit

### Private sources

Work emails, Slack exports, or other private writing go in `sources/private/` which is gitignored. You can reference them in `source_refs` for provenance without committing the content.

### Re-running ingest

If you add new blog posts or writing samples to `sources/blogs/`:

```bash
python scripts/ingest.py sources/blogs/ --cutoff 2024-01-01 --output drafts
```

This regenerates drafts (in `drafts/`, also gitignored). Review the new excerpts and fold anything useful into your context files.

## MCP Tools

The server exposes:

| Tool/Resource | What It Does |
|--------------|-------------|
| `get_writing_style()` | Returns your writing-style.md — the most commonly needed file |
| `get_all_context()` | Returns all 6 context files as a dict |
| `context://{filename}` | Resource access to any individual file by name |

## Project Structure

```
personal-context/
├── context/           # Your curated context files (the product)
├── sources/
│   ├── blogs/         # Public writing samples (committed or symlinked)
│   └── private/       # Private writing samples (GITIGNORED)
├── scripts/
│   └── ingest.py      # Bootstrap drafts from existing writing
├── drafts/            # Generated drafts from ingest (GITIGNORED)
├── tests/             # Tests for ingest script and server
├── server.py          # FastMCP MCP server
├── pyproject.toml
└── README.md
```

## Running Tests

```bash
python -m pytest -v
```

## Security

This repo is designed to be public, but you're putting personal information in it. A few things to know:

- **Path traversal protection.** The `get_context` resource handler validates that requested filenames resolve inside the `context/` directory. Traversal attempts like `../../etc/passwd` are rejected.
- **Private sources are gitignored.** `sources/private/` is in `.gitignore` so work emails, Slack exports, etc. stay local. But be careful with `source_refs` in frontmatter — the filenames are committed even if the files aren't. Use opaque names like `work-email-1.md` instead of descriptive titles.
- **Review your context files before committing.** These files are meant to be public, but watch for details you didn't intend to share: financial specifics, internal company information, health details, or anything useful for phishing. If in doubt, leave it out.
- **`.env` is gitignored.** If you extend this with API keys, they won't be committed accidentally.

## Philosophy

- **Start minimal.** 6 files is enough. Add complexity only when you outgrow it.
- **Curate manually.** You know your voice better than any automated pipeline. The LLM can help draft, but you decide what stays.
- **Iterate from use.** The best edits come from noticing when the LLM gets something wrong about your writing.
- **Keep private things private.** The `sources/private/` directory exists so you can reference work writing without committing it.
