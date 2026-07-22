"""Runtime compatibility helpers for Reflex 0.9's generated frontend."""

import json
import logging
from pathlib import Path
import shlex
import subprocess
from collections.abc import Sequence

import reflex as rx


_PATCHED: bool = False


def _command_text(command: object) -> str:
    if isinstance(command, str):
        return command
    if isinstance(command, Sequence):
        return shlex.join(str(part) for part in command)
    return str(command)


def _package_candidates(cwd: object) -> list[Path]:
    base = Path(cwd) if cwd else Path.cwd()
    return [
        base / "package.json",
        base / ".web" / "package.json",
        base.parent / ".web" / "package.json",
    ]


def _is_frontend_export_command(command: object) -> bool:
    """Match only Bun's generated frontend export script invocation."""
    try:
        command_parts = shlex.split(_command_text(command))
    except ValueError as error:
        logging.exception(f"Failed to parse frontend command: {error}")
        return False

    for index in range(len(command_parts) - 2):
        executable = Path(command_parts[index]).name
        if (
            executable == "bun"
            and command_parts[index + 1] == "run"
            and command_parts[index + 2] == "export"
        ):
            return True
    return False


def _ensure_frontend_scripts(command: object, cwd: object) -> None:
    if not _is_frontend_export_command(command):
        return

    for package_path in _package_candidates(cwd):
        if not package_path.is_file():
            continue
        try:
            package = json.loads(package_path.read_text(encoding="utf-8"))
            scripts = package.get("scripts")
            if not isinstance(scripts, dict):
                scripts = {}
            required = {
                "export": "react-router build",
                "build": "react-router build",
                "dev": "react-router dev",
            }
            changed = False
            for name, script in required.items():
                if scripts.get(name) != script:
                    scripts[name] = script
                    changed = True
            if changed:
                package["scripts"] = scripts
                package_path.write_text(
                    json.dumps(package, indent=2) + "\n",
                    encoding="utf-8",
                )
            return
        except (OSError, json.JSONDecodeError, TypeError) as error:
            logging.exception(
                f"Failed to patch generated frontend scripts: {error}"
            )
            return


def install_runtime_compatibility_patch() -> None:
    """Patch the process boundary used by Reflex before it runs Bun export.

    Reflex 0.9.6 can generate a React Router frontend without copying the
    matching package scripts. The patch is deliberately limited to the
    `bun run export` command and leaves all application and UI behavior alone.
    """
    global _PATCHED
    if _PATCHED:
        return

    original_popen = subprocess.Popen

    def patched_popen(*args: object, **kwargs: object) -> subprocess.Popen:
        command = args[0] if args else kwargs.get("args", "")
        if _is_frontend_export_command(command):
            _ensure_frontend_scripts(command, kwargs.get("cwd"))
        return original_popen(*args, **kwargs)

    subprocess.Popen = patched_popen  # type: ignore[assignment]
    _PATCHED = True
