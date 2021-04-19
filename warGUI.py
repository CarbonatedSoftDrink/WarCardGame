# Gregory Flores
# War card game with breezypythongui
######################################

# imports
from breezypythongui import EasyFrame
from tkinter import PhotoImage
import sys
import random

# Card class
class Card(object):
    suit = "None"
    value = 0
    letter = ""

    def __init__(self, newSuit, newValue):
        self.suit = newSuit
        self.value = newValue
        if self.value == 11:
            self.letter += "J"
            self.letter += self.suit[0]
        elif self.value == 12:
            self.letter += "Q"
            self.letter += self.suit[0]
        elif self.value == 13:
            self.letter += "K"
            self.letter += self.suit[0]
        elif self.value == 14:
            self.letter += "A"
            self.letter += self.suit[0]
        else:
            self.letter += str(self.value)
            self.letter += self.suit[0]

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
    
    def getLetter(self):
        return self.letter

# Deal function
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

# Reset the game
def gimmieBack(deckHome, deck1, deck2):
    counter = len(deck1) - 1
    while counter > -1:
        deckHome.append(deck1[counter])
        deck1.pop(counter)
        counter = counter - 1
    
    counter = len(deck2) - 1
    while counter > -1:
        deckHome.append(deck2[counter])
        deck2.pop(counter)
        counter = counter - 1


