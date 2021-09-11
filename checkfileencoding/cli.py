"""Console script for checkfileencoding."""
import argparse
import sys, os, json
from .checkfileencoding import get_encoding
from rich import print, print_json



def main():
    """Console script for checkfileencoding."""
    parser = argparse.ArgumentParser()
    parser.add_argument('file',nargs='*',required=True, help='需要检查编码的文件名')
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
