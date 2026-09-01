from pathlib import Path

import pytest

from personal_context.cli import PUBLIC_DOCUMENTS, main


@pytest.fixture
def context_dir(tmp_path: Path) -> Path:
    directory = tmp_path / "context"
    directory.mkdir()
    for filename in PUBLIC_DOCUMENTS:
        directory.joinpath(filename).write_text(
            f"# {filename.removesuffix('.md')}\n\nContent from {filename}.\n"
        )
    directory.joinpath("private.md").write_text("# Private\n\nPrivate content.\n")
    directory.joinpath("travel.md").write_text("# Travel\n\nTravel content.\n")
    return directory


def run_cli(capsys, *args: str) -> tuple[int, str, str]:
    try:
        code = main(list(args))
    except SystemExit as exc:
        code = int(exc.code)
    captured = capsys.readouterr()
    return code, captured.out, captured.err


def test_list_and_get_public_documents(context_dir, capsys):
    code, stdout, stderr = run_cli(
        capsys, "list", "--context-dir", str(context_dir)
    )

    assert code == 0
    assert stdout.splitlines() == list(PUBLIC_DOCUMENTS)
    assert "private.md" not in stdout
    assert stderr == ""

    code, stdout, stderr = run_cli(
        capsys, "get", "writing-style", "--context-dir", str(context_dir)
    )

    assert code == 0
    assert stdout == "# writing-style\n\nContent from writing-style.md.\n"
    assert stderr == ""


def test_get_multiple_documents_has_source_boundaries(context_dir, capsys):
    code, stdout, stderr = run_cli(
        capsys,
        "get",
        "identity.md",
        "projects",
        "--context-dir",
        str(context_dir),
    )

    assert code == 0
    assert stdout.startswith("## Source: `identity.md`\n\n")
    assert "\n\n---\n\n## Source: `projects.md`\n\n" in stdout
    assert stdout.index("identity.md") < stdout.index("projects.md")
    assert stderr == ""


def test_get_all_excludes_private_documents(context_dir, capsys):
    code, stdout, stderr = run_cli(
        capsys, "get", "--all", "--context-dir", str(context_dir)
    )

    assert code == 0
    for filename in PUBLIC_DOCUMENTS:
        assert f"## Source: `{filename}`" in stdout
    assert "private.md" not in stdout
    assert "travel.md" not in stdout
    assert stderr == ""


def test_include_private_lists_and_gets_extra_documents(context_dir, capsys):
    code, stdout, stderr = run_cli(
        capsys,
        "list",
        "--include-private",
        "--context-dir",
        str(context_dir),
    )

    assert code == 0
    assert stdout.splitlines() == [*PUBLIC_DOCUMENTS, "private.md", "travel.md"]
    assert stderr == ""

    code, stdout, stderr = run_cli(
        capsys,
        "get",
        "--all",
        "--include-private",
        "--context-dir",
        str(context_dir),
    )

    assert code == 0
    assert "## Source: `private.md`" in stdout
    assert "## Source: `travel.md`" in stdout
    assert "Private content." in stdout
    assert stderr == ""


def test_non_public_name_requires_explicit_opt_in(context_dir, capsys):
    code, stdout, stderr = run_cli(
        capsys, "get", "private", "--context-dir", str(context_dir)
    )

    assert code == 1
    assert stdout == ""
    assert "requires --include-private" in stderr

    code, stdout, stderr = run_cli(
        capsys,
        "get",
        "private.md",
        "--include-private",
        "--context-dir",
        str(context_dir),
    )

    assert code == 0
    assert stdout == "# Private\n\nPrivate content.\n"
    assert stderr == ""


def test_absent_document_is_an_error(context_dir, capsys):
    (context_dir / "projects.md").unlink()

    code, stdout, stderr = run_cli(
        capsys, "get", "projects", "--context-dir", str(context_dir)
    )

    assert code == 1
    assert stdout == ""
    assert "context document not found: projects.md" in stderr


def test_path_traversal_is_rejected(context_dir, tmp_path, capsys):
    (tmp_path / "secret.md").write_text("secret")

    code, stdout, stderr = run_cli(
        capsys,
        "get",
        "../secret.md",
        "--include-private",
        "--context-dir",
        str(context_dir),
    )

    assert code == 1
    assert stdout == ""
    assert "invalid document name" in stderr
    assert "secret" not in stdout


def test_environment_override_and_flag_precedence(tmp_path, monkeypatch, capsys):
    env_dir = tmp_path / "environment"
    env_dir.mkdir()
    env_dir.joinpath("identity.md").write_text("from environment\n")
    flag_dir = tmp_path / "flag"
    flag_dir.mkdir()
    flag_dir.joinpath("identity.md").write_text("from flag\n")
    monkeypatch.setenv("PERSONAL_CONTEXT_DIR", str(env_dir))

    code, stdout, stderr = run_cli(capsys, "get", "identity")
    assert (code, stdout, stderr) == (0, "from environment\n", "")

    code, stdout, stderr = run_cli(
        capsys, "get", "identity", "--context-dir", str(flag_dir)
    )
    assert (code, stdout, stderr) == (0, "from flag\n", "")


def test_invalid_combination_uses_stderr_and_nonzero_exit(context_dir, capsys):
    code, stdout, stderr = run_cli(
        capsys,
        "get",
        "identity",
        "--all",
        "--context-dir",
        str(context_dir),
    )

    assert code == 2
    assert stdout == ""
    assert "not both" in stderr
