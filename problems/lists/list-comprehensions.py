# This is solution to problem stated in link https://www.hackerrank.com/challenges/list-comprehensions/problem
# Points -  10
# Difficulty- Easy
# Concept usage - List Comprehensions

if __name__ == '__main__':
    op_list = []
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                if not i+j+k ==n:
                    op_list.append([i,j,k])
        
    print(op_list)
