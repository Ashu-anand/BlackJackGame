import random as r
from os import system
import time


class Cards:
    suits = {'S': '\u2660',
             'C': '\u2663',
             'H': '\u2665',
             'D': '\u2666'}

    def __init__(self,nod):
        card_num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
        suits = ['S', 'C', 'H', 'D']
        self.deck = ([(idx, jdx) for idx in suits for jdx in card_num])
        self.deck=self.deck*nod
        r.shuffle (self.deck)

    def reshuffle_deck(self, current_hand):
        #self.__init__ (self)
        pass

    def print_card(self, card_suit):
        pass


class Hands:
    def __init__(self, is_dealer=False):
        self.dealer_hand = is_dealer
        self.cards = []
        self.value = 0

    def add_card(self, card):
        self.cards.append (card)
        if type (card[1]) == int:
            self.value = self.value + card[1]
        else:
            self.value = self.value + 10

    def show_card(self, hide=False):
        if self.dealer_hand:
            print ('Dealer'.rjust (60))
            if hide:
                print ('[X,{0}] ({1})'.format (self.cards[1], self.value).rjust (60))
            else:
                print ('{0} ({1})'.format (self.cards, self.value).rjust (60))
            for idx in range (4): print ('')
        else:
            print ('{0}'.format (self.cards).rjust (100))
            print ('Total: ({0})'.format (self.value).rjust (100))


def clear_screen():
    system ('cls')


def delay(t=0):
    time.sleep (t)


clear_screen ()
print ('Welcome to Black Jack'.rjust (70))
delay ()
print ("How may decks you want to play with ")
delay ()
num_of_decks = int (input ("Choose from number 1 to 4: "))
clear_screen ()

while num_of_decks not in range (1, 5):
    num_of_decks = int (input ("Invalid Selection. Please from number 1 to 4: "))

card = Cards (num_of_decks)
print ("")
"""
Setting the game to start from here. This game will continue till the time
player select N for playing further.
"""

play = 'Y'
while play in ("Y", "y"):
    dealer = Hands (True)
    player = Hands ()
    for idx in range (2):
        player.add_card (card.deck.pop ())
        dealer.add_card (card.deck.pop ())
    dealer.show_card (True)
    player.show_card ()

    response = 2
    while response != 1:
        print ('')
        try:
            response = int (input ('Do you want to Stay (1) or hit(2)?: '))
            if response == 2:
                player.add_card (card.deck.pop ())
            system ('cls')
            dealer.show_card (True)
            player.show_card ()
            if player.value > 21:
                print ('You Lost!! You have total of {0} for cards in {1}'.format (player.value, player.cards))
                break
            else:
                print ('You have total of {0} for cards in {1}'.format (player.value, player.cards))
        except:
            print ('Please enter correct number')
            response = 0

    while dealer.value < 17 and player.value < 22:
        system ('cls')
        dealer.show_card (False)
        player.show_card ()
        print ('')
        print ('Dealer has total of {0} for cards in {1}. Dealer Turn to Pick the card'.format (dealer.value,
                                                                                                dealer.cards))
        input ('Press any key to continue..')
        print ('')
        dealer.add_card (card.deck.pop ())
    system ('cls')
    dealer.show_card (False)
    player.show_card ()

    if player.value > 21:
        print ('Dealer has {0} and You have {1}. Dealer WON!!'.format (dealer.value,
                                                                       player.value))
    elif dealer.value > 21:
        print (
            'You has {0} and Dealer have {1}. You WON!!'.format (player.value, dealer.value))
    elif dealer.value > player.value:
        print ('Dealer has total of {0} for cards in {1}. Dealer Won!!'.format (dealer.value, dealer.cards))
    elif player.value > dealer.value:
        print ('You has total of {0} for cards in {1}. Dealer has total of {2} for cards in {3}. You Won!!' \
               .format (player.value, player.cards, dealer.value, dealer.cards))
    else:
        print ('Both you have dealer have same total. It''s a Tie.')
    print ('')

    play = input ('Do You want to play More. Yes (Y) or No (N)')
    clear_screen ()
else:
    print ("Thanks for playing with us")
    input ("Press any key to exist...")
