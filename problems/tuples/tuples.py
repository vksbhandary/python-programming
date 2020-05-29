# This is solution to problem stated in link https://www.hackerrank.com/challenges/python-tuples/problem
# Points -  10
# Difficulty- Easy
# Concept usage - Tuples


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_tup = tuple(integer_list)
    print(hash(integer_tup))
