# This is solution to problem stated in link https://www.hackerrank.com/challenges/symmetric-difference/problem
# Points -  10
# Difficulty- Easy
# Concept usage - Sets


def getSymDiff(a,b):
    uni = a.union(b)
    intersect = a.intersection(b)
    sym = uni.difference(intersect)
    out = sorted(sym)
    for i in out:
        print(i)


if __name__ == '__main__':
    a_count = int(input())
    a = input()
    a = a.split()
    a = set(map(int, a))
    b_count = int(input())
    b = input()
    b = b.split()
    b = set(map(int, b))

    getSymDiff(a,b)
