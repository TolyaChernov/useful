#!/bin/bash
# !/usr/bin/python3


# dec to bin
s = ""
t = int(input())
n = 1
while t != 0:
    s = str(t % 2) + s
    t = t // 2
print(s)
