# -*- coding: utf-8 -*-
"""Simple file read demo for local study notes."""
import os

print("hello world")


def testprint():
    print("=====main start")
    print("main")
    print("=====main end")


def test():
    today = "20210531"
    print(today)
    print(today + "_test")


def get_file_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.txt")


def read_file(file_path):
    with open(file_path, encoding="utf-8") as handle:
        for line in handle:
            print(line.rstrip("\n"))
    return 1


def hello():
    read_file(get_file_path())


if __name__ == "__main__":
    hello()
