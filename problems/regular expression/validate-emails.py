# This is solution to problem stated in link https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
# Points -  20
# Difficulty- Easy
# Concept usage - Regular expressions & Email.utils() Library



import email.utils
import re
NUMS = "1234567890"
CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

if __name__ == '__main__':
    count = int(input())
    for _ in range(0,count):
        email_ = input()
        _ , emid = email.utils.parseaddr(email_)
        validid = re.findall(r'^['+CHAR+']['+CHAR+NUMS+'_.-]+\@['+CHAR+']+\.['+CHAR+']['+CHAR+']?['+CHAR+']?$', emid)
        if len(validid)==0:
            continue
        else:
            print(email_)


