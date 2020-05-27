# This is solution to problem stated in link https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Points -  10
# Difficulty- Easy
# Concept usage - Lists


if __name__ == '__main__':
    n = int(input())
    arr = [ int(i) for i in input().split() ]
    
    winner = arr[0]
    runner_up = -100
    for i in arr:
        if i > winner:
            runner_up = winner
            winner = i
        elif runner_up<i and i < winner:
            runner_up = i

    print(runner_up)

