#import from random, * imports all the methods from the random module
from random import *
#card is going to be formatted and returned.
#will be called in the class 'deck'.
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        #why is it returning a tuple if i format it this way?
        #return (self.value), (self.suit) 
        return str(self.value) + str(self.suit)
 
    #this method will print the number and suit of the card formatted.
    def show_formatted_card(self):
        print((self.value), (self.suit))

class Deck:
    def __init__(self):
        self.deck_of_cards = []
        self.build_()

    #For loop will iterate through every suit and avery number. Ex: 1s,1h,1d,1c. 
    #Every value and suit will be used as parameters for the "Card" class. 
    #An instance of that class will be created, and added to the "deck_of_cards" list. 
    def build_(self):
        symbols = {"Spades":"♦", "Hearts":"♥","Diamonds":"♦", "Clubs":"♣"}
        for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
            for value in range(1, 14):
                self.deck_of_cards.append(Card(symbols[suit], value))
    
    #Get the length of the deck, to get the index, index will start at the end, going to 0, by one.
    #"random_card" will be an index, randint will return a number from 0 to # being looped, sp from 0 to index.
    #Changing the value of the random card to the value of the card at that index, this is what shuffles the deck.
    def shuffle_deck_of_cards(self):
        for indexes in range (len(self.deck_of_cards)-1,0,-1): #Fisher-Yates shuffle
            random_index = randint(0 , indexes) 
            self.deck_of_cards[indexes], self.deck_of_cards[random_index] = self.deck_of_cards[random_index], self.deck_of_cards[indexes]
    
    def show_cards_in_deck(self):
        for card_in_deck in (self.deck_of_cards):
            card_in_deck.show_formatted_card()
            
    #Selecting a random card from the deck, 
    #Remember you are selecting an instance of Card, you still have to call it's method.
    #When calling this method, save it as a variable, and call the method from the class 'Card'.
    def draw_one_card(self,):
        return self.deck_of_cards.pop()
    
class Player:
    #Array will hold the cards that the player has.
    def __init__(self,):
        self.hand = []
        self.value = 0
    #Pass Deck object as a parameter.
    #Add the "card" to the "hand" array, using the deck class. 
    def draw(self, card):
        self.hand.append(card.draw_one_card())
    
    def show_cards_in_hand(self):
        for card in self.hand:
            card.show_formatted_card()
    
def show_some(player, dealer):
    print("\nDealer's Hand: ")
    print(" <card hidden>")
    print("", dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
        

class Hand:
    pass


deck_instance = Deck()
deck_instance.shuffle_deck_of_cards()

player_instance = Player()
player_instance.draw(deck_instance)
player_instance.show_cards_in_hand()

print(Card(1,2))





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

