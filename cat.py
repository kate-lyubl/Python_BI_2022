#!/usr/bin/env python

import argparse
import sys


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = read_args()
    if args.filename:
        f = open(args.filename, "r")
        content = f.read()
        f.close()
    else:
        content = sys.stdin.read()
    print(content)

