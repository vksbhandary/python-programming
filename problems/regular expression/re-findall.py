# This is solution to problem stated in link https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
# Points -  20
# Difficulty- Easy
# Concept usage - Lists and dictionary

import re

if __name__ == '__main__':
    str_ = input()
    matches = re.findall(r'[AEIOUaeiou][AEIOUaeiou]+',str_)
    counts = 0
    for i in matches:
        if not str_.startswith(i) and not str_.endswith(i):
            print(i)
            counts = counts+1
    if(counts==0):
        print(-1)
