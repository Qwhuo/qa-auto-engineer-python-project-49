import random
import prompt
from brain_games.scripts.utils.main_pattern import main_pattern


def game():
    def add(n1, n2):
        return n1 + n2
    def sub(n1, n2):
        return n1 - n2
    def mul(n1, n2):
        return n1 * n2
    operators = {"+": add, "-": sub, "*": mul}
    selected_operator = random.choice(["+", "-", "*"])
    num1 = random.randint(-10, 10)
    num2 = random.randint(-10, 10) if selected_operator != '-' else abs(random.randint(-10, 10))
    correct_answer = operators[selected_operator](num1, num2)
    print(f"Question: {num1} {selected_operator} {num2}")
    answer = prompt.integer("Your answer: ")
    if answer != correct_answer:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False
    else:
        print("Correct!")
        return True

def main():
    return main_pattern(game, "What is the result of the expression?")

