# This is solution to problem stated in link https://www.hackerrank.com/challenges/re-start-re-end/problem
# Points -  20
# Difficulty- Easy
# Concept usage - Regular expressions

# solution inspired from https://stackoverflow.com/questions/5616822/python-regex-find-all-overlapping-matches

import re

if __name__ == '__main__':
    
    main_str = input()
    k = input()
    s_len = len(main_str)
    offset = 0
    m = re.finditer(r'(?=('+k+'))',main_str)
    count = 0
    for match in m:
        count = count+1
        print("({}, {})".format(match.start(1), match.end(1)-1))

    if count ==0:
        print("(-1, -1)")
