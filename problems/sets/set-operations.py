# Name of problem: "Set .discard(), .remove() & .pop()"
# This is solution to problem stated in link https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Points -  10
# Difficulty- Easy
# Concept usage - Sets


def set_pop(s):
    s.pop()
    return s

def set_discard(s,i):
    s.discard(i)
    return s

def set_remove(s,i):
    s.remove(i)
    return s

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    count = int(input())
    for _ in range(count):
        cmd = input().split()
        if cmd[0]=="pop":
            s = set_pop(s)
        elif cmd[0]=="remove":
            s = set_remove(s,int(cmd[1]))
        elif  cmd[0]=="discard": 
            s = set_discard(s,int(cmd[1]))

    print(sum(s))
