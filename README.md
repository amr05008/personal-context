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
