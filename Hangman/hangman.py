import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo+"\n\n")

display = []
entered=[]

for _ in range(word_length):
    display += "_"

n = round(word_length/4)

while n >= 0:
    i = random.randint(0,word_length-1)
    if chosen_word[i] not in display:
        letter = chosen_word[i]
        for i in range(word_length):
            if chosen_word[i]==letter:
                display[i]=letter
                n-=1

print(f"{' '.join(display)}") 

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()	

    if guess in entered:
        print(f"\nAlready Entered. Choose again\n")
        continue

    else:
        entered+=guess

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"\nUh-Oh! {guess} doesnt occur in the word. You now have {lives} lives left")
        if lives == 0:
            end_of_game = True
            print(f"\n\nThe word was {chosen_word}")
            print("\nYou Lose")          

    print(f"{' '.join(display)}")    

    print(hangman_art.stages[lives])

    if "_" not in display:
        end_of_game = True
        print("\n\nYou win.")