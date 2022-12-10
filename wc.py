#!/usr/bin/env python

import argparse
import sys


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('-w')
    parser.add_argument('-l')
    parser.add_argument('-c')
    args = parser.parse_args()
    return args


def count_lines(content):
    return len(content.split("\n"))


def count_words(content):
    return len(content.split())


def count_bytes(content):
    return len(content)


if __name__ == "__main__":
    args = read_args()
    ans = []
    if args.filename:
        f = open(args.filename, "r")
        content = f.read()
        f.close()
    else:
        content = sys.stdin.read()
    if not args.l and not args.w and not args.c:
        ans.append(count_lines(content))
        ans.append(count_words(content))
        ans.append(count_bytes(content))
    else:
        for opt, func in zip([args.l, args.w, args.c], [count_lines, count_words, count_bytes]):
            if opt:
                ans.append(func(content))
    print(*ans)

