#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sort log lines and annotate delta milliseconds between neighbors."""
import datetime
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(SCRIPT_DIR, "test.txt")
output = os.path.join(SCRIPT_DIR, "result.log")


def get_time_ms(pre_line, next_line):
    try:
        index = pre_line.index("] ")
        next_index = next_line.index("] ")
        pre_time = datetime.datetime.strptime(
            pre_line[index + 2 : index + 25], "%Y-%m-%d %H:%M:%S.%f"
        )
        next_time = datetime.datetime.strptime(
            next_line[next_index + 2 : next_index + 25], "%Y-%m-%d %H:%M:%S.%f"
        )
        return int((next_time - pre_time).total_seconds() * 1000)
    except (ValueError, IndexError) as exc:
        print(exc)
        return 0


content = []
with open(filename, "r", encoding="utf-8") as fo:
    for line in fo:
        content.append(line.strip())

content.sort()

with open(output, "w+", encoding="utf-8", newline="\n") as wo:
    pre_line = ""
    for line in content:
        if not pre_line:
            pre_line = line
        annotated = "[{}]{}\n".format(get_time_ms(pre_line, line), line)
        wo.write(annotated)
        pre_line = line
