import sys
from pathlib import Path
import argparse
from nxtool.nxstyle.nxstyle import Checker, CChecker

argparser: argparse.ArgumentParser = argparse.ArgumentParser(
    prog = "nxstyle",
    description = "My CLI tool"
)

argparser.add_argument(
    "-n",
    "--non-nuttx",
    action = "store_false",
    dest = "nuttx_codebase",
    help = "disable checks that are not relevant for non-nuttx codebase"
)

argparser.add_argument(
    "file",
    type = Path,
    help = "File to check"
)

args = argparser.parse_args()

file_path: Path = Path(args.file)

if not file_path.resolve().is_file():
    print("Not a valid file path")
    sys.exit(1)

checker: Checker | None = None

match file_path.suffix:
    case '.c':
        checker = CChecker(
            file_path,
            'c.scm',
            nuttx_codebase = args.nuttx_codebase
        )
    case '.h':
        pass
    case _:
        sys.exit(1)

if checker is not None:
    checker.check_style()

sys.exit(0)