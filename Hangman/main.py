from os import wait
import random
import hangman_art
import hangman_words
import subprocess as sp


def clear():
    tmp = sp.call('clear', shell=True)
    print(hangman_art.logo+"\n\n")


word_list = hangman_words.word_list

while True:
    tmp = sp.call('clear', shell=True)
    print(hangman_art.logo+"\n\n")
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    display = []
    entered = []

    for _ in range(word_length):
        display += "_"

    n = word_length

    while n > word_length-2:
        i = random.randint(0, word_length-1)
        if chosen_word[i] not in display:
            letter = chosen_word[i]
            for i in range(word_length):
                if chosen_word[i] == letter:
                    display[i] = letter
                    n -= 1

    while not end_of_game:
        print(f"{' '.join(display)}") 
        print(hangman_art.stages[lives])
        print(f"Already entered : {entered}")
        print(f"Lives Remaining : {lives}")
        guess = input("\nGuess a letter: ").lower()	

        if guess in entered:
            clear()
            continue

        else:
            entered += guess

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            lives -= 1

            if lives == 0:
                end_of_game = True
                clear()
                print(f"{' '.join(display)}") 
                print(hangman_art.stages[lives])
                print(f"\nThe word was {chosen_word}")
                print("\nYou Lose")
                break

        if "_" not in display:
            end_of_game = True
            clear()
            print(f"{' '.join(display)}") 
            print(hangman_art.stages[lives])
            print("\nYou win.")
        else:
            clear()

    choice = input("\nTry Again? (y/n) : ")
    if choice.lower() == 'n':
        print("See ya Again!")
        exit()
