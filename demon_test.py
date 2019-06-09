import random
from word_frequency import counter
from mystery_word import make_underscore_line

test_current_list = ["shit", "fuck", "crap", "damn", "abba", "baab", "alla", "alta", "allo", "laal", "perp", "aaaa", "sads", "asda"]
test_underscore = "____"
test_guess = "a"

# given the current guess, current list of words, and the previous selections, makes word families and coutns them
def family_maker(guess, current_list, concretes):
    families_string_list = []
    for word in current_list:
        print(word)
        word_list = zip(word, concretes)
        tuple_list = family_string(guess, word_list)
        concrete_string = make_underscore_line(tuple_list)
        families_string_list.append(concrete_string)
    new_blueprint = counter(families_string_list)
    return new_blueprint

# given a dict full of word families and their count, picks the largest family and returns the blueprint (e.g., _a__)
def family_picker(new_blueprint):
    biggest_family = max(new_blueprint, key=lambda x: new_blueprint[x])
    return biggest_family

def family_string(clean_guess, guess_record):
    new_record = []
    for i in guess_record:
        if i[1] == 1 or i[0] == clean_guess.lower():
            new_record.append([i[0], 1])
        else:
            new_record.append([i[0], 0])
    return new_record

a = family_maker(test_guess, test_current_list, test_underscore)    
print(a)
b = family_picker(a)
print(b)
