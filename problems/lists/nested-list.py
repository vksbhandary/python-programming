# This is solution to problem stated in link https://www.hackerrank.com/challenges/nested-list/problem
# Points -  10
# Difficulty- Easy
# Concept usage - Nested Lists


if __name__ == '__main__':
    names =[]
    lowest = None
    sec_low = 999999
    data = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score])
    
    lowest = data[0][1]
    for i in data:
        score = i[1]
        if lowest>score:
            sec_low = lowest
            lowest = score
        elif score<sec_low and score>lowest:
            sec_low = score

    for i, data_list in enumerate(data):
        if data[i][1]== sec_low:
            names.append(data_list[0])

    names.sort()

    for nm in names:
        print(nm)
