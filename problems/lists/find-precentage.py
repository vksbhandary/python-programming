# This is solution to problem stated in link https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Points -  10
# Difficulty- Easy
# Concept usage - Lists and dictionary


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    count= len(student_marks[query_name])
    avg = float(sum(student_marks[query_name])/count)
    print("{:.2f}".format(round(avg, 2)))
