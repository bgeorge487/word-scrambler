# CIS 2131 Project 3 - Secret Word Scrambler
# imports and libraries
import argparse
import create_lists
import random
# Select word from a 'predefined list'
# word will get scrambled using a function
# the player will get 3 attempts to guess the original word
# the player is told after each guess whether it's correct or not
# after each game the player can choose to play again

def main() -> None:
    pass
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--jumble')
    # args = parser.parse_args()

# get the random word
def get_random_word():
    get_words = create_lists.initialize_list()
    random_word = random.choice(get_words)
    return random_word

# scramble the word
def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    jumbled_word = "".join(letters)
    return jumbled_word

# play a single round
def play_one_round():
    selected_word = get_random_word()
    # I'm cheating to test it
    print(selected_word)
    jumble_word = scramble_word(selected_word)
    player_input = input(f'Guess the word: {jumble_word}')
    player_guess = 3
    while player_guess > 0:
        if player_input == selected_word:
            print("Congrats! you guessed correctly!")
            break
        elif player_guess > 0 and player_input != selected_word:
            print(f'Try again! You have {player_guess} tries left')
            player_guess -= 1
        else:
            print(f'Better luck next time! The word was {selected_word}')
# after each round ask if the player wants to go again
def ask_to_play_again():
    pass

if __name__ == '__main__':
    main()

play_one_round()