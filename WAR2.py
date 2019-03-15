# imports
import cards, games
#Kyla, Bridger, Sabastian, Jacob
#Period:1/2

###############################################################
# Classes

class War_Card(cards.Card):
    @property
    def value(self):
        if self.is_face_up:
            v = War_Card.RANKS.index(self.rank) + 1
        else:
            v = None
        return v


class War_Deck(cards.Deck):

    def populate(self):
        for suit in War_Card.SUITS:
            for rank in War_Card.RANKS:
                self.cards.append(War_Card(rank, suit,face_up=True))


class War_Hand(cards.Hand):

    def __init__(self, name):
        super(War_Hand, self).__init__()
        self.name = name


class War_Player(War_Hand):

    def play(self, hand):
        top_card = self.cards[0]
        self.give(top_card, hand)

    def lose(self):
        print(self.name, "loses.")
        self.cards.clear()

    def win(self):
        print(self.name, "wins.")

    def war(self,pot):
        for i in range(3):
            self.give(self.cards[0],pot)

class War_Pot(War_Hand):
    def __init__(self, players):
        super(War_Hand, self).__init__()
        self.players = players



    @property
    def check_winner_war(self):
        if self.cards[8].value > self.cards[9].value:
            winner = 0
        elif self.cards[8].value < self.cards[9].value:
            winner = 1
        else:
            winner = "War!"
        return winner

    def check_winner(self):
        if self.cards[0].value > self.cards[1].value:
            winner = 0
        elif self.cards[0].value < self.cards[1].value:
            winner = 1
        else:
            winner = None
        return winner

    def give_pot(self,winner):
        for i in range(len(self.cards)):
            self.give(self.cards[0], self.players[winner])
    def to_pot(self,pot):
        for i in range(len(self.cards)):
            self.give(self.cards[0],pot)


class War_Field(War_Hand):
    @property
    def check_winner(self):
        if self.cards[0].value > self.cards[1].value:
            winner = 0
        elif self.cards[0].value < self.cards[1].value:
            winner = 1
        else:
            winner = "WAR!"
        return winner
    def to_pot(self,pot):
        for i in range(len(self.cards)):
            self.give(self.cards[0],pot)


class War_Game(object):
    def __init__(self, names):

        self.players = []
        for name in names:
            player = War_Player(name)
            self.players.append(player)

        self.pot = War_Pot(self.players)
        self.field = War_Pot(self.players)
        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def game_over(self):
        for player in self.players:
            x = len(player.cards)
            print(player.name, x)
            if x <= 0:
                return True
        return False

    def play(self):
        game_over = None
        self.deck.deal(self.players, per_hand=26)
        while not game_over:
            for player in self.players:
                player.play(self.field)

            winner = self.field.check_winner()
            print(self.players[0].name + " ", self.field, self.players[1].name)
            self.field.to_pot(self.pot)
            if winner == 0 or winner == 1:#removed the elif and made it a compound function
                self.pot.give_pot(winner)
                print(self.players[winner].name, "Wins")


            else:
                p1len = len(self.players[0].cards)
                p2len = len(self.players[1].cards)
                if p1len >= 4 and p2len >= 4:
                    print("WAR!!!!!!!")
                    self.players[0].war(self.pot)
                    self.players[1].war(self.pot)
                    print(self.pot)

                else:
                    if p1len <= 4:
                        self.players[0].lose()
                    else:
                        self.players[1].lose()



            input("press enter to play")

            game_over = self.game_over()

def main():
    want_to_play=input("Do you want to play a game? (yes/no)")
    if want_to_play.lower() == "yes":
        play_one=input("Enter your name: ")
        play_two=input("Enter your name: ")
        names = []
        names.append(play_one)
        names.append(play_two)

        game = War_Game(names)
        game.play()
    else:
        print("Bye")

main()
#Credit to Broadbent