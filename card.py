#import from random, * imports all the methods from the random module
from random import *
#card is going to be formatted and returned.
#will be called in the class 'deck'.


values_dict = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13}
symbols = {"Spades":"♦", "Hearts":"♥","Diamonds":"♦", "Clubs":"♣"}
values = ["Ace", "2", "3", "4", "5", "6", "7", "9", "10", "Jack", "Queen", "King"]


class Card:

    #this class will be used to create a card object.
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    #this method will print the number and suit of the card formatted.
    def show_formatted_card(self):
        print((self.value), (self.suit))

class Deck:
    def __init__(self):
        self.deck_of_cards = []
        self.build_()

    #For loop will iterate through every suit and every number. Ex: 1s,1h,1d,1c. 
    #Every value and suit will be used as parameters for the "Card" class. 
    #An instance of that class will be created, and added to the "deck_of_cards" list. 
    def build_(self):
        for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for value in ["Ace", "2", "3", "4", "5", "6", "7", "9", "10", "Jack", "Queen", "King"]:
                self.deck_of_cards.append(Card(symbols[suit], values_dict))
    
    #Get the length of the deck, to get the index, index will start at the end, going to 0, by one.
    #"random_card" will be an index, randint will return a number from 0 to # being looped, sp from 0 to index.
    #Changing the value of the random card to the value of the card at that index, this is what shuffles the deck.
    
    def shuffle_deck_of_cards(self):
        for indexes in range (len(self.deck_of_cards)-1,0,-1): #Fisher-Yates shuffle
            random_index = randint(0 , indexes) 
            self.deck_of_cards[indexes], self.deck_of_cards[random_index] = self.deck_of_cards[random_index], self.deck_of_cards[indexes]

    def shuffle(self):
        shuffle((self.deck_of_cards))

    #Selecting a random card from the deck, 
    #Remember you are selecting an instance of Card, you still have to call it's method.
    #When calling this method, save it as a variable, and call the method from the class 'Card'.
    def draw_one_card(self,):
        return self.deck_of_cards.pop()
    
class Player:
    #Array will hold the cards that the player has.
    #Set value for card points and ace count. 
    def __init__(self,):
        self.hand = []
        self.value = 0
        ace = 0
        self.bet = 0
        self.total = 100

    #Pass Deck object as a parameter.
    #Add the "card" to the "hand" array, using the deck class. 
    #Add the value of the card to the "value" variable, and add 1 to the "ace" variable if pulled. 
    def draw(self, card):
        self.hand.append(card)
        self.value += values_dict[card.value]
        if card.values == 'ace':
            self.aces+=1
    #Since ace can be written as 1 or 11, we need to check he value of hand and decide what ace will be worth.
    def adjust_value_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 


########################################################################

#If the player wins bet the bet will be added to the "total" variable.
def win_bet(self):
        self.total += self.bet

#If the player loses bet the bet will be subtracted to the "total" variable.
def lose_bet(self):
        self.total -= self.bet


#When using this function, you have to pass "Deck" instance as a parameter.
def show_cards_in_hand(self):
        for card in self.hand:
            card.show_formatted_card()

def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)






deck_instance = Deck()
deck_instance.shuffle()

player_instance = Player()
player_instance.draw(deck_instance)
player_instance.draw(deck_instance)
player_instance.draw(deck_instance)
player_instance.show_cards_in_hand()




card_instance = Card('Spades', 1)
#card_instance.show_formatted_card()
#deck_instance.show_cards_in_deck()
#deck_instance.draw_card()
#deck_instance.shuffle_deck_of_cards()
#deck_instance.show_cards_in_deck()
#deck_instance.draw_card()
#deck_instance.draw_one_card()
#one_card = deck_instance.draw_one_card()
#one_card.show_formatted_card()
