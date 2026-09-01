"""Command-line access to local personal context files."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Sequence

PUBLIC_DOCUMENTS = (
    "identity.md",
    "writing-style.md",
    "opinions.md",
    "expertise.md",
    "projects.md",
    "communication.md",
)
ENV_CONTEXT_DIR = "PERSONAL_CONTEXT_DIR"
DEFAULT_CONTEXT_DIR = Path(__file__).resolve().parent.parent / "context"


class CLIError(Exception):
    """An error that should be reported without a traceback."""


def _add_context_dir_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--context-dir",
        type=Path,
        default=argparse.SUPPRESS,
        help=(
            "directory containing context Markdown files; overrides "
            f"{ENV_CONTEXT_DIR} and the repository default"
        ),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="personal-context",
        description="Read curated personal context from local Markdown files.",
        epilog=(
            "Only the six curated public documents are shown by default. "
            "Use --include-private explicitly to include other local .md files."
        ),
    )
    _add_context_dir_argument(parser)
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser(
        "list", help="list available context documents"
    )
    _add_context_dir_argument(list_parser)
    list_parser.add_argument(
        "--include-private",
        action="store_true",
        help="also list non-public local Markdown files",
    )

    get_parser = subparsers.add_parser("get", help="print context documents")
    _add_context_dir_argument(get_parser)
    get_parser.add_argument(
        "names",
        nargs="*",
        metavar="NAME",
        help="document name, with or without the .md suffix",
    )
    get_parser.add_argument(
        "--all",
        action="store_true",
        help="print all six curated public documents",
    )
    get_parser.add_argument(
        "--include-private",
        action="store_true",
        help="allow other local .md files (and include them with --all)",
    )
    return parser


def _context_dir(args: argparse.Namespace) -> Path:
    if hasattr(args, "context_dir"):
        return args.context_dir.expanduser()

    configured = os.environ.get(ENV_CONTEXT_DIR)
    if configured:
        return Path(configured).expanduser()

    return DEFAULT_CONTEXT_DIR


def _require_context_dir(context_dir: Path) -> Path:
    try:
        resolved = context_dir.resolve()
    except OSError as exc:
        raise CLIError(f"cannot resolve context directory '{context_dir}': {exc}") from exc

    if not resolved.is_dir():
        raise CLIError(f"context directory not found: {context_dir}")
    return resolved


def _normalize_name(name: str) -> str:
    if not name or Path(name).is_absolute() or "/" in name or "\\" in name:
        raise CLIError(f"invalid document name: {name!r}")

    suffix = Path(name).suffix
    if not suffix:
        return f"{name}.md"
    if suffix != ".md":
        raise CLIError(f"document names must end in .md: {name!r}")
    return name


def _document_path(context_dir: Path, filename: str) -> Path:
    # Only direct entries can be selected. A symlink deliberately placed in
    # context/ remains a valid curated entry, matching the repository's MCP use.
    if (
        not filename
        or Path(filename).name != filename
        or "/" in filename
        or "\\" in filename
    ):
        raise CLIError(f"invalid document name: {filename!r}")

    candidate = context_dir / filename
    if not candidate.is_file():
        raise CLIError(f"context document not found: {filename}")
    return candidate


def _available_documents(context_dir: Path, include_private: bool) -> list[str]:
    public = []
    for filename in PUBLIC_DOCUMENTS:
        if (context_dir / filename).is_file():
            _document_path(context_dir, filename)
            public.append(filename)
    if not include_private:
        return public

    public_set = set(PUBLIC_DOCUMENTS)
    extras = sorted(
        path.name
        for path in context_dir.glob("*.md")
        if path.is_file() and path.name not in public_set
    )
    for filename in extras:
        _document_path(context_dir, filename)
    return public + extras


def _read_documents(context_dir: Path, filenames: Sequence[str]) -> list[tuple[str, str]]:
    documents = []
    for filename in filenames:
        path = _document_path(context_dir, filename)
        try:
            documents.append((filename, path.read_text()))
        except (OSError, UnicodeError) as exc:
            raise CLIError(f"cannot read context document '{filename}': {exc}") from exc
    return documents


def _render_documents(documents: Sequence[tuple[str, str]]) -> str:
    if len(documents) == 1:
        return documents[0][1].rstrip() + "\n"

    sections = [
        f"## Source: `{filename}`\n\n{content.rstrip()}"
        for filename, content in documents
    ]
    return "\n\n---\n\n".join(sections) + "\n"


def _run(args: argparse.Namespace, parser: argparse.ArgumentParser) -> str:
    context_dir = _require_context_dir(_context_dir(args))

    if args.command == "list":
        filenames = _available_documents(context_dir, args.include_private)
        return "".join(f"{filename}\n" for filename in filenames)

    if args.all and args.names:
        parser.error("get accepts document names or --all, not both")
    if not args.all and not args.names:
        parser.error("get requires at least one document name or --all")

    if args.all:
        filenames = list(PUBLIC_DOCUMENTS)
        if args.include_private:
            available = _available_documents(context_dir, include_private=True)
            filenames.extend(
                filename for filename in available if filename not in PUBLIC_DOCUMENTS
            )
    else:
        filenames = [_normalize_name(name) for name in args.names]
        if not args.include_private:
            disallowed = [name for name in filenames if name not in PUBLIC_DOCUMENTS]
            if disallowed:
                raise CLIError(
                    f"non-public document requires --include-private: {disallowed[0]}"
                )

    return _render_documents(_read_documents(context_dir, filenames))


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI and return its process exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        output = _run(args, parser)
    except CLIError as exc:
        print(f"personal-context: error: {exc}", file=sys.stderr)
        return 1

    sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
