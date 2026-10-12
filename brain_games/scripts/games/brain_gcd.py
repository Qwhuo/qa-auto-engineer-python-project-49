import random
import prompt
from brain_games.scripts.utils.main_pattern import main_pattern



def game():
    def gcd(a, b):
        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0:
                return i
        return 1
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = gcd(num1, num2)
    print(f"Question: {num1} {num2}")
    answer = prompt.integer("Your answer: ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False
    return True

def main():
    return main_pattern(game, "Find the greatest common divisor of given numbers.")