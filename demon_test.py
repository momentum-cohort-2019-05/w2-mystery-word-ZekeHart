import random
from word_frequency import counter
from mystery_word import make_underscore_line, guess_checker

test_current_list = ["shit", "fuck", "crap", "damn", "abba", "baab", "alla", "alta", "allo", "laal", "perp", "aaaa", "sads", "asda"]
test_current_two = ["astro", "astra", "fatso", "artsy", "ratso", "ddtff"]
test_underscore = "__t__"
test_guess = "a"

def pick_guesses():
    num_guesses = input("please choose a number of guesses for your game foolish human")
    return num_guesses

def choose_word_length():
    word_length = input("please choose a length of word to guess pathetic fleshbag")
    return word_length



# given the current guess, current list of words, and the previous selections, makes word families and coutns them
def family_maker(guess, current_list, concretes):
    families_string_list = []
    zeroed_concretes = []
    for letter in concretes:
        if letter == '_':
            zeroed_concretes.append(0)
        else:
            zeroed_concretes.append(1)
    for word in current_list:
        print(word)
        word_list = zip(word, zeroed_concretes)
        tuple_list = family_string(guess, word_list)
        concrete_string = make_underscore_line(tuple_list)
        families_string_list.append(concrete_string)
    new_blueprint = counter(families_string_list)
    return new_blueprint

# given a dict full of word families and their count, picks the largest family and returns the blueprint (e.g., _a__)
def family_picker(new_blueprint):
    biggest_family = max(new_blueprint, key=lambda x: new_blueprint[x])
    return biggest_family

# given a text file and a word length, generates a list of words of that length. defaults to words.txt
def get_initial_list(word_length, file="words.txt"):
    with open(file) as unclean:
        unclean_list = unclean.readlines()
    clean_list = []
    for dirty_string in unclean_list:
        clean_list.append(dirty_string.strip('\n'))
    possibles_list = []
    for w_string in clean_list:
        if len(w_string) == word_length:
            possibles_list.append(w_string)
    return possibles_list

def family_string(clean_guess, guess_record):
    new_record = []
    for i in guess_record:
        if i[1] == 1 or i[0] == clean_guess.lower():
            new_record.append([i[0], 1])
        else:
            new_record.append([i[0], 0])
    return new_record

def gameplay():
    guesses = []
    has_won = False
    wrong_guesses = 0
    num_guesses = pick_guesses()
    word_length = choose_word_length()


if __name__ == "__main__":
    gameplay()

# a = family_maker(test_guess, test_current_two, test_underscore)    
# print(a)
# b = family_picker(a)
# print(b)
