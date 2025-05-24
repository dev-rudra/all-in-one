#!/usr/bin/python3

import random

# card constants
SUIT_TUPPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

# pass in a deck and this function returns a random
# card from the deck

def getCard(deckListIn):
    thisCard = deckListIn.pop() # pop one off the top of the deck and return
    return thisCard

# pass in the deck and this function returns a shuffled copy of the desk

def shuffle(deckListIn):
    deckListOut = deckListIn.copy() # make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut

# Main code
print("Welcome to Higher or Lower.")
print("You have to choose whether the next card to be shown will be higher or lower than the current card.")
print("Getting it right adds 20 points; get it wrong and you lose 15 points.")
print("You have 50 points to start.")
print()

startingDeckList = []

for suit in SUIT_TUPPLE:
    for thisValue, rank in enumerate(RANK_TUPPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)
    
    print(startingDeckList)
    score = 50

    while True: # play multiple games
        print()
        gameDeckList = shuffle(startingDeckList)

        currentCardDict = getCard(gameDeckList)
        currentCardRank = currentCardDict['rank']
        currentCardValue = currentCardDict['value']
        currentCardSuit = currentCardDict['suit']

        print('Starting card as:', currentCardRank + ' of ' + currentCardSuit)
        print()

        for cardNumber in range(0, NCARDS): #play one game of this many cards
            answer = input("Will the next card be higher or lower tahn the " + currentCardRank + " of " + currentCardSuit + ' ? (enter h or 1):')
            answer = answer.casefold() # force lowercase

            nextCardDict = getCard(gameDeckList)
            nextCardRank = nextCardDict['rank']
            nextCardSuit = nextCardDict['suit']
            nextCardValue = nextCardDict['value']

            print("Next card is:", nextCardRank + " of " + nextCardSuit)

            if answer == 'h':
                if nextCardValue > currentCardValue:
                    print("You got it right, it was higher")
                    score = score + 20
                else:
                    print("Sorry, it was not higher")
                    score = score - 15
            elif answer == '1':
                if nextCardValue < currentCardValue:
                    score = score + 20
                    print("You got it right, it was higher")
                else:
                    score = score - 15
                    print("Sorry, it was not lower")

            print("Your score is:", score)
            print()
            currentCardRank = nextCardRank
            currentCardvalue = nextCardValue # Don't need current suit

        goAgian = input('To play agina, press ENTER, or "q" to quit: ')

        if goAgain == 'q':
            break

        print("OK bye!")


