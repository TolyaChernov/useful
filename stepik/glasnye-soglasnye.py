#!/bin/bash
# !/usr/bin/python3

# счетчик гласных и согласных
g = "ауоыиэяюёе"
s = "бвгджзйклмнпрстфхцчшщ"
gl = 0
so = 0
words = input().lower()
for i in range(len(words)):
    if words[i] in g:
        gl += 1
    elif words[i] in s:
        so += 1
print("Количество гласных букв равно ", gl,
      "\n", "Количество согласных букв равно ", so, sep="")