## GUI #######################################################
class warGame(EasyFrame):
    """Illustrates command buttons and user events."""
    playerScore = 0
    opponentScore = 0
    myCard = 0
    theirCard = 0
    myPlay = 0
    theirPlay = 0
    warStatus = 0
    myPath = ""
    theirPath = ""
    path = "cardPictures/"
    ext = ".png"

    def __init__(self):
        """Sets up the window, label, and buttons."""
        EasyFrame.__init__(self, "War! Card Game", 700, 360, "green")

        # Title at the top of the menu
        title = self.addLabel(text = "War! Card Game", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "light green")

        # The text input box
        #self.inputField = self.addFloatField(value = 0, row = 1, column = 0, width = 10, sticky = "NSEW")

        # Play button
        self.playButton = self.addButton(text = "Play", row = 1, column = 0, command = self.playGame)

        # Quit button
        self.quitButton = self.addButton(text = "Quit", row = 2, column = 0, command = self.quitGame)

        # Opponent label
        opponentName = self.addLabel(text = "Opponent", row = 1, column = 5, sticky = "NSEW")

        # Opponent deck
        self.opponentDeckCount = self.addLabel(text = "0", row = 0, column = 5, sticky = "NSEW")

        # Opponent's score
        self.opponentScoreDisplay = self.addLabel(text = "Opponent Score:", row = 1, column = 3, sticky = "NSEW")

        # Opponent's card
        self.opponentCardPlayed = self.addLabel(text = "", row = 1, column = 4, sticky = "NSEW")

        # Player's hand
        self.cardDisplay1 = self.addLabel(text = "", row = 2, column = 3, sticky = "NSEW")
        self.image1 = PhotoImage(file = "cardPictures/Blue_back.png")
        self.cardDisplay1["image"] = self.image1

        # Winner label
        self.winner = self.addLabel(text = ".........", row = 2, column = 4, sticky = "NSEW")

        # Opponent's hand
        self.cardDisplay2 = self.addLabel(text = "", row = 2, column = 5, sticky = "NSEW")
        self.image2 = PhotoImage(file = "cardPictures/Red_back.png")
        self.cardDisplay2["image"] = self.image2
        
        # Player's card
        self.playerCardPlayed = self.addLabel(text = "", row = 3, column = 4, sticky = "NSEW")

        # Player's score
        self.playerScoreDisplay = self.addLabel(text = "Player Score:", row = 3, column = 5, sticky = "NSEW")

        # Player deck
        self.playerDeckCount = self.addLabel(text = "0", row = 4, column = 3, sticky = "NSEW")

        # Player label
        playerName = self.addLabel(text = "Player", row = 3, column = 3, sticky = "NSEW")

        # Next button
        self.nextButton = self.addButton(text = "Next round", row = 4, column = 4, command = self.nextAction, state="disabled")

        # Card buttons
        #cardButton1 = self.addButton(text = "Card #1", row = 5, column = 2, command = self.playGame)
        self.cardButton2 = self.addButton(text = "Card #2", row = 5, column = 3, command = self.cardSelect, state="disabled")
        self.cardButton3 = self.addButton(text = "Card #3", row = 5, column = 4, command = self.cardSelect, state="disabled")
        self.cardButton4 = self.addButton(text = "Card #4", row = 5, column = 5, command = self.cardSelect, state="disabled")

    # Methods to handle user events
    # function to play the game
    def playGame(self):
        self.playButton["state"] = "disabled"
        deal(deck, myDeck, opponentDeck)
        self.playerDeckCount["text"] = len(myDeck)
        self.opponentDeckCount["text"] = len(opponentDeck)
        self.nextButton["state"] = "disabled"
        self.winner["text"] = "Play a card!"

        self.playerScoreDisplay["text"] = ("Player Score: " + str(self.playerScore))
        self.opponentScoreDisplay["text"] =("Opponent Score: " + str(self.opponentScore))

        self.cardButton2["state"] = "normal"
        self.cardButton3["state"] = "normal"
        self.cardButton4["state"] = "normal"



    def nextAction(self):
        self.image1 = PhotoImage(file = "cardPictures/Blue_back.png")
        self.cardDisplay1["image"] = self.image1
        self.image2 = PhotoImage(file = "cardPictures/Red_back.png")
        self.cardDisplay2["image"] = self.image2
        self.myPath = ""
        self.theirPath = ""
        
        self.nextButton["state"] = "disabled"

        if len(myDeck) == 0:
            if self.playerScore > self.opponentScore:
                self.winner["text"] = "You win!"
            elif self.playerScore < self.opponentScore:
                self.winner["text"] = "Opponent wins!"
            elif self.playerScore == self.opponentScore:
                self.winner["text"] = "It's a tie!"
            else:
                self.winner["text"] = "Nobody wins?!"

            self.playerCardPlayed["text"] = ""
            self.opponentCardPlayed["text"] = ""
            
            self.nextButton["state"] = "disabled"
            self.cardButton2["state"] = "disabled"
            self.cardButton3["state"] = "disabled"
            self.cardButton4["state"] = "disabled"

        elif self.warStatus > 0:
            self.winner["text"] = "War! Play a card!"
            self.playerCardPlayed["text"] = ""
            self.opponentCardPlayed["text"] = ""

            if len(myDeck) >= 3:
                self.cardButton2["state"] = "normal"
                self.cardButton3["state"] = "normal"
                self.cardButton4["state"] = "normal"
            elif len(myDeck) >= 2:
                self.cardButton2["state"] = "normal"
                self.cardButton3["state"] = "normal"
                self.cardButton4["state"] = "disabled"
            else:
                self.cardButton2["state"] = "normal"
                self.cardButton3["state"] = "disabled"
                self.cardButton4["state"] = "disabled"

        else:
            self.winner["text"] = "Play a card!"
            self.playerCardPlayed["text"] = ""
            self.opponentCardPlayed["text"] = ""

            if len(myDeck) >= 3:
                self.cardButton2["state"] = "normal"
                self.cardButton3["state"] = "normal"
                self.cardButton4["state"] = "normal"
            elif len(myDeck) >= 2:
                self.cardButton2["state"] = "normal"
                self.cardButton3["state"] = "normal"
                self.cardButton4["state"] = "disabled"
            else:
                self.cardButton2["state"] = "normal"
                self.cardButton3["state"] = "disabled"
                self.cardButton4["state"] = "disabled"



    def cardSelect(self):
        self.cardButton2["state"] = "disabled"
        self.cardButton3["state"] = "disabled"
        self.cardButton4["state"] = "disabled"

        myCard = random.randint(0, len(myDeck)-1)
        theirCard = random.randint(0, len(opponentDeck)-1)

        self.playerCardPlayed["text"] = str(myDeck[myCard])
        self.opponentCardPlayed["text"] = str(opponentDeck[theirCard])

        myPlay = myDeck[myCard].getValue()
        theirPlay = opponentDeck[theirCard].getValue()

        self.myPath += self.path
        self.myPath += myDeck[myCard].getLetter()
        self.myPath += self.ext
        self.image1 = PhotoImage(file = self.myPath)
        self.cardDisplay1["image"] = self.image1

        self.theirPath += self.path
        self.theirPath += opponentDeck[theirCard].getLetter()
        self.theirPath += self.ext
        self.image2 = PhotoImage(file = self.theirPath)
        self.cardDisplay2["image"] = self.image2

        deck.append(myDeck[myCard])
        deck.append(opponentDeck[theirCard])

        myDeck.pop(myCard)
        opponentDeck.pop(theirCard)

        self.playerDeckCount["text"] = len(myDeck)
        self.opponentDeckCount["text"] = len(opponentDeck)


        if myPlay > theirPlay:
            if self.warStatus == 0:
                self.winner["text"] = "The player wins this hand!"
                self.playerScore = self.playerScore + 2
                self.playerScoreDisplay["text"] = ("Player Score: " + str(self.playerScore))
            else:
                self.winner["text"] = "The player wins this war!"
                self.playerScore = self.playerScore + self.warStatus
                self.playerScoreDisplay["text"] = ("Player Score: " + str(self.playerScore))
                self.warStatus = 0

            self.nextButton["state"] = "normal"
        elif myPlay < theirPlay:
            if self.warStatus == 0:
                self.winner["text"] = "The opponent wins this hand!"
                self.opponentScore = self.opponentScore + 2
                self.opponentScoreDisplay["text"] =("Opponent Score: " + str(self.opponentScore))
            else:
                self.winner["text"] = "The opponent wins this war!"
                self.opponentScore = self.opponentScore + self.warStatus
                self.opponentScoreDisplay["text"] =("Opponent Score: " + str(self.opponentScore))
                self.warStatus = 0

            self.nextButton["state"] = "normal"
        elif myPlay == theirPlay:
            if self.warStatus == 0:
                self.winner["text"] = "A tie! This means war!"
                self.warStatus = self.warStatus + 4
            else:
                self.winner["text"] = "A tie! This means another war!"
                self.warStatus = self.warStatus + 2

            self.nextButton["state"] = "normal"
        else:
            self.winner["text"] = "Woah! What?"

    # function to quit the game
    def quitGame(self):
        self.playerScore = 0
        self.opponentScore = 0
        self.myCard = 0
        self.theirCard = 0
        self.myPlay = 0
        self.theirPlay = 0
        self.warStatus = 0

        self.playButton["state"] = "normal"
        gimmieBack(deck, myDeck, opponentDeck)
        self.playerDeckCount["text"] = len(myDeck)
        self.opponentDeckCount["text"] = len(opponentDeck)
        self.nextButton["state"] = "disabled"
        self.cardButton2["state"] = "disabled"
        self.cardButton3["state"] = "disabled"
        self.cardButton4["state"] = "disabled"

        self.playerCardPlayed["text"] = ""
        self.opponentCardPlayed["text"] = ""
        
        self.image1 = PhotoImage(file = "cardPictures/Blue_back.png")
        self.cardDisplay1["image"] = self.image1
        self.image2 = PhotoImage(file = "cardPictures/Red_back.png")
        self.cardDisplay2["image"] = self.image2
        self.myPath = ""
        self.theirPath = ""

        self.playerScoreDisplay["text"] = "Player Score:"
        self.opponentScoreDisplay["text"] = "Opponent Score:"
        self.winner["text"] = "........."
        SystemExit(0)


