from random import randint
print("This is a game where the computer chooses a number between 1 and 9 (including 1 and 9) and you have to guess the number. (Enter exit to close the game.)")

def num_guess():
    while True:
        number, guesses = randint(1,9), 0
        while True:
            user = input("Please enter your guess: ")
            if user.lower() == "exit":
                quit()
            try:
                user = int(user)
            except:
                print("That was not a number.")
                continue
            guesses += 1
            if user == number:
                print("Congratulations! You guessed the number was {} after {} guesses.".format(number, guesses))
                break
            print("Guess too low." if user<number else "Guess too high.")
            continue
num_guess()
