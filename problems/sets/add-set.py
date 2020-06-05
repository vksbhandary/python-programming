
# This is solution to problem stated in link https://www.hackerrank.com/challenges/py-set-add/problem
# Points -  10
# Difficulty- Easy
# Concept usage - Sets



if __name__ == '__main__':
    country_set =set()
    count = int(input())
    for _ in range(count):
        c = input()
        country_set.add(c)
    print(len(country_set))
