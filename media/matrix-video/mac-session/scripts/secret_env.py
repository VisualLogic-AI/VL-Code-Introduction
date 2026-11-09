"""Load selected credential fields from the local Secret Root into os.environ.

Values never leave this process: nothing is printed, logged or written.
"""
import os
import shlex

DEFAULT_ROOT = os.path.expanduser("~/Documents/docs/auth/SecretRoot.local.env")


def _root_file():
    root = os.environ.get("MATRIX_SECRET_ROOT") or DEFAULT_ROOT
    if os.path.isdir(root):
        cand = os.path.join(root, "SecretRoot.local.env")
        return cand if os.path.isfile(cand) else None
    return root if os.path.isfile(root) else None


def load(names):
    """Return the set of requested names that were found (names only)."""
    path = _root_file()
    found = set()
    if not path:
        return found
    wanted = set(names)
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            if s.startswith("export "):
                s = s[7:].lstrip()
            if "=" not in s:
                continue
            key, val = s.split("=", 1)
            key = key.strip()
            if key not in wanted or key in found:
                continue
            val = val.strip()
            try:
                parts = shlex.split(val, comments=True)
                val = parts[0] if parts else ""
            except ValueError:
                val = val.strip("'\"")
            if val:
                os.environ.setdefault(key, val)
                found.add(key)
    return found
