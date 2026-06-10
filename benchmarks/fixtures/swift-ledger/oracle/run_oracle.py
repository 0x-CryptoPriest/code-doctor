#!/usr/bin/env python3
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def main():
    candidate = Path(sys.argv[1]).resolve()
    oracle = Path(__file__).with_name("OracleMain.swift")
    with tempfile.TemporaryDirectory() as temp:
        work = Path(temp) / "repo"
        shutil.copytree(candidate, work)
        main = Path(temp) / "main.swift"
        shutil.copy2(oracle, main)
        binary = Path(temp) / "oracle-test"
        result = subprocess.run(
            [
                "swiftc",
                str(work / "Sources" / "LedgerKit" / "Ledger.swift"),
                str(main),
                "-o",
                str(binary),
            ],
            cwd=work,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=120,
        )
        if result.returncode == 0:
            result = subprocess.run(
                [str(binary)],
                cwd=work,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=120,
            )
        print(result.stdout)
        return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
