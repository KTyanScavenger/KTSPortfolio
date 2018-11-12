#Parker Dean
#Kyla Ryan
#11/2/17
#Guessing game

import random
import os

#Ask user which game they want to play
def menu():
    print("MENU\n"
          "1.Play Number Guess\n"
          "2.Play Coin Flip\n"
          "3.View Credit\n"
          "4.Quit\n"
          "")
    option=input('What do you want to do: Enter 1, 2, 3, or 4.')
    if option=="1":
        num_guess()
    elif option=="2":
        coin_flip()
    elif option=="3":
        credit()
    elif option=="4":
        quit
    else:
        print("That is not a valid input.")
        menu()

#Define peramaters if they input an invalid number
def guess_num():
    while True:
        g1=input("Guess: ")
        if g1.isdigit():
            g1=int(g1)
            return g1
        else:         
            print("That wasn't a number.")
    
#Define number guessing game. Set the random generator to choose number between 0 and 100.
def num_guess():
    low=0
    high=100
    set_num=random.randint(low,high)
    print("Guess a number between 1 and 100!\n"
          "")
    g1= guess_num()
    if g1 == set_num:
        print("You win!")
        what_now=input("What do you want to do now?\n"
                       "1.Play Again.\n"
                       "2.Back To Menu.\n"
                       ""
                       "Enter 1 or 2."
                       "")
        #Determine if the guess is greater than the randomly chosen number and give the output that it is, or determine if the guess
        #is less than the random number and give the output that it is. If the guess is not the number, go to next guess (g2)
        if what_now=="1":
            num_guess()
        elif what_now=="2":
            menu()
        else:
            print("That is not a valid option.")
            what_now()
    else:
        print("Try again.")
        if g1>=set_num:
            print("Too high! Guess lower!")
        elif g1<=set_num:
            print("Too low! Guess higher!")
        g2=guess_num()
        if g2==set_num:
            print("You win!")
            what_now=input("What do you want to do now?\n"
                       "1.Play Again.\n"
                       "2.Back To Menu.\n"
                       ""
                       "Enter 1 or 2."
                       "")
            if what_now=="1":
                num_guess()
            elif what_now=="2":
                menu()
            else:
                print("That is not a valid option.")
                what_now()
        else:
            #Determine if the guess is greater than the randomly chosen number and give the output that it is, or determine if the guess
        #is less than the random number and give the output that it is. If the guess is not the number, go to next guess (g3)
            print("Try again.")
            if g2>=set_num:
                print("Too high! Guess lower!")
            elif g2<=set_num:
                print("Too low! Guess higher!")
            g3=guess_num()
            if g3==set_num:
                print("You win!")
                what_now=input("What do you want to do now?\n"
                           "1.Play Again.\n"
                           "2.Back To Menu.\n"
                           ""
                           "Enter 1 or 2."
                           "")
                if what_now=="1":
                    num_guess()
                elif what_now=="2":
                    menu()
                else:
                    print("That is not a valid option.")
                    what_now()
            else:
                #Determine if the guess is greater than the randomly chosen number and give the output that it is, or determine if the guess
        #is less than the random number and give the output that it is. If the guess is not the number, go to next guess (g4)
                print("Try again.")
                if g3>=set_num:
                    print("Too high! Guess lower!")
                elif g3<=set_num:
                    print("Too low! Guess higher!")
                g4=guess_num()
                if g4==set_num:
                    print("You win!")
                    what_now=input("What do you want to do now?\n"
                           "1.Play Again.\n"
                           "2.Back To Menu.\n"
                           ""
                           "Enter 1 or 2."
                           "")
                    if what_now=="1":
                        num_guess()
                    elif what_now=="2":
                        menu()
                    else:
                        print("That is not a valid option.")
                        what_now()
                else:
                    #Determine if the guess is greater than the randomly chosen number and give the output that it is, or determine if the guess
        #is less than the random number and give the output that it is. If the guess is not the number, go to next guess (g5)
                    print("Try again.")
                    if g4>=set_num:
                        print("Too high! Guess lower!")
                    elif g4<=set_num:
                        print("Too low! Guess higher!")
                    g5=int(input("Guess: "))
                    if g5==set_num:
                        print("You win!")

                        what_now=input("What do you want to do now?\n"
                                       "1.Play Again.\n"
                                       "2.Back To Menu.\n"
                                       ""
                                       "Enter 1 or 2."
                                       "")
                        if what_now=="1":
                            num_guess()
                        elif what_now=="2":
                            menu()
                        else:
                            print("That is not a valid option.")
                            what_now()
                    else:
                        print("You didn't guess the number in your 5 tries.\n"
                              "The number was,",set_num,".")
                        what_now=input("What do you want to do now?\n"
                                       "1.Play Again.\n"
                                       "2.Back To Menu.\n"
                                       ""
                                       "Enter 1 or 2."
                                       "")
                        if what_now=="1":
                            num_guess()
                        elif what_now=="2":
                            menu()
                        else:
                            print("That is not a valid option.")
                            what_now()

#Define Coin Flip game
def coin_flip():
    flips = 0
    heads = 0
    tails = 0
    
    
    coin_guess = input("If I flip a coin 100 times, which do you think will be higher? Heads or Tails: ")
    #Determine if the random number of flips is heads or tails. Add 1 to flips, and heads, or flips and tails. 
    while flips < 100:
        if random.randint(1,2) == 1:
            print("heads")
            heads += 1
        else:
            print("tails")
            tails += 1
        flips += 1
    if coin_guess.lower() == "heads":
        print("So you guessed Heads")
        print("There were" , heads , "Heads, and there were" , tails , "tails")
        if heads > tails:
            print("You Win!")
            #If the number of heads is greater than 50, show how many there are. If the user guessed heads, they won. Vise verse with tails.
        else:
            print("You Lose!")
    elif coin_guess.lower() == "tails":
        print("So you guessed Heads")
        print("There were" , tails , "Tails, and" , heads , "Heads")
        if heads < tails:
            print("You Win!")
        else:
            print("You Lose!")
    input("")

#Define Credits
def credit():
    print("Directed by: Parker Dean and Kyla Ryan")
    print("Written by: Parker Dean and Kyla Ryan")
    print("Inspired by: Eric Broadbent")
    input("")

#Define escape sequence
def quit():
    os._exit(0)

menu()
    
