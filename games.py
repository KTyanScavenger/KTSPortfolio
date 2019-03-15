import cards

def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    ANSWER = ("y", "n", "yes", "YES", "Yes", "No", "NO", "Y", "N")
    while response not in ANSWER:
        response = input(question).lower()

    return response
def ask_number(question,low,high):
    """Ask for a number"""
    response="9999"
    while True:
        # try:
        #     response = int(input(question))
        #     if response in range(low, high):
        #         return response
        #     else:
        #         print("that's out of range")
        if response.isdigit():
            if int(response) in range(low,high):
                break
            else:
                response=input(question)
        else:
            print("You must enter a number. ")
            response=input(question)
    return int(response)

def switch_turn(num_players, turn):
    turn = turn
    if turn<num_players-1:
        turn += 1
        return turn

    else:
        turn=0
        return turn

def winner_grats():
    print("You win! Congratualations!")

def create_player():
    for i in range(num_players):
        print("Player ",i+1)
    while True:
        name=input("Enter your name: ")
        name=name.title()
        if name=="":
            print("That is an invalid name. Try again.")
        else:
            break
    player=Player(name,i+1)
    players.append(player)

def roll(self):
    die1 = random.randint(1, 6)
    print("You rolled a", die1)
    roll = die1
    return roll


def add_to_score(score, points):
    """Adds points to an earned score"""
    new_score=score
    score+=points
    return new_score

class Player(object):
    def __init__(self, name,score=0):
        self.name=name
        self.score=score()
    def __str__(self):
        rep=self.name
        rep=rep+""+str(self.score)
        return rep


if __name__=="__main__":
    print("You ran the module directly (and didn't import it)")
    input("\n\nPress the enter key to exit.")
