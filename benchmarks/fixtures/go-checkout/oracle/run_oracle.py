#!/usr/bin/env python3
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def main():
    candidate = Path(sys.argv[1]).resolve()
    oracle = Path(__file__).with_name("checkout_oracle_test.go")
    with tempfile.TemporaryDirectory() as temp:
        work = Path(temp) / "repo"
        shutil.copytree(candidate, work)
        shutil.copy2(oracle, work / "checkout_oracle_test.go")
        result = subprocess.run(
            ["go", "test", "./..."],
            cwd=work,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=60,
        )
        print(result.stdout)
        return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
