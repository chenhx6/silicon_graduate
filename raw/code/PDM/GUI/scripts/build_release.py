"""Build and validate local artifacts; never reads credentials or uploads."""

from pathlib import Path
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    subprocess.run(
        [sys.executable, "-m", "build", "--no-isolation"], cwd=root, check=True
    )
    artifacts = sorted(
        str(p)
        for p in (root / "dist").iterdir()
        if p.suffix == ".whl" or p.name.endswith(".tar.gz")
    )
    subprocess.run([sys.executable, "-m", "twine", "check", "--strict", *artifacts], check=True)


if __name__ == "__main__":
    main()
