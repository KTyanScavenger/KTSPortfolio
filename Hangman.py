#Hangman Game
#Kyla Ryan
#11/26/18
#The classic game of Hangman. the computer picks a random word
#and the player wrong to guess it, one letter at a time. If the player
#can't guess the word in time, the little stick figure gets hung.

import random

HANGMAN=(
"""
       _______
     |/      |
     |
     |  
     |       
     |  
     | _____
"""
    ,
"""
       _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
     |____
"""
,
"""
       _______
     |/      |
     |      (_)
     |        |
     |       
     |  
     |
     |____
"""
,
"""
       _______
     |/      |
     |      (_)
     |        |/
     |       
     |      
     |
     |____
"""
,
"""
       _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
     |____
"""
,
"""
       _______
     |/      |
     |      (_)
     |      \|/
     |        |
     |      
     |
     |____
"""
,
"""
       _______
     |/      |
     |      (_)
     |      \|/
     |        |
     |      / 
     |
     |____
"""
,
"""
       _______
     |/      |
     |      (_)
     |      \|/
     |        |
     |      / \
     |
     |___

""")
##We need to place each hangman ascii art into a tupple so it cannot be changed/added, yet holds it as a list would. 

MAX_WRONG=len(HANGMAN)-1
#Max wrong gives the number of items in the tupple and subtracts(goes to the next one) when a wrong answer was entered. 
##the words are the right answers
WORDS=("pop","index","tuple","num","list","append","def","input","variable","print")
#initialize variables
word=random.choice(WORDS) #word to be guessed
so_far="-"*len(word) #print dash for each letter in word
wrong=0 # # of wrong guesses
used=[] #letters already guessed
#Me must append letters which were already guessed to a list, so we cannot use them again. 
print("WELCOME TO HANGMAN")
print("Good luck!")
#Welcome the user/player
def game(wrong,MAX_WRONG,word,so_far,used):
    while wrong< MAX_WRONG and so_far!=word:
#While the max wrong guesses are greater than the wrong guesses, the user may guess a letter. 
        print(HANGMAN[wrong])
        print("\nYou've used the following letters:\n",used)
        print("\nSo far, the word is:\n", so_far)
        guess=input("\n\nEnter your guess: ")
        guess=guess.lower()
        #Presents what has been guessed. 
        while guess in used:
            print("You've already guessed the letter: ",guess)
            guess=input("Enter your guess: ")
            guess=guess.lower()
        used.append(guess)
    if guess in word:
       #This checks if the input from the user is in the word. 
        print("\nYes!",guess,"is in the word!")
        new=""
       #If it is in the word, the program removes the placeholder in the place the character is in and, in turn, places the letter there.
        for i in range(len(word)):
            if guess==word[i]:
                new+=guess
            else:
                new+=so_far[i]
        so_far=new
    else:
        print("\nSorry,",guess,"isn't in the word.")
        wrong+=1
        #Tells if the user win or loses depending on if the max number of wrong guesses has been reached. 
        if wrong==MAX_WRONG:
            winlose(wrong,word)
            
def winlose(wrong,word):
    if wrong==MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nYou've been hung!")
    else:
        print("\nYou guessed it!")
        print("\nThe word was", word)
        input("\n\nPress the enter key to exit.")
#Presents a win/lose screen
def main(wrong,MAX_WRONG,word,so_far,used):
    game(wrong,MAX_WRONG,word,so_far,used)
    winlose(wrong,word)
#Main function which calls the others. 

main(wrong,MAX_WRONG,word,so_far,used)

#Begins the program
