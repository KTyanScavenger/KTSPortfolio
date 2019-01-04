#Kyla Ryan
#1/19
#Trivia Challenge
#Trivia Game that reads a plain text file

import sys
##NAME THE FILE NAME
##ASSIGN MODE (PERMISSIONS TO THE FILE)
def open_file(file_name,mode):
    """OPEN A FILE"""
    try:
        the_file=open(file_name,mode)
    except IOError as e:
        print("Unable to open file",
              file_name,"Ending the program.\n",e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file



def next_line(the_file):
    """RETURN NEXT LINE FROM THE TRIVIA FILE, FORMATTED"""
    line=the_file.readline()
    line=line.replace("/","\n")
    return line
##just a test
##file_name="test.txt"
##the_file=open_file(file_name,"r")
##line=next_line(the_file)
##print(line)
def next_block(the_file):
    """  this moves to the next text block"""
    category=next_line(the_file)
    question=next_line(the_file)
    answer=[]
    for i in range(4):
        answer.append(next_line(the_file))
    correct=next_line(the_file)
    if correct:
        correct=correct[0]
    explanation=next_line(the_file)
    return category, question, answer, correct, explanation


def welcome(title):
    """"welcome the player to their game"""
    print("\t\tWelcome to Trivia Game!\n")
    print("\t\t",title,"\n")
        
##just a test    
##the_file=open_file("test.txt","r")
##title=next_line(the_file)
##category, question, answers, explanation=next_block(the_file)
##print(category)
##print(question)
##print(answers)
##print(explanation)
##print(title)
        
def main():
    file_name="test.txt"
    mode="r"
    the_file=open_file(file_name,mode)
    open_file(file_name, mode)
    title=next_line(the_file)
    welcome(title)
    score=0
    category, question, answer, correct, explanation=next_block(the_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(i+1,":",answer[i])
        user_answer=input("What is the correct answer?")
        if user_answer in correct:
            print("Congratulations! You chose the correct answer! ",end=" ")
            score+=1
        else:
            print("Sorry that answer was incorrect.\n")
        print(explanation)
        print(score)
        category, question, answer, correct, explanation=next_block(the_file)
    the_file.close()
    print("The game has been completed. Well done.")
    print("Your final score was: ",score)
    print("Press enter key to close.")
    sys.exit()


main()
