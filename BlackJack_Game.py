import random as r
from os import system

global num_of_decks
suits_dict = {'S': '\u2660', # Suits
              'C': '\u2663', # Club
              'H': '\u2665', # Heart
              'D': '\u2666', # Diamond
              '?': '?'}      # Hidden card


class Cards:
    def __init__(self, nod):
        # The Card Value
        rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']

        # Type of Suit
        suits = ['S', 'C', 'H', 'D']

        # Creating a single deck
        self.deck = ([(idx, jdx) for idx in suits for jdx in rank])

        # Creating the number of deck as per user choice
        self.deck = self.deck * nod

        # Shuffle the deck
        r.shuffle (self.deck)

    def reshuffle_deck(self, nod):
        input ("Deck about to finish. Reshuffling deck. Press any key to continue..")
        self.__init__ (nod)


class Hands:
    def __init__(self, player_onhand=pow (2, 25), is_dealer=False):
        # if this is a dealer hand
        self.dealer_hand = is_dealer

        # if this hand contains Ace card or total going above 21 for Ace card
        self.ace = False
        self.cards = []
        self.value = 0
        self.player_current_balance = player_onhand
        self.bet = 0

    def win_bet(self):
        self.player_current_balance += self.bet

    def lose_bet(self):
        self.player_current_balance -= self.bet

    def add_card(self, card):
        self.cards.append (card)
        if card[1] == 'A':
            if not self.ace and (self.value + 11 <= 21):
                self.value = self.value + 11
                self.ace = True
            else:
                self.value = self.value + 1
        else:
            if type (card[1]) == int:
                self.value = self.value + card[1]
            else:
                self.value = self.value + 10
            if self.value > 21 and self.ace:
                self.value -= 10
                self.ace = False

    def print_card(self, card_suit, pos=1):
        s = ""
        for _ in card_suit:
            s = s + "\t ________"
        print (s.rjust (pos))
        s = ""
        for idx, jdx in card_suit:
            if jdx == 10:
                s = s + "\t| {0}     |".format (jdx)
            else:
                s = s + "\t| {0}      |".format (jdx)
        print (s.rjust (pos))
        s = ""
        for _ in card_suit:
            s = s + "\t|        |"
        print (s.rjust (pos))
        s = ""
        for idx, jdx in card_suit:
            s = s + "\t|   {0}    |".format (suits_dict[idx])
        print (s.rjust (pos))
        s = ""
        for _ in card_suit:
            s = s + "\t|        |"
        print (s.rjust (pos))
        s = ""
        for idx, jdx in card_suit:
            if jdx == 10:
                s = s + "\t|     {0} |".format (jdx)
            else:
                s = s + "\t|      {0} |".format (jdx)
        print (s.rjust (pos))
        s = ""
        for _ in card_suit:
            s = s + "\t|________|"
        print (s.rjust (pos))

    def show_card(self, hide=False):
        if self.dealer_hand:
            if hide:
                print ('Dealer'.rjust (60))
                self.print_card ([self.cards[0], ('?', '?')])
            else:
                print ('Dealer (Total: {0})'.format (self.value).rjust (60))
                self.print_card (self.cards)
            for idx in range (4): print ('')
        else:
            print ('Player (Total: {0})'.format (self.value).rjust (60))
            self.print_card (self.cards)
            print ('Bet Amount: {0}'.format (self.bet).rjust (60))


def clear_screen():
    system ('cls')


def validate_number(p_text):
    while True:
        try:
            p_num = int (input (p_text))
        except ValueError:
            print ("Sorry, please enter a number")
        else:
            return p_num


def take_bet(player_hand):
    while True:
        player_hand.bet = validate_number ('How many chips you want to bet: ')
        if player_hand.bet > player_hand.player_current_balance:
            print ("Sorry, you cannot bet more than {0}".format (player_hand.player_current_balance))
        else:
            clear_screen ()
            break


