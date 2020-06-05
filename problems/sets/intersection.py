
# Name of problem: "Set .intersection() Operation"
# This is solution to problem stated in link https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
# Points -  10
# Difficulty- Easy
# Concept usage - Sets


if __name__ == '__main__':
    a_count =int(input())
    a = set(map(int, input().split()))
    b_count = int(input())
    b = set(map(int, input().split()))
    i = a.intersection(b)
    print(len(i))
