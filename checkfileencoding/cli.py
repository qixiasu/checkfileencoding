"""Console script for checkfileencoding."""
import argparse
import sys, os, json
from .checkfileencoding import get_encoding
from rich import print, print_json
from .__version__ import version
from .function_run_time import print_run_time

@print_run_time
def main():
    """Console script for checkfileencoding."""
    parser = argparse.ArgumentParser()
    parser.add_argument('file',nargs='*', help='需要检查编码的文件名')
    parser.add_argument('-v','--version',action="version", version=version, help="版本信息")
    args = parser.parse_args()
    for f in args.file:
        if os.path.exists(f):
            dict = get_encoding(f)
            print(os.path.basename(f))
            print_json(json.dumps(dict, indent=4, ensure_ascii=False))
        else:
            print('%s不存在...'% os.path.basename(f))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
