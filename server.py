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
        path = (context_dir / filename).resolve()
        if not path.is_relative_to(context_dir.resolve()):
            return "Access denied: path outside context directory"
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
