#!/usr/bin/env python3

import argparse
import os
import shutil


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('-r', action='store_true')
    args = parser.parse_args()
    return args


def remove_all_files(path):
    shutil.rmtree(path)


def remove_file(path):
    os.remove(path)


if __name__ == "__main__":
    args = read_args()
    path = args.filename
    if path:
        if args.r:
            remove_all_files(path)
        else:
            remove_file(path)


