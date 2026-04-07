import asyncio
from pathlib import Path

from server import create_server


def test_list_tools(tmp_path):
    """Test that the server registers expected tools."""
    context_dir = tmp_path / "context"
    context_dir.mkdir()
    (context_dir / "identity.md").write_text("# Identity\nTest identity content")
    (context_dir / "writing-style.md").write_text("# Writing Style\nTest style content")

    mcp = create_server(context_dir)

    tools = asyncio.run(mcp.list_tools())
    tool_names = [t.name for t in tools]
    assert "get_all_context" in tool_names
    assert "get_writing_style" in tool_names


def test_get_all_context(tmp_path):
    """Test that get_all_context returns all markdown files."""
    context_dir = tmp_path / "context"
    context_dir.mkdir()
    (context_dir / "identity.md").write_text("# Identity\nTest identity content")
    (context_dir / "writing-style.md").write_text("# Writing Style\nTest style content")

    mcp = create_server(context_dir)

    result = asyncio.run(mcp.call_tool("get_all_context", {}))
    # result.structured_content contains the dict directly
    data = result.structured_content
    assert "identity.md" in data
    assert "writing-style.md" in data
    assert "Test identity content" in data["identity.md"]


def test_get_writing_style(tmp_path):
    """Test the writing style convenience tool."""
    context_dir = tmp_path / "context"
    context_dir.mkdir()
    (context_dir / "writing-style.md").write_text("# Writing Style\nI write casually.")

    mcp = create_server(context_dir)

    result = asyncio.run(mcp.call_tool("get_writing_style", {}))
    text = result.content[0].text
    assert "I write casually" in text


def test_get_writing_style_missing(tmp_path):
    """Test writing style tool when file doesn't exist."""
    context_dir = tmp_path / "context"
    context_dir.mkdir()

    mcp = create_server(context_dir)

    result = asyncio.run(mcp.call_tool("get_writing_style", {}))
    text = result.content[0].text
    assert "not found" in text
