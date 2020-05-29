# This is solution to problem stated in link https://www.hackerrank.com/challenges/hex-color-code/problem
# Points -  30
# Difficulty- Easy
# Concept usage - Regular expressions

## problem was to extract hex from css code



import re

VALID = "1234567890ABCDEFabcdef"

if __name__ == '__main__':
    n = int(input())
    lines = ""
    for _ in range(n):
        code_line = input()
        lines = lines+code_line+"\n"

    for hax in re.findall(r'#['+VALID+']{6}(?!\s*\{)|#['+VALID+']{3}(?!\s*\{)', lines):
        print(hax)

