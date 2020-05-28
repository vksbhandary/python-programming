# This is solution to problem stated in link https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
# Points -  20
# Difficulty- Medium
# Concept usage - Regular expressions

## added multiple lines for both cases because
## it didnt replace all " && " by " and " in case two  && are joint together
## maybe i need to revisit this solution later

import re

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        line_str = input()
        line_str =  re.sub("\s\&\&\s", " and ", line_str)
        line_str =  re.sub("\s\&\&\s", " and ", line_str)

        line_str =  re.sub("\s\|\|\s", " or ", line_str)
        line_str =  re.sub("\s\|\|\s", " or ", line_str)
        print(line_str)



