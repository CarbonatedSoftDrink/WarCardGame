# lets recreate the War card game.

# imports
import sys
import random

# Card class
class Card(object):
    suit = "None"
    value = 0

    def __init__(self, newSuit, newValue):
        self.suit = newSuit
        self.value = newValue

    def __str__(self):
        if self.value == 11:
            return str("Jack of " + self.suit)
        elif self.value == 12:
            return str("Queen of " + self.suit)
        elif self.value == 13:
            return str("King of " + self.suit)
        elif self.value == 14:
            return str("Ace of " + self.suit)
        else:
            return str(self.value) + " of " + str(self.suit)

    def getSuit(self): 
        return self.suit

    def setSuit(self, newSuit):
        self.suit = newSuit

    def getValue(self):
        return self.value
    
    def setValue(self, newValue):
        self.value = newValue




def deal(deckHome, deck1, deck2):
    counter = len(deckHome) - 1
    while counter > 0:
        deckCount = len(deckHome) - 1
        #print(deckCount)
        cardPulled = random.randint(0, deckCount)

        deck1.append(deckHome[cardPulled])
        deckHome.pop(cardPulled)
        counter = counter - 1

        deckCount = len(deckHome) - 1
        cardPulled = random.randint(0, deckCount)

        deck2.append(deckHome[cardPulled])
        deckHome.pop(cardPulled)
        counter = counter - 1




def war(playerScore, opponentScore, deckHome, deckPlayer, deckOpponent, pile):
    if len(deckPlayer) == 0:
        print("But there are no more cards to play! All the cards in this war are forfeit.")
        return

    localPile = pile + 2
    userChoice = 0
    myCard = 0
    theirCard = 0
    myPlay = 0
    theirPlay = 0
    print("War mode:")

    while userChoice > 4 or userChoice < 1:
        try:
            userChoice = int(input("Enter a number between 1 and 4 to play a card: "))
            if userChoice > 4 or userChoice < 1:
                print("Invalid option.")
        except:
            print("Invalid datatype.")

        myCard = random.randint(0, len(deckPlayer)-1)
        theirCard = random.randint(0, len(deckOpponent)-1)
        print("The player plays:" , deckPlayer[myCard])
        print("The opponent plays:" , deckOpponent[theirCard])

        myPlay = deckPlayer[myCard].getValue()
        theirPlay = deckOpponent[theirCard].getValue()
        print(myPlay)
        print(theirPlay)

        if myPlay > theirPlay:
            print("The player wins the war!")
            playerScore = playerScore + localPile

            deckHome.append(deckPlayer[myCard])
            deckHome.append(deckOpponent[theirCard])

            deckPlayer.pop(myCard)
            deckOpponent.pop(theirCard)

            return [True, localPile]

        elif myPlay < theirPlay:
            print("The opponent wins the war!")
            opponentScore = opponentScore + localPile
            
            deckHome.append(deckPlayer[myCard])
            deckHome.append(deckOpponent[theirCard])

            deckPlayer.pop(myCard)
            deckOpponent.pop(theirCard)

            return [False, localPile]

        elif myPlay == theirPlay:
            print("A tie! We have another War.")
            war(playerScore, opponentScore, deckHome, deckPlayer, deckOpponent, pile)
        else:
            print("Woah! What happened??")




