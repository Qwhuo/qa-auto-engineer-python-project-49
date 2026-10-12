import random
import prompt
from brain_games.scripts.utils.main_pattern import main_pattern



def game():
    sequence = []
    rand_start = random.randint(-100, 100)
    rand_k = random.randint(-10, 10)
    def rec(curr):
        sequence.append(curr)
        if len(sequence) == 10:
            return
        rec(curr + rand_k)
    rec(rand_start)
    missing_pos = random.randint(0, len(sequence) - 1)
    correct_answer = sequence[missing_pos]
    print(f"Question: ", end="")
    for i in range(len(sequence)):
        if i == missing_pos:
            print(".. ", end="")
        else:
            print(f"{sequence[i]} ", end="")
    answer = prompt.integer("\nYour answer: ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False
    return True

def main():
    return main_pattern(game, "What number is missing in the progression?")