from pathlib import Path
import os
import yaml

# Repository root (one level above /tools)
REPO_ROOT = Path(__file__).resolve().parents[1]

TIERS_FILE = REPO_ROOT / "tiers" / "tiers.yml"
TIERS_DIR = REPO_ROOT / "tiers"

POINTER_HEADER = """<!-- POINTER ONLY
This file is navigation-only and has zero authority.
Do not cite this file. Cite the canonical document it links to.
-->
"""

def write_pointer(pointer_path: Path, canonical_rel: str) -> None:
    canonical_abs = REPO_ROOT / canonical_rel

    # Compute a relative link from the pointer file to the canonical file
    relative_link = os.path.relpath(canonical_abs, pointer_path.parent)
    relative_link = relative_link.replace(os.sep, "/")

    pointer_path.write_text(
        POINTER_HEADER
        + "\nThis file is a navigation pointer.\n\n"
        + "Canonical authority lives here:\n"
        + f"- [`{canonical_rel}`]({relative_link})\n",
        encoding="utf-8",
    )

def main() -> None:
    if not TIERS_FILE.exists():
        raise RuntimeError(f"Missing tier manifest: {TIERS_FILE}")

    tiers = yaml.safe_load(TIERS_FILE.read_text(encoding="utf-8"))

    for tier_name, files in tiers.items():
        tier_dir = TIERS_DIR / tier_name.replace("_", "-")
        tier_dir.mkdir(parents=True, exist_ok=True)

        # Write tier README (navigation-only)
        (tier_dir / "README.md").write_text(
            f"# {tier_name.replace('_', ' ').upper()}\n\n"
            "This folder is navigation-only.\n"
            "All files here are pointers with zero authority.\n"
            "Always cite the canonical source.\n",
            encoding="utf-8",
        )

        for canonical_rel in files:
            pointer_name = Path(canonical_rel).name
            pointer_path = tier_dir / pointer_name
            write_pointer(pointer_path, canonical_rel)

if __name__ == "__main__":
    main()
