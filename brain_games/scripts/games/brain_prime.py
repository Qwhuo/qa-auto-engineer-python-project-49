import random
import prompt
from brain_games.scripts.utils.main_pattern import main_pattern


def game():
    def is_prime(n):
        is_pr = True
        for i in range(2, round(n**0.5+1)):
            if n % i == 0:
                is_pr = False
                break
        return is_pr
    number = random.randint(1, 100)
    print(f"Question: {number}")
    answer = prompt.string("Your answer: ")
    correct_answer = "yes" if is_prime(number) else "no"
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False
    return True

def main():
    return main_pattern(game, "Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
