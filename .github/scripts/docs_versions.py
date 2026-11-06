#!/usr/bin/env python3
"""Rewrite versions.json of the published docs site (the gh-pages branch).

The site is laid out as:

    stable/        docs built from master
    latest/        docs built from develop
    vX.Y.Z/        releases
    versions.json  what the landing page (index.html) offers in its picker

    docs_versions.py update SITE

versions.json lists stable, latest and the newest release of each major
version. Older releases stay in SITE, so saved links to them keep working,
but nothing on the landing page points at them.
"""

import argparse
import json
import re
from pathlib import Path

RELEASE_DIR = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")

# listed ahead of the releases, as (folder, label shown in the picker)
PINNED = [("stable", "stable"), ("latest", "latest (develop)")]


def releases(site):
    """Find the release folders (vX.Y.Z) directly under site.

    The version is split into numbers so that versions compare the way people
    expect: as text "2.10.0" would sort before "2.9.0", as (2, 10, 0) it
    sorts after (2, 9, 0).

    Args:
        site: Directory holding the published docs, one folder per version.

    Returns:
        A dict mapping (major, minor, patch) to the folder name, for example
        {(2, 1, 5): "v2.1.5", (3, 0, 0): "v3.0.0"}. Folders that are not
        named vX.Y.Z, such as stable/ and latest/, are left out.
    """
    found = {}
    for folder in site.iterdir():
        match = RELEASE_DIR.match(folder.name)
        if folder.is_dir() and match:
            found[tuple(int(part) for part in match.groups())] = folder.name
    return found


def newest_per_major(found):
    """Pick the newest release of each major version.

    Args:
        found: The dict returned by releases().

    Returns:
        The versions to list, newest first. For example, 2.1.0, 2.1.5, 2.1.6
        and 3.0.0 give [(3, 0, 0), (2, 1, 6)].
    """
    newest = {}
    for version in found:
        if version[0] not in newest or version > newest[version[0]]:
            newest[version[0]] = version
    return sorted(newest.values(), reverse=True)


def update(site):
    """Write site/versions.json from the folders present in site.

    The list holds stable and latest (when their folders exist), followed by
    the newest release of each major version. The landing page reads this
    file to fill its version picker, and opens the first entry.

    Args:
        site: Directory holding the published docs, one folder per version.
    """
    found = releases(site)

    entries = [
        {"name": label, "path": f"{folder}/"}
        for folder, label in PINNED
        if (site / folder).is_dir()
    ]
    entries += [
        {"name": ".".join(map(str, version)), "path": f"{found[version]}/"}
        for version in newest_per_major(found)
    ]
    (site / "versions.json").write_text(json.dumps(entries, indent=2) + "\n")
    print("versions.json:", ", ".join(entry["name"] for entry in entries) or "(empty)")


def main():
    """Read the command line and run update(), as the docs workflow calls it:

        docs_versions.py update SITE
    """
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    commands = parser.add_subparsers(dest="command", required=True)
    rewrite = commands.add_parser("update")
    rewrite.add_argument("site", type=Path)

    args = parser.parse_args()
    update(args.site)


if __name__ == "__main__":
    main()
