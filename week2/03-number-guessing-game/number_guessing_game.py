import random


def play_game(target=None, max_attempts=None):
    def exit():
        try_again = input(
            "Would you like to try again (y/n): ").lower().strip()
        if try_again == "y":
            return True
        else:
            print("Goodbyee!!!")
            return False
    if target == None:
        target_num = random.randint(1, 100)
    else:
        target_num = target
    correct = False
    num_of_attempt = 0
    while not correct:
        try:
            guessed_num = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("invalid input. enter a whole number between 1 and 100")
            continue
        if guessed_num < 1 or guessed_num > 100:
            print("invalid input. enter a whole number between 1 and 100")
        elif guessed_num > target_num:
            num_of_attempt += 1
            print("too high")
        elif guessed_num < target_num:
            num_of_attempt += 1
            print("too low")
        else:
            num_of_attempt += 1
            print(f"correct! you got it in {num_of_attempt} guesses")
            if exit():
                play_game()
            else:
                correct = True
        if max_attempts == None:
            continue
        elif max_attempts == num_of_attempt and guessed_num != target_num:
            print(f"You are out of guess, the anser is {target_num}")
            if exit():
                play_game()
            else:
                correct = True


# Do not modify below this line
if __name__ == "__main__":
    play_game()
