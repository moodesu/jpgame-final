#!/usr/bin/env python3
"""Publish a local guide image to the JP-Game V2 Hugo branch.

Example:
  python scripts/publish_guide_image.py a350-overhead "C:\Users\me\Downloads\a350.png"

Requires Python 3 and Git. Uses the already configured Git remote credentials.
The script copies the ORIGINAL image bytes: it does not redraw, resize, or optimise.
"""
from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PRESETS = {
    "a350-overhead": {
        "bundle": "content/blog/inibuilds-a350-full-flight-tutorial",
        "filename": "a350-overhead-precise-annotations.png",
        "article": "index.md",
        "shortcode": "{{< a350-overhead-image >}}",
        "heading": "## 2. Cold and dark — establishing electrical power",
    }
}

def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=REPO, text=True).strip()

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("preset", choices=PRESETS.keys())
    parser.add_argument("image", type=Path, help="Source image file on this computer")
    parser.add_argument("--no-push", action="store_true", help="Commit locally but do not push")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without copying or committing")
    parser.add_argument("--replace", action="store_true", help="Overwrite an existing different image")
    args = parser.parse_args()

    config = PRESETS[args.preset]
    src = args.image.expanduser().resolve()
    if not src.is_file():
        parser.error(f"Image not found: {src}")
    if src.suffix.lower() != Path(config["filename"]).suffix.lower():
        parser.error("The source image must be PNG for this preset; no automatic image conversion is performed.")
    if src.stat().st_size > 15 * 1024 * 1024:
        parser.error("Image exceeds 15 MB; optimise it before publishing.")

    try:
        branch = git("branch", "--show-current")
        if branch != "v2-refresh":
            parser.error(f"Expected branch v2-refresh; currently on {branch or '(detached HEAD)'}")
        staged = git("diff", "--cached", "--name-only")
        if staged:
            parser.error("Other files are already staged. Commit or unstage them first to avoid mixing changes.")
    except FileNotFoundError:
        parser.error("Git is not installed or not available on PATH.")

    directory = REPO / config["bundle"]
    dest = directory / config["filename"]
    article = directory / config["article"]
    if not article.is_file():
        parser.error(f"Hugo article not found: {article}")
    text = article.read_text(encoding="utf-8")
    shortcode = config["shortcode"]
    new_text = text
    if shortcode not in text:
        heading = config["heading"]
        if heading not in text:
            parser.error(f"Expected insertion heading missing: {heading}")
        new_text = text.replace(heading, heading + "\n\n" + shortcode, 1)

    changed_image = not dest.exists() or digest(dest) != digest(src)
    if changed_image and dest.exists() and not args.replace:
        parser.error(f"Different file already exists: {dest}. Use --replace to overwrite.")
    changed_article = new_text != text

    print(f"Source: {src}")
    print(f"Destination: {dest.relative_to(REPO)}")
    print(f"Image: {'new/changed' if changed_image else 'identical'}")
    print(f"Article: {'shortcode added' if changed_article else 'already configured'}")
    if args.dry_run:
        print("Dry run: nothing changed.")
        return 0
    if not changed_image and not changed_article:
        print("No changes to commit.")
        return 0

    if changed_image:
        directory.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dest)
    if changed_article:
        article.write_text(new_text, encoding="utf-8")
    paths = [str(dest.relative_to(REPO))]
    if changed_article:
        paths.append(str(article.relative_to(REPO)))
    git("add", "--", *paths)
    git("commit", "-m", f"docs: publish {args.preset} annotated guide image")
    commit = git("rev-parse", "--short", "HEAD")
    print(f"Committed: {commit}")
    if args.no_push:
        print("Local commit only (--no-push).")
    else:
        print("Pushing to origin/v2-refresh (Netlify auto-deploys this branch)...")
        subprocess.run(["git", "push", "origin", "v2-refresh"], cwd=REPO, check=True)
        print("Push completed. Check the Netlify deployment before announcing the page is live.")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as error:
        print(f"Git command failed (exit {error.returncode}): {error.cmd}", file=sys.stderr)
        raise SystemExit(error.returncode)
