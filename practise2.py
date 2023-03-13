#ask user for amount of money they wan to bet< make sure user has enough money to bet.
def take_bet(chips): 
    while True:
        try:
            Player.bet = int(input("How many much would you like to bet? "))
        except ValueError:
            print("*Error* Please can you type in a number: ")
        else:
            if Player.bet > Player.total:
                print("You dont have enough money!")
            else:
                break

#Since ace can be written as 1 or 11, we need to check he value of hand and decide what ace will be worth.
    def adjust_value_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 

    #If the player wins bet the bet will be added to the "total" variable.
    def win_bet(self):
        self.total += self.bet

    #If the player loses bet the bet will be subtracted to the "total" variable.
    def lose_bet(self):
        self.total -= self.bet

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

    #When using this function, you have to pass "Deck" instance as a parameter.
    def show_cards_in_hand(self):
        for card in self.hand:
            card.show_formatted_card()