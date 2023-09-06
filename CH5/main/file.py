# 計算文章中單字出現的次數
import pandas as pd

infile = open('python_example_001.txt')
lines = infile.read().split("\n")

line_count = len(lines)
word_count = 0
char_count = 0

for line in lines:
    words = line.split()
    word_count += len(words)
    char_count += len(line)

print(f"File has {line_count} lines, {word_count} words, {char_count} characters")

str = ' '.join(lines)
w = str.split(" ")
print(pd.Series(w).value_counts())
