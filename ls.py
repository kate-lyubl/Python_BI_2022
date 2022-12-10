#!/usr/bin/env python3

import os
import argparse


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?')
    parser.add_argument('-a', action='store_true')
    args = parser.parse_args()
    return args


def get_all_files(path):
    return [f for f in os.listdir(path)]


def get_files(path):
    return [f for f in os.listdir(path) if f[0] != "."]


if __name__ == "__main__":
    args = read_args()
    if args.filename:
        path = args.filename
    else:
        path = os.getcwd()
    if not args.a:
        print(*get_files(path), sep='\n')
    else:
        print(*get_all_files(path), sep='\n')
