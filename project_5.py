#Python Blackjack
#For this project you will make a Blackjack game using Python. 
#Click here to familiarize yourself with the the rules of the game. 
#You won't be implementing every rule "down to the letter" with the game, 
#but we will doing a simpler version of the game. 
#This assignment will be given to further test your knowledge on object-oriented programming concepts.

#Rules:
#1. The game will have two players: the Dealer and the Player. 
#The game will start off with a deck of 52 cards. 
#The 52 cards will consist of 4 different suits: Clubs, Diamonds, Hearts and Spades. 
#For each suit, there will be cards numbered 1 through 13.
#Note: No wildcards will be used in the program

#2. When the game begins, the dealer will shuffle the deck of cards, making them randomized.
#After the dealer shuffles, it will deal the player 2 cards and will deal itself 2 cards from. 
#The Player should be able to see both of their own cards, but should only be able to see one of the Dealer's cards.

#3. The objective of the game is for the Player to count their cards after they're dealt. 
#If they're not satisfied with the number, they have the ability to 'Hit'. 
#A hit allows the dealer to deal the Player one additional card. 
#The Player can hit as many times as they'd like as long as they don't 'Bust'. 
#A bust is when the Player is dealt cards that total more than 21.

#4. If the dealer deals the Player cards equal to 21 on the first deal, the Player wins. 
#This is referred to as Blackjack. 
#Blackjack is NOT the same as getting cards that equal up to 21 after the first deal. 
#Blackjack can only be attained on the first deal.

#5. The Player will never see the Dealer's hand until the Player chooses to 'stand'.
#A Stand is when the player tells the dealer to not deal it anymore cards. 
#Once the player chooses to Stand, the Player and the Dealer will compare their hands. 
#Whoever has the higher number wins. Keep in mind that the Dealer can also bust.

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
                self.deck_of_cards.append(Card(symbols[suit], values_dict[value]))



    #Get the length of the deck, to get the index, index will start at the end, going to 0, by one.
    #"random_card" will be an index, randint will return a number from 0 to # being looped, sp from 0 to index.
    #Changing the value of the random card to the value of the card at that index, this is what shuffles the deck.
    def shuffle_deck_of_cards(self):
        for indexes in range (len(self.deck_of_cards)-1,0,-1): #Fisher-Yates shuffle
            random_index = randint(0 , indexes) 
            self.deck_of_cards[indexes], self.deck_of_cards[random_index] = self.deck_of_cards[random_index], self.deck_of_cards[indexes]



    #Selecting a random card from the deck, 
    #Remember you are selecting an instance of Card, you still have to call it's method.
    #When calling this method, save it as a variable, and call the method from the class 'Card'.
    def draw_one_card(self,):
        return self.deck_of_cards.pop()
    


class player_or_dealer:
    #Array will hold the cards that the player has.
    #Set value for card points and ace count. 
    def __init__(self, dealer = False):
        self.hand = []
        self.value = 0
        self.dealer = dealer
        ace = False



    #Pass Deck object as a parameter.
    #Add the "card" to the "hand" array, using the deck class. 
    #Add the value of the card to the "value" variable, and add 1 to the "ace" variable if pulled. 
    def draw(self, card):
        self.hand.append(card)
        self.value += values_dict[card.value]



    #Figure out the value of the hand, most importantly you have to figure out the the ace value. 
    #if the value of hand is a number, add the value of the number, if its an "ace# add 11.
    #Check if value will exceed 21, if so make ace == 1 if not make ace == 11
    def calculate_value(self):
        for card in self.hand:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "Ace":
                    ace = True
                    self.value += 11
                else:
                    self.value += 10

        if ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value


    def show_cards(self):
        if self.dealer:
            print("hidden")
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("Value:", self.get_value())

class Game: 

    #will outline the game, place in a while loop so it repeats, call class 'deck' and its shuffle method to get the game started. 
    #Create a variable for the player and for the dealer, set it equal to the class 'player_or_dealer', if its the dealer set it = to true.
    #Add two cards from to each player's hand by calling the "draw_one_card" method form the class 'player_or_dealer'. 
    #Finally show cards by calling the "show_cards" method from the class 'player_or_dealer'.
    #Create a while loop to end game by checking method "check_for_blackjack". If the returned value is 21, this will end the game.

    def play(self):
        playing = True
        game_over = False

        while playing:
            self.deck = Deck()
            self.deck.shuffle_deck_of_cards()

            self.player_hand = player_or_dealer()
            self.dealer_hand = player_or_dealer(dealer=True)

            for i in range(2):
                self.player_hand.draw(self.deck.draw_one_card())
                self.dealer_hand.draw(self.deck.draw_one_card())

            print("Your hand is: ")
            self.player_hand.show_cards()
            print()
            print("Dealer's hand is: ")
            self.dealer_hand.show_cards()

            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack == 21:
                    game_over = True
                    self.show_blackjack_results(
                        player_has_blackjack, dealer_has_blackjack)
                    continue
    #Check to see if player or dealer has black jack by checking the value of their hand.
    #If the value of the hand is 21, then the player has blackjack, and their value will be returned. 
    def check_for_blackjack(self):
        player = 0
        dealer = 0
        if self.player_hand.get_value() == 21:
            player = 21
        if self.dealer_hand.get_value() == 21:
            dealer = 21

        return player, dealer
    
    #Print out results of game. as parameters , pass the whether or not the player/dealer have black jack.
    def win_loose(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack == 21 and dealer_has_blackjack == 21:
            print("Both players have blackjack.")

        elif player_has_blackjack:
            print("Congrats, you have blackjack! You win!")

        elif dealer_has_blackjack:
            print("Sorry you loose, dealer has blackjack!")
                
                


    

        
def intro():
    players_balance = 100
    greeting1 = ("Welcome to Blackjack!")
    players_name = input("What's your name? ")
    greeting2 = input(f"Hello {players_name.title()} are you ready to play? If you are type 'y' if no type 'n': ")
    while greeting2.lower()!= 'y' and greeting2.lower()!= 'n':
        greeting2 = input(f"*Invalid response* If are you ready to loose some $$$ playing BlackJack, please type 'y' otherwise type 'n': ")
    if greeting2 == 'y':
        print("Great! Let's get started, your balance is $100.")
    else:
        print(f"Sorry to see you go {players_name.title}, please come back when your ready to loose some money!")

