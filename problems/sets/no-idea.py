# This is solution to problem stated in link https://www.hackerrank.com/challenges/no-idea/problem
# Points -  50
# Difficulty- Medium
# Concept usage - Sets



def printHappiness(arr, A, B):
    score = 0
    for i in arr:
        if i in A:
            score=score+1
        elif i in B:
            score= score-1
    print(score)
    

if __name__ == '__main__':
    first = input()
    first = list(map(int, first.split()))
    n = first[0]
    m = first[1]
    arr = input()
    arr = list(map(int, arr.split()))
    A = input()
    A  = set(map(int, A.split()))
    B = input()
    B  = set(map(int, B.split()))
    printHappiness(arr, A, B)


