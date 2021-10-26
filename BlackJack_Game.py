import random as r
from os import system, name
import time

def show_user(user_card):
    print('{0}'.format(user_card).rjust(100))
    print ('You ({0})'.format (sum(user_card)).rjust(100))

def show_dealer(dealer_card,hide=True):
    print('Dealer'.rjust(60))
    if hide:
        print('[X,{0}] ({1})'.format(dealer_card[1],dealer_card[1]).rjust(60))
    else:
        print('{0} ({1})'.format(dealer_card,sum(dealer_card)).rjust(60))
    print('')
    print('')
    print('')
    print('')


def clear_screen():
    system ('cls')

def delay(t=0):
    time.sleep (t)

def check_card_total(cards):
    return sum(cards)

clear_screen()
print('Welcome to Black Jack'.rjust(70))
delay()
print("How may decks you want to play with ")
delay()
num_of_decks=int(input("Choose from number 1 to 4: "))
clear_screen()

while num_of_decks not in range(1,5):
    num_of_decks=int(input("Invalid Selection. Please from number 1 to 4: "))

cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]
cards=cards*4*num_of_decks
r.shuffle(cards)

print("")
"""
Setting the game to start from here. This game will continue till the time
player select N for playing further.
"""
play='Y'
while play in ("Y","y"):
    dealer=[]
    player=[]
    for idx in range(2):
        temp=cards.pop()
        player.append(temp)
        temp=cards.pop()
        dealer.append (temp)
    show_dealer(dealer,True)
    show_user(player)

    response=2
    while response!=1 :
        print('')
        try:
            response=int(input('Do you want to Stay (1) or hit(2)?: '))
            if response==2:
                temp=cards.pop()
                player.append(temp)
            system('cls')
            show_dealer(dealer,True)
            show_user(player)
            if sum(player)>21:
                print ('You Lost!! You have total of {0} for cards in {1}'.format (check_card_total(player),player))
                break
            else:
                print ('You have total of {0} for cards in {1}'.format (check_card_total(player),player))
        except:
            print('Please enter correct number')
            response=0

    while check_card_total(dealer)<17 and check_card_total(player)<22:
        system('cls')
        show_dealer(dealer,False)
        show_user(player)
        print('')
        print('Dealer has total of {0} for cards in {1}. Dealer Turn to Pick the card'.format(sum(dealer),dealer))
        input('Press any key to continue..')
        print('')
        temp=cards.pop()
        dealer.append(temp)
    system('cls')
    show_dealer(dealer,False)
    show_user(player)

    if check_card_total(player)>21:
        print('Dealer has {0} and You have {1}. Dealer WON!!'.format(check_card_total(dealer),check_card_total(player)))
    elif check_card_total(dealer)>21:
        print('You has {0} and Dealer have {1}. You WON!!'.format(check_card_total(player),check_card_total(dealer)))
    elif check_card_total(dealer)>check_card_total(player):
        print ('Dealer has total of {0} for cards in {1}. Dealer Won!!'.format (check_card_total(dealer),dealer))
    elif check_card_total(player)>check_card_total(dealer):
        print ('You has total of {0} for cards in {1}. Dealer has total of {2} for cards in {3}. You Won!!'
               .format (check_card_total(player),player,check_card_total(dealer),dealer))
    else:
        print('Both you have dealer have same total. It''s a Tie.')
    print('')


    play = input ('Do You want to play More. Yes (Y) or No (N)')
    clear_screen ()
else:
    print("Thanks for playing with us")
    input("Press any key to exist...")

