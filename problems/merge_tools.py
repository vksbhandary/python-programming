# This is solution to problem stated in link https://www.hackerrank.com/challenges/merge-the-tools/problem
# Points -  40
# Difficulty- Medium
# Concept usage - Strings

def squish(s):
    chars_ = set(s)
    visited = list()
    new_str=""
    for i in s:
        if i in visited:
            continue
        else:
            new_str = new_str+i
            visited.append(i)
    return new_str


def merge_the_tools(string, k):
    substr = [string[i:i+k] for i in range(0,len(string)-k+1, k)]
    for s in substr:
        print (squish(s))
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
