# CIS 2131 Project 3 - Secret Word Scrambler
# imports and libraries
import argparse
import resources.initialize_word_lists as word_lists
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
    get_words = word_lists.initialize_list()
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
    # printing the selected word for testing :)
    print(selected_word)
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
    play_again = input('Do you want to play again? (Y/N): ')
    if play_again.lower() == 'y':
        return True
    elif play_again.lower() == 'n':
        return False
    else:
        raise ValueError("Invalid input. Please enter 'Y' or 'N'.")
        ask_to_play_again()

if __name__ == '__main__':
    

    while True:
        play_one_round()
        if not ask_to_play_again():
            break
            print("Thanks for playing!")