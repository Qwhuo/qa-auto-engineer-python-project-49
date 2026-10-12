import random
import prompt
from brain_games.scripts.utils.main_pattern import main_pattern


def game():
    number = random.randint(1, 1000000)
    print(f"Question: {number}")
    answer = prompt.string("Your answer: ")
    if (answer == "yes" and number % 2 == 0) or (answer == "no" and number % 2 != 0):
        print("Correct!")
    else:
        if answer == "yes" and number % 2 != 0:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
        return False
    return True

def main():
    return main_pattern(game, "Answer \"yes\" if the number is even, otherwise answer \"no\".")
