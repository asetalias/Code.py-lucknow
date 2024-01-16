import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#Importing  the logo from hangman_art.py
from hangman_art import logo
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while '_' in display:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(f"Remaining lives: {lives}")
        
        if lives == 0:
            print("You lose.")
            break

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
    #Importing the stages from hangman_art.py 
    from hangman_art import stages
    print(stages[lives])
if '_' not in display:
  print("Contragulations!, You won.")
else:
  print(f"The right answer is: {chosen_word}")