# The set up
deck = [Card("Hearts", 2), Card("Hearts",3), Card("Hearts", 4), Card("Hearts",5), Card("Hearts", 6), Card("Hearts",7), Card("Hearts", 8), Card("Hearts",9), Card("Hearts", 10), Card("Hearts",11), Card("Hearts", 12), Card("Hearts",13), Card("Hearts", 14)
    , Card("Spades", 2), Card("Spades",3), Card("Spades", 4), Card("Spades",5), Card("Spades", 6), Card("Spades",7), Card("Spades", 8), Card("Spades",9), Card("Spades", 10), Card("Spades",11), Card("Spades", 12), Card("Spades",13), Card("Spades", 14)
    , Card("Clubs", 2), Card("Clubs",3), Card("Clubs", 4), Card("Clubs",5), Card("Clubs", 6), Card("Clubs",7), Card("Clubs", 8), Card("Clubs",9), Card("Clubs", 10), Card("Clubs",11), Card("Clubs", 12), Card("Clubs",13), Card("Clubs", 14)
    ,Card("Diamonds", 2), Card("Diamonds",3), Card("Diamonds", 4), Card("Diamonds",5), Card("Diamonds", 6), Card("Diamonds",7), Card("Diamonds", 8), Card("Diamonds",9), Card("Diamonds", 10), Card("Diamonds",11), Card("Diamonds", 12), Card("Diamonds",13), Card("Diamonds", 14)]
myDeck = []
opponentDeck = []


# initializes the gui
if __name__ == "__main__":
    warGame().mainloop()