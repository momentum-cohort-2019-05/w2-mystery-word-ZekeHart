import math
import random
import re
difficulty_list = ["e", "m", "h", "easy", "medium", "hard"]

# ___________greeting and input
def ask_difficulty():
    difficulty = input("Please select a difficulty level Easy (e), Medium (m), or Hard (h)")
    print(difficulty)
    if difficulty.lower() not in difficulty_list:
        ask_difficulty()
    else:
        return difficulty.lower()
    


# print("hello, welcome to the game")
# print(ask_difficulty())



# _______________get length
# # takes difficulty as argument, and depending on length finds a word of corresponding legnth
def get_length(difficulty_value):
    if difficulty_value == "e" or difficulty_value == "easy":
        length = range(4,6)
    elif difficulty_value == "m" or difficulty_value == "medium":
        length = range(6,8)
    else:
        length = range(8, 50)
    return length





# _________________get possibles list
# takes a length, opens the file and gets a list of all words of that length
def get_length_words(length_range):
    with open("words.txt") as unclean:
        unclean_list = unclean.readlines()
    clean_list = []
    for dirty_string in unclean_list:
        dirty_string = dirty_string[:-2]
        clean_list.append(dirty_string)
    possibles_list = []
    for w_string in clean_list:
        for x in length_range:
            if len(w_string) == x:
                possibles_list.append(w_string)
    return possibles_list

# x = range(5,9)
# test_list = get_length_words(x)

# ________________pick word
# takes a cleaned list of words in a specifc range and returns one word
def get_word(possibilities_list):
    list_size = len(possibilities_list)
    chosen_index = random.randint(1,list_size)
    chosen_index -= 1
    chosen_word = possibilities_list[chosen_index]
    return chosen_word

# print(get_word(test_list))





a_test = ask_difficulty()
b_test = get_length(a_test)
c_test = get_length_words(b_test)
d_test = get_word(c_test)
print(d_test)











# _________________get possibles list DO NOT USE OLD VERSION
# takes a length, opens the file and gets a list of all words of that length
# def get_length_words____old(length):
#     with open("words.txt") as unclean:
#         unclean_list = unclean.readlines()
#     clean_list = []
#     for dirty_string in unclean_list:
#         dirty_string = dirty_string[:-2]
#         clean_list.append(dirty_string)
#     possibles_list = []
#     for w_string in clean_list:
#         if len(w_string) == length:
#             possibles_list.append(w_string)
#     return possibles_list

# # print(get_length_words(15))



# # _______________get length DO NOT USE OLD
# # # takes difficulty as argument, and depending on length finds a word of corresponding legnth
# def get_length________old(difficulty_value):
#     if difficulty_value == "e" or difficulty_value == "easy":
#         length = random.randint(4,6)
#     elif difficulty_value == "m" or difficulty_value == "medium":
#         length = random.randint(6,8)
#     else:
#         length = random.randint(8, 29)
#         if length == 26:
#             length -= 1
#         elif length == 27:
#             length += 1
#     return length

