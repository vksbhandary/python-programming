# This is solution to problem stated in link https://www.hackerrank.com/challenges/python-lists/problem
# Points -  10
# Difficulty- Easy
# Concept usage - Lists

def insert_at(list_arr, indx, item):
    list_arr.insert(indx, item)
    return list_arr

def append_item(list_arr, item):
    list_arr.append(item)
    return list_arr

def get_reverse(list_arr):
    b = []
    for i in reversed(list_arr):
        b.append(i)
    return b

def get_sorted(list_arr):
    return sorted(list_arr)

def remove_item(list_arr, item):
    list_arr.remove(item)
    return list_arr

def pop_list(list_arr):
    list_arr.pop()
    return list_arr


if __name__ == '__main__':
    N = int(input())
    list_ar = []
    for i in range(0,N):
        line = input()
        line = line.split(" ")
        if line[0]=="insert":
            list_ar = insert_at(list_ar, int(line[1]), int(line[2]))
        elif line[0]=="print":
            print(list_ar)
        elif line[0]=="remove":
            list_ar = remove_item(list_ar, int(line[1]))
        elif line[0]=="append":
            list_ar = append_item(list_ar, int(line[1]))
        elif line[0]=="sort":
            list_ar = get_sorted(list_ar)
        elif line[0]=="pop":
            list_ar = pop_list(list_ar)
        elif line[0]=="reverse":
            list_ar = get_reverse(list_ar)
        else:
            pass

