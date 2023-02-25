import random
from colorama import Fore
import colorama
import config

# import from config
COLORS = config.COLORS
TRIES = config.TRIES
CODE_LENGTH = config.CODE_LENGTH

colorama.init()

### Colors ###
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


# generate colors
def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code


def guess_code():
    prYellow("================================================================================")
    guess = input(Fore.LIGHTGREEN_EX + " Guess:").upper().split(" ")
    prYellow("================================================================================")
    while True:
        if len(guess) != CODE_LENGTH:
            prLightPurple(f"You must guess {CODE_LENGTH} colors.")
            break
        for color in guess:
            if color not in COLORS:
                prLightGray(f"Invalid color: {color}. Try again")
                break
        else:
            break
    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_position = 0
    incorrect_position = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_position += 1
            color_counts[guess_color] -= 1
    
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_position += 1
            color_counts[guess_color] -= 1
    return correct_position, incorrect_position


def game():
    prCyan(f"Welcome to master mind color guessing game, you have {TRIES} to guess the color...")
    prYellow("================================================================================")
    prPurple(f"The Valid Colors are:, {COLORS}")
    code = generate_code()
    for attempt in range(1, TRIES + 1):
        guess = guess_code()
        correct_position, incorrect_position = check_code(guess, code)
        if correct_position == CODE_LENGTH:
            prGreen(f"You guessed the code in {attempt} tries!")
            break

        prLightPurple(f"Correct position: {correct_position} | incorrect position: {incorrect_position}")
    else:
        prRed(f"Your tried are finished, the code was: , {code}")

if __name__ == "__main__":
    while True:
        game()
        yes = input(Fore.LIGHTGREEN_EX + " Type yes to continue or No to Quit: ")
        if yes == "yes":
            game()
        else:
            break