def gameplay(deckHome, deckPlayer, deckOpponent):
    print("Lets play!")
    playerScore = 0
    opponentScore = 0
    userChoice = 0
    myCard = 0
    theirCard = 0
    myPlay = 0
    theirPlay = 0

    while len(deckPlayer) > 0:
        print("----------------------------")
        print("Player score =" , playerScore)
        print("Opponent score =" , opponentScore)
        while userChoice > 4 or userChoice < 1:
            try:
                userChoice = int(input("Enter a number between 1 and 4 to play a card: "))
                if userChoice > 4 or userChoice < 1:
                    print("Invalid option.")
            except:
                print("Invalid datatype.")

        myCard = random.randint(0, len(deckPlayer)-1)
        theirCard = random.randint(0, len(deckOpponent)-1)
        print("The player plays:" , deckPlayer[myCard])
        print("The opponent plays:" , deckOpponent[theirCard])

        myPlay = deckPlayer[myCard].getValue()
        theirPlay = deckOpponent[theirCard].getValue()
        print(myPlay)
        print(theirPlay)

        if myPlay > theirPlay:
            print("The player wins this hand!")
            playerScore = playerScore + 2

            deckHome.append(deckPlayer[myCard])
            deckHome.append(deckOpponent[theirCard])

            deckPlayer.pop(myCard)
            deckOpponent.pop(theirCard)

            userChoice = 0

        elif myPlay < theirPlay:
            print("The opponent wins this hand!")
            opponentScore = opponentScore + 2
            
            deckHome.append(deckPlayer[myCard])
            deckHome.append(deckOpponent[theirCard])

            deckPlayer.pop(myCard)
            deckOpponent.pop(theirCard)

            userChoice = 0

        elif myPlay == theirPlay:
            print("A tie! We have a War.")

            deckHome.append(deckPlayer[myCard])
            deckHome.append(deckOpponent[theirCard])

            deckPlayer.pop(myCard)
            deckOpponent.pop(theirCard)

            userChoice = 0

            outcomeList = war(playerScore, opponentScore, deckHome, deckPlayer, deckOpponent, 2)
            if outcomeList[0] == True:
                playerScore = playerScore + outcomeList[1]
            elif outcomeList[0] == False:
                opponentScore = opponentScore + outcomeList[1]
            else:
                print("hmmmm....")
                
        else:
            print("Woah! What happened?")
            userChoice = 0

    print("And thats the game! Determining a winner...")
    print("Player score =" , playerScore)
    print("Opponent score =" , opponentScore)
    if playerScore > opponentScore:
        print("The player wins!")
    elif playerScore < opponentScore:
        print("The opponent wins!")
    elif playerScore == opponentScore:
        print("It's a tie!")
    else:
        print("No one wins?")
    
        



def main(): # heres the beginning of main!
    deck = [Card("Hearts", 2), Card("Hearts",3), Card("Hearts", 4), Card("Hearts",5), Card("Hearts", 6), Card("Hearts",7), Card("Hearts", 8), Card("Hearts",9), Card("Hearts", 10), Card("Hearts",11), Card("Hearts", 12), Card("Hearts",13), Card("Hearts", 14)
    , Card("Spades", 2), Card("Spades",3), Card("Spades", 4), Card("Spades",5), Card("Spades", 6), Card("Spades",7), Card("Spades", 8), Card("Spades",9), Card("Spades", 10), Card("Spades",11), Card("Spades", 12), Card("Spades",13), Card("Spades", 14)
    , Card("Clubs", 2), Card("Clubs",3), Card("Clubs", 4), Card("Clubs",5), Card("Clubs", 6), Card("Clubs",7), Card("Clubs", 8), Card("Clubs",9), Card("Clubs", 10), Card("Clubs",11), Card("Clubs", 12), Card("Clubs",13), Card("Clubs", 14)
    ,Card("Diamonds", 2), Card("Diamonds",3), Card("Diamonds", 4), Card("Diamonds",5), Card("Diamonds", 6), Card("Diamonds",7), Card("Diamonds", 8), Card("Diamonds",9), Card("Diamonds", 10), Card("Diamonds",11), Card("Diamonds", 12), Card("Diamonds",13), Card("Diamonds", 14)]
    myDeck = []
    opponentDeck = []

    print("Welcome! Dealing out the cards...")
    deal(deck, myDeck, opponentDeck)
    gameplay(deck, myDeck, opponentDeck)
    #for i in myDeck:
    #    print(i)



if __name__== "__main__" :
    main()
    print("Exiting...")
