
import argparse
import os, json
import sys
sys.path.append(os.path.abspath('../'))
from checkfileencoding.filefunc.function_run_time import print_run_time
from checkfileencoding.filefunc.get_encoding import get_encoding
from rich import print, print_json
from checkfileencoding.filefunc.version import version
@print_run_time
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='*', help='需要检查编码的文件名')
    parser.add_argument('-v', '--version', action="version", version=version, help="版本信息")
    args = parser.parse_args()
    for f in args.file:
        if os.path.exists(f):
            dic = get_encoding(f)
            print(os.path.basename(f))
            print_json(json.dumps(dic, indent=4, ensure_ascii=False))
        else:
            print('%s不存在...' % os.path.basename(f))
    return 0


if __name__ == "__main__":
    main()  # pragma: no cover
