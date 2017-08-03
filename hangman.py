import os
from words import random_word


def clear_screen():
    os.system('cls')


def display_board(man_state, word, correctly_guessed):
    clear_screen()
    display_man(man_state)
    display_word(word, correctly_guessed)


def display_man(man_state):
    man_body = ["0", "|", "/", "\\", "/", "\\"]
    man = """
         ____
        /    |
        |    {0}
        |   {2}{1}{3}
        |   {4} {5}
       /|\\
        """
    # Fill new_man with 6 spaces
    new_man = [" " for i in range(0, 6)]
    # Replace each space with a bodypart from man_body until man_state
    for i, body_part in enumerate(man_body):
        if i < man_state:
            new_man[i] = body_part

    print(man.format(*new_man))


def display_word(word, correctly_guessed):
    # Makes a list of each letter in word thats been guessed
    # unguessed letter are replaced with "_"
    word_with_only_guessed = [(l if l in correctly_guessed else "_") for l in word]
    print(" ".join(word_with_only_guessed))


def check_win(word, guessed):
    """Returns True if every letter in word has been guessed, else False"""
    for letter in word:
        if letter not in guessed:
            return False
    return True


def check_loose(man_state):
    return man_state == 6


def check_guess(word, letter):
    return letter in word


def play(player_name):
    clear_screen()
    word = random_word()
    guessed_letters = []
    man_state = 0
    while not (check_loose(man_state) or check_win(word, guessed_letters)):
        display_board(man_state, word, guessed_letters)
        print("Guessed Letters: {}".format(", ".join(guessed_letters)))
        guess = input("> ")
        man_state += check_guess(word, guess)


if __name__ == '__main__':
    name = input("Whats your name? ")
    play(name)
