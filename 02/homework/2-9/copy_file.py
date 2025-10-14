#!/usr/bin/env python3
# coding=utf-8

import os

def copy_file_without_comments(source_path: str, destination_path: str) -> None:
    with open(source_path, "r") as src, open(destination_path, "w") as dst:
        for line in src:
            if not line.strip().startswith("#"):
                dst.write(line)

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    src = os.path.join(base_dir, "input.txt")
    dst = os.path.join(base_dir, "output.txt")

    copy_file_without_comments(src, dst)