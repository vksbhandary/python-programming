
# This is solution to problem stated in link https://www.hackerrank.com/challenges/the-minion-game/problem
# Points -  40
# Difficulty- Medium
# Concept usage - Strings

## In this problem two users have to play a game and create all possible substrings
## The number of substrings created is dependent on starting index and the remaining string
## all the generated substrings can be printed by removing the commented code
## its commented to reduce the execution time


def getall_substring_score(string, use_vowels=False):
    
    score = 0
    length_ = len(string)
    for i, s in enumerate(string):
        if use_vowels and s in "AEIOU":
            score += len(range(i + 1, length_ + 1))
            # for j in range(i + 1, length_ + 1):
                # print(string[i: j])
        elif not use_vowels and not s in "AEIOU":
            score += len(range(i + 1, length_ + 1))
            # for j in range(i + 1, length_ + 1):
                # print(string[i: j])
           
    return score


def minion_game(string):
    s_score = getall_substring_score(string)
    k_score = getall_substring_score(string,use_vowels=True)
    if s_score>k_score:
        print("Stuart {}".format(s_score))
    elif k_score>s_score:
        print("Kevin {}".format(k_score))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