def select_play_deck():
    global num_of_decks
    print ("How may decks you want to play with \n")
    num_of_decks = validate_number ("Choose from number 1 to 4: ")
    while num_of_decks not in range (1, 5):
        clear_screen ()
        num_of_decks = int (input ("Invalid Selection. Please select from number 1 to 4: "))
    clear_screen ()


"""
Setting the game to start from here. This game will continue till the time
player select N for playing further.
"""
if __name__ == '__main__':
    print ('Welcome to Black Jack'.rjust (70))

    # Asking the player to select the number of decks he would like to play with
    select_play_deck ()

    # Setting up the deck as per the user choice
    card = Cards (num_of_decks)

    # Setting up player opening balance to 100
    player_opening_balance = 100

    # Setting up the game flag to Y to start the game.
    play = 'Y'

    while play in ("Y", "y"):
        # Setting up Dealer hand
        dealer = Hands (is_dealer=True)

        # Setting up player hand with the number of chips he brought to table or he had after the last round
        player = Hands (player_opening_balance)

        # Taking bet from the player
        take_bet (player)

        # if the number of cards are less than 8 then reshuffle the card
        if len (card.deck) <= 7:
            card.reshuffle_deck (num_of_decks)

        # Dealing initial 2 cards each to player and dealer
        for idx in range (2):
            player.add_card (card.deck.pop ())
            dealer.add_card (card.deck.pop ())

        # Displaying dealer Card
        dealer.show_card (True)
        # Displaying Player Card
        player.show_card ()

        response = 2
        # Dealing the card to the player till he don't stay
        while response != 1:
            print ('')
            try:
                response = int (input ('Do you want to Stay (1) or hit(2)?: '))
                # Adding card to the player
                if response == 2:
                    player.add_card (card.deck.pop ())
                system ('cls')

                # showing the Dealer and player cards both
                dealer.show_card (True)
                player.show_card ()

                # If the player total is 21 then asking player to stay.
                if player.value == 21:
                    input ('Your Total is 21. Stay at 21. Dealer Turn. Press any key to continue')
                    break
                # If the player total is more than 22, then player got busted.
                elif player.value > 21:
                    break
            except ValueError:
                print ('Please enter correct number')
                response = 0

        # If the dealer value is less than 17 and player value is less than 22, then it's dealer turn
        while dealer.value < 17 and player.value < 22:
            system ('cls')

            # showing the Dealer and player cards both
            dealer.show_card (False)
            player.show_card ()

            print ('')
            print ('Dealer cards total is {0}. Dealer Turn to Pick the card \n'.format (dealer.value))
            input ('Press any key to continue...')

            # Dealing the card to the dealer
            dealer.add_card (card.deck.pop ())
        system ('cls')

        # showing the Dealer and player cards both
        dealer.show_card (False)
        player.show_card ()

        # Checking who won after each dealer deal
        if player.value > 21:
            player.lose_bet ()
            print ('Dealer has {0} and You have {1}. Dealer WON!!'.format (dealer.value,
                                                                           player.value))
        elif dealer.value > 21:
            player.win_bet ()
            print (
                'You has {0} and Dealer have {1}. You WON!!'.format (player.value, dealer.value))
        elif dealer.value > player.value:
            player.lose_bet ()
            print ('Dealer has total of {0} for cards. Dealer Won!!'.format (dealer.value))
        elif player.value > dealer.value:
            player.win_bet ()
            print ('You has total of {0} for cards. Dealer has total of {1} for cards. You Won!!'.format (player.value,
                                                                                                          dealer.value))
        else:
            print ('Both you have dealer have same total. It''s a Tie.')
        print ('')

        # Getting player current balance.
        player_opening_balance = player.player_current_balance

        # Showing the player current balance.
        print ("You have {0} chips in hand. \n".format (player_opening_balance))

        # If the player current balance is 0 then quiting the game for the player.
        if player_opening_balance == 0:
            input ()
            play = 'N'
        else:
            play = input ('Do You want to play More. Yes (Y) or No (N)')
        clear_screen ()
    else:
        print ("Thanks for playing with us. You have {0} chips in hand. \n".format (player_opening_balance))
        input ("Press any key to exist...")
