import random
class Card(object):
    """A playing card.
    this class will build a single card
    to build a card call Card() and pass in a rank and suit
    card1 = Card(rank = "A", suit = "s"
    """
    RANKS = ["A", "2", "3", "4", "5", "6","7","8","9","10","J", "Q", "K"]
    SUITS = ["♣","♦","♥","♠"]

    def __init__(self, rank, suit, face_up):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up
 #       self.face_up = True

 #   def flip(self):
 #       self.face_up = not self.face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep="XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(object):
    """A hand of playing cards
    also can empty a hand my_hand.clear() print(my_hand)
    and give my_hand.give(my_hand.cards[0], your_hand)print(my_hand) print(your_hand)
    and add cards to a hand for i in range(5): my_hand.add(deck.pop())
    """
    def __init__(self):
        self.cards=[]
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card)+" "
        else:
            rep="<empty>"
        return rep



    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """This populates the deck and also passes out hands with unlimited amount of cards"""

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card=Card(rank,suit,True)
                self.add(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue to deal. Out of Cards")

if __name__=="__main__":
    print("You ran the module directly (and didn't import it)")
    input("\n\nPress the enter key to exit.")





    # deck=Deck()
    # deck.populate()
    # deck.shuffle()
    # print(deck)
    # print(len(deck.cards), "cards left in the deck.")
    #
    # my_hand=Hand()
    # other_hand=Hand()
    # hands = []
    # hands.append(my_hand)
    # hands.append(other_hand)
    # deck.deal(hands, 5)
    # print(deck)
    # print(len(deck.cards), "cards left in the deck.")
    # for card in my_hand.cards:
    #     card.flip()
    #     print("My hand:", my_hand)
    #     print("Are you feeling lucky?")
    # for card in other_hand.cards:
    #     card.flip()
    #     print("Opponent's hand:", other_hand)


# main()
#my_hand = Hand()
#your_hand = Hand()
#deck = []
#for i in range(10):
#    card = Card(rank = random.choice(Card.RANKS), suit = random.choice(Card.SUITS))
#    deck.append(card)

#for i in range(5):
#    my_hand.add(deck.pop())
#    your_hand.add(deck.pop())
#print(my_hand)
#print(your_hand)

#my_hand.give(my_hand.cards[0], your_hand)
#print(my_hand)
#print(your_hand)

#my_hand.clear()
#your_hand.clear()

#print(my_hand)
#print(your_hand)