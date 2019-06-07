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
        length = range(4,7)
    elif difficulty_value == "m" or difficulty_value == "medium":
        length = range(6,9)
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
        clean_list.append(dirty_string.strip('\n'))
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
    # print(chosen_word)
    return chosen_word

# print(get_word(test_list))

# _____________________display length
# lets the user know the length of the chosen word 
def display_word_length(chosen_word):
    print(f"Your word is {len(chosen_word)} letters long. Best of luck.")
    
# ______________make initial underscore
# makes the tuple dictionary out of the chosen word letters and 0 by default
def make_paired_list(chosen_word):
    initial_paired_list = []
    for letter in chosen_word:
        initial_paired_list.append([letter, 0])
    return initial_paired_list

# _______________disply underscores
# displays underscores as long as the chosen word, if any of the tuples have a 1 in the value column it instead displays that letter
def make_underscore_line(guess_record):
    underscore_line = ""
    for letter, value in guess_record:
        if value == 0:
            underscore_line += "_"
        else:
            underscore_line += letter
    return underscore_line

# ______________guess guess_checker
# checks to make sure guess is correct format
def guess_checker(raw_guess):
    lower_guess = raw_guess.lower()
    if len(lower_guess) != 1 or lower_guess not in "abcdefghijklmnopqrstuvwyxz":
        print("please enter a single letter")
        return guesser()
    else:
        return lower_guess

# _________time for guesses
# asks the user to guess, takes an input, checks to amke sure it is one character then passes it
def guesser():
    print("Please make a guess")
    raw_guess = input()
    clean_guess = guess_checker(raw_guess)
    return clean_guess

# _______________guess comparer
# compares the values in guess_record to the guess and if they match changes the value to 1
def guess_compare(clean_guess, guess_record, wrong_guesses):
    new_record = []
    for i in guess_record:
        if i[1] == 1 or i[0] == clean_guess:
            new_record.append([i[0], 1])
        else:
            new_record.append([i[0], 0])
    if clean_guess not in guess_record:
        wrong_guesses += 1
    return new_record

# _________ check win 
# checks if the user has guessed all of the letters inb the chosen word
def check_if_won(guess_record):
    for i in guess_record:
        if i[1] == 0:
            return False
    print("You won!")
    return True

# ___________gues display 
# takes in the guess record and prints a list of just the guesses

# _________gameplay
# runs the game, decides whether ot keep going, stop, what to print etc.
def gameplay():
    # instantiate new blank guesses list after user selects difficulty
    print("welcome to mystery word")
    difficulty_value = ask_difficulty()
    guesses = []
    word_length_range = get_length(difficulty_value)
    possible_word_list = get_length_words(word_length_range)
    chosen_word = get_word(possible_word_list)
    display_word_length(chosen_word)
    paired_list = make_paired_list(chosen_word)
    underscore_line = make_underscore_line(paired_list)
    # print(paired_list)
    print(underscore_line)
    new_record = paired_list
    has_won = False
    wrong_guesses = 0
    while has_won == False and wrong_guesses <= 8:
        clean_guess = guesser()
        # print(clean_guess)
        guesses += clean_guess
        print("your already guessed letters are: ", end = '')
        for guess in range(len(guesses)): 
            print(guesses[guess], ",", end = '')
        print()
        new_record = guess_compare(clean_guess, new_record, wrong_guesses)
        print(make_underscore_line(new_record))
        # print(new_record)
        has_won = check_if_won(new_record)
    play_again = input("would you like to play again? [y/n]")
    if play_again == "y":
        return gameplay()


if __name__ == "__main__":
    gameplay()