from brain_games.cli import welcome_user


def main_pattern(game, entry_rule):
    cnt = 0
    name = welcome_user()
    print(entry_rule)
    while True:
        g = game()
        if not g:
            print(f"Let's try again, {name}!")
            return 0
        cnt += 1
        if cnt == 3:
            print(f"Congratulations, {name}!")
            return 1