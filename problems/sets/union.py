# Name of problem: "Set .union() Operation"
# This is solution to problem stated in link https://www.hackerrank.com/challenges/py-set-union/problem
# Points -  10
# Difficulty- Easy
# Concept usage - Sets


if __name__ == '__main__':
    a_count =int(input())
    a = set(map(int, input().split()))
    b_count = int(input())
    b = set(map(int, input().split()))
    u = a.union(b)
    print(len(u))
