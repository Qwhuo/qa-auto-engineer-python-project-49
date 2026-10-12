import prompt



def welcome_user():
    print("Welcome to Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


if __name__ == '__main__':
    welcome_user()