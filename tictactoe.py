#display instructions
#ask for user
#display grid/board
#While nobody has one, it is not a tie
#if it's the user's turn, get input from user
#update the board
# else calculate computer movement board's play board switch turn
#win lose tie
X="X"
O="O"
EMPTY=" "
TIE="TIE"
NUM_SQUARES=9
board="""
 0 | 1 | 2
 --------
 3 | 4 | 5
 --------
 6 | 7 | 8
 """
#PResents the board and possible plays. 
YES=["yes","Yes","Y","y"]
NO=["No","N","n","no"]
#Possible input for the user
def display_instructions(board):
    print("Hi player. Do you want to play a game???")
    print("Here are your instructions:\n"
          "Pick a marker. Try to pick positions on your board to get three in a row!\n"
          "You get three in a row, you win! If the computer does, the computer wins!\n"
          "There is a situation where neither win, in that case you tie!\n"
          "Enter a number, 1-8 to pick your position!\n"
          "Good luck!")
    #displays the instructions to the user, telling what they can do and how they play
    print(board)
    print("Computer: YOU'LL NEVER BEAT ME, PUNY HUMAN!")
 ##GIVES THE COMPUTER A VERY EGOTISTICAL PERSONALITY >:D



def ask_yes_no(question):
    """Ask a yes or no question"""
    response=None
    ANSWER=("y","n","yes","YES","Yes","No","NO","Y","N")
    while response not in ANSWER:
        response=input(question).lower()
        #Presents a yes or no question and gives the possible responses the user may give. If the response is not in the response list, tell the user; 
    
    return response



##def ask_number(question,low,high):
##    """Ask for a number wihtin a range"""
##    response=None
##    while response not in range(low,high):
##        response=input(question)
##        return int(response)
##ask_number("Enter a number within 1-10",1,11)

def ask_number(question,low,high):
    """Ask for a number"""
    response="9999"
    while True:
     #ASks for which position the user would like to place their move
        if response.isdigit():
            if int(response) in range(low,high):
                break
            else:
                response=input(question)
        else:
            print("You must enter a number. ")
            response=input(question)
    return int(response)



def pieces():
    """DETERMINE IF PLAYER GOES FIRST"""
    go_first=ask_yes_no("Do you want to go first? ")
    if go_first=="Y" or go_first=="yes" or go_first=="YES" or go_first=="Yes"or go_first=="y":
        print("\nThen take the first move. You will need it.")
        human=X
        computer=O
        #Asigns place values for the computer and user
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        computer=X
        human=O
    return computer, human
##com,human=pieces()
##print(com)
##print(human)
        
def new_board():
    """Create a new board"""
    board=[]
    for squares in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
#NEW GAME

def display_board(board):
    """Display game board on screen"""
    print("\n\t",board[0],"|",board[1],"|",board[2])
    print("\t","------")
    print("\n\t",board[3],"|",board[4],"|",board[5])
    print("\t","------")
    print("\n\t",board[6],"|",board[7],"|",board[8],"\n")

#This is the playable board

def legal_moves(board):
    moves_list=[]
    for square in range(len(board)):
        if board[square]==EMPTY:
            moves_list.append(square)
    return moves_list
#Determines if the place the user would like to play (or the computer), is playable. 


def the_winner(board):
    """"Determine the winner"""
    WAYS_TO_WIN=((0,1,2),
    (3,4,5),
    (6,7,8),
    (0,3,6),
    (2,5,8),
    (1,4,7),
    (0,4,8),
    (2,4,6))
   #Positional values that allow the player or computer to win
    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]] !=EMPTY:
            winner=board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None
 #If there are no more playable moves, the players end in a tie. 
#print(winner)


def human_move(board,human):
    legal=legal_moves(board)
    move=None
    while move not in legal:
        move=ask_number("Where do you want to play? (0-8) ", 0,NUM_SQUARES)
        if move not in legal:
            print("Computer: YOU SHALL NEVER DEFEAT ME WITH THOSE PETTY MOVES! TRY AGAIN!")
        return move

#Defines the legal moves for a user to play. Asks the user where they would like to play. 
#Determines if the move is in a list of possible moves. 


def next_turn(turn):
    """Switch Turns"""
    if turn ==X:
        return O
    else:
        return X
#Switches the turns from the player to the computer and vise verse

def congrat_winner(the_winner,computer,human):
    if the_winner!=TIE:
        print("The winner is ", the_winner)
    else:
        print("It's a tie!")
        if the_winner==computer:
            print("Computer: I REMAIN VICTORIOUS! BASK IN MY GLORY!")
        elif the_winner==human:
            print("Computer: I... I can't believe you beat me.... YOU MUST HAVE CHEATED!")
        elif the_winner==TIE:
            print("It's a tie!")
            print("Computer: ALAS, I REMAIN UNDEFEATED! You put up a good fight, but you still LOST!")
       #The computer responses to the human winning, itself winning, or a tie. 
       
    print("\n\n\tGAME OVER")


def computer_move(board,computer,human):
    """Make computer move"""
    #make a copy of the board
    board=board[:]
    #best positions to have, in order
    BEST_MOVES=(4,0,2,6,8,1,3,5,7)
    print("Computer: I'll play ", end="")
    #if computer can win, take the move
    for move in legal_moves(board):
        board[move]=computer
        if the_winner(board)==computer:
            print(move)
            return move
                  #done checking this move, undo it
        board[move]=EMPTY

                  #if human can win, block it
    for move in legal_moves(board):
        board[move]=human
        if the_winner(board)==human:
            print(move)
            return move
            #done checking this move, undo it
        board[move]=EMPTY
        #since no one can win, pick next best square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
#This is the computer determining where it can play, and which moves would best ensure a win. 


def main(board):
         #Main function calls to the others to perform their functions in order that the main presents.        
        display_instructions(board)
        computer,human=pieces()
        turn=X
        board=new_board()
        display_board(board)
        while not the_winner(board):
            if turn==human:
               move = human_move(board,human)
               board[move]=human
            else:
                move=computer_move(board,computer,human)
                board[move]=computer
            turn= next_turn(turn)
            display_board(board)
        winner=the_winner(board)
        congrat_winner(winner,computer,human)
                

main(main)
#call main function                
        

            
