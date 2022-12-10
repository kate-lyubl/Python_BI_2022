#!/usr/bin/env python

import argparse
import sys


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    return args


def sort_lines(content):
    content = content.split("\n")
    content.sort()
    return content


if __name__ == "__main__":
    args = read_args()
    if args.filename:
        f = open(args.filename, "r")
        content = f.read()
        f.close()
    else:
        content = sys.stdin.read()
    print(*sort_lines(content), sep="\n")

