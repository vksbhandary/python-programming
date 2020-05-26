# This is solution to problem stated in link https://www.hackerrank.com/challenges/validating-the-phone-number/problem
# Points -  20
# Difficulty- Easy
# Concept usage - Regular expression

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
total = int(input())


for i in range(0, total):
    phone=input()
    match = re.search(r'^[789][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', phone)

    if match:
        print("YES")
    else:
        print("NO")
