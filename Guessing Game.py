import random

print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100")


def random_number():
    number = random.randint(1, 100)
    return number


def again():
    h = True
    while h:
        another1 = input("Do you want to play again? y or n: ")
        if another1 != "y" and another1 != "n":
            print("Please input y and n only!")
        elif another1 == "y":
            play()
        elif another1 == "n":
            print("THANK YOU FOR PLAYING THE GAME!")
            h = False


def guess_number():
    guess = int(input("Make a guess: "))
    return guess


def main_easy(number):
    a = True
    easy_lives = 10
    while a:
        print(f"You have {easy_lives} attemps remaining to guess the number")
        guess = guess_number()
        if guess < number:
            easy_lives -= 1
            print("Too Low.")
            if easy_lives == 0:
                print(f"You've run out of guesses, you lose, The number is {number}")
                a = False
            else:
                print("Guess again.")

        elif guess > number:
            easy_lives -= 1
            print("Too High")
            if easy_lives == 0:
                print(f"You've run out of guesses, you lose, The number is {number}")
                a = False
            else:
                print("Guess again.")

        elif guess == number:
            print(f"CONGRATULATION YOU'VE GUESSED THE NUMBER, The number is {number}")
            a = False


def main_hard(number):
    b = True
    hard_lives = 5
    while b:

        print(f"You have {hard_lives} attemps remaining to guess the number")
        guess = guess_number()
        if guess < number:
            hard_lives -= 1
            print("Too Low.")
            if hard_lives == 0:
                print(f"You've run out of guesses, you lose, The number is {number}")
                b = False
            else:
                print("Guess again.")

        elif guess > number:
            lives -= 1
            print("Too High")
            if hard_lives == 0:
                print(f"You've run out of guesses, you lose, The number is {number}")
                b = False
            else:
                print("Guess again.")


        elif guess == number:
            print(f"CONGRATULATION YOU'VE GUESSED THE NUMBER, The number is {number}")
            b = False


def play():
    play = True
    number = random_number()
    while play:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty != "easy" and difficulty != "hard":
            print("Please input easy and hard only!")
        elif difficulty == "easy":
            main_easy(number)
            play = False
        elif difficulty == "hard":
            main_hard(number)
            play = False


play()
again()









