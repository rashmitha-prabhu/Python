import art
import random

print(art.logo)
num = random.randint(1, 100)


def game(g):
    print(f"\nREMAINING LIVES : {g}\n")
    n = int(input("Make a guess : "))
    if n > num:
        print("Too HIGH")
    elif n < num:
        print("Too LOW")
    else:
        print("You guessed it! Congratulations!")
        exit()


diff = input("Choose Difficulty : \nEASY (10 chances) \t\t HARD(10 chances) : ")

print("\nI am thinking of a number between 1 and 100.")
print("Can You guess it?\n")

if diff.lower() == "easy":
    guess = 10
    while guess > 0:
        game(guess)
        guess -= 1
    print(f"\nYou ran out of chances.\nThe number on my mind was {num}\nBetter luck next time!")

if diff.lower() == "hard":
    guess = 5
    while guess >= 0:
        game(guess)
        guess -= 1
    print(f"\nYou ran out of chances.\nThe number on my mind was {num}\nBetter luck next time!")

