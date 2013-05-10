# blackjack.py
# Author: Bill Drescher
# Course: CS680

from random import shuffle
from tkinter import *
root = Tk()
faces = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
         "Ten", "Jack", "Queen", "King", "Ace" )
suits = ( "Clubs", "Diamonds", "Hearts", "Spades" )
values = ( 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11 )
playerActions = ( "Double Down", "Hit", "Split", "Stand", "Surrender" )

class Card:

   def __init__( self, face, suit, value ):
      self.face = face
      self.suit = suit
      self.value = value

class Deck:

   def __init__( self, numDecks ):
      self.topCard = 0
      self.deck = []
      for k in range( 0, numDecks ):
         for i in range( 0, len( suits ) ):
            for j in range( 0, len( faces ) ):
               self.deck.append( Card( faces[j], suits[i], values[j] ) )

   def shuffleDeck( self ):
      shuffle( self.deck )

   def dispDeck( self, start, stop ):
      outStr0 = self.deck[i].face + " of " + self.deck[i].suit
      for i in range( start, stop ):
#         print( "%s%s%s" % ( self.deck[i].face.rjust(5), " of ",
#                self.deck[i].suit.ljust(8) ) )
         print( self.outStr0 )

   def setTopCard( self, top ):
      self.topCard = top

   def getTopCard( self ):
      return self.topCard

class Hand:

   def __init__( self ):
      self.score = 0
      self.hand = []
      self.scoreList = []
      
   def countAces( self ):
      numAces = 0
      for i in range( 0, len( self.hand ) ):
         if self.hand[ i ].face == "Ace":
            numAces += 1
      return numAces
   
   def scoreHand( self ):
      self.score = 0
      for i in range( 0, len( self.hand ) ):
         self.score += self.hand[ i ].value

   def acesScoring( self ):
      a = self.countAces( )
      for i in range( 0, a + 1 ):
         if len( self.scoreList ) == i :
            self.scoreList.append( self.score - i * 10 )
         else:
            self.scoreList[ i ] = self.score - i * 10

      self. score = self.scoreList[ len( self.scoreList ) - 1 ]
      for i in range( len( self.scoreList ) - 1, -1, -1 ):
         if self.scoreList[ i ] <= 21:
            self. score = self.scoreList[ i ]

   def dispScore( self ):
      for i in range( 0, len( self.scoreList ) ):
         outStr1 = self.scoreList[ i ]
#         print( self.scoreList[ i ], " ", end="" )
#      print( '\n' )
         return( outStr1 )

   def dispHand( self ):
      for i in range( 0 , len( self.hand ) ):
         outStr2 = self.hand[i].face + " of " + self.hand[i].suit
#         print( "%s%s%s" % ( self.hand[i].face.rjust(5), " of ",
#                self.hand[i].suit.ljust(8) ) )
         return( outStr2 )

   def dispDealerHand( self ):
      outStr2 = self.hand[0].face + " of " + self.hand[0].suit + " FACEDOWN"
      #outStr3 = "FACEDOWN"
#      print( self.hand[0].face, " of ", self.hand[0].suit )
#      print( "FACEDOWN" )
      return( outStr2 )
      #print( outStr3 )

class Player:

   def __init__( self, name, stash ):
      self.playerHand = Hand( )
      self.name = name
      self.pocket = stash
      self.state = "PLAY"

#   def getPlayerPocket( self ):
#      return self.pocket

   def newHand( self, newHand ):
      self.playerHand = newHand

   def placeBet( self, betAmount ):
      self.pocket -= betAmount

   def winBet( self, winAmount ):
      self.pocket += winAmount

   def dispStash( self ):
      outStr4 = "Player Amount = $" + str( self.pocket )
#      print( "Player Amount = $", self.pocket )
      return( outStr4 )

class Bet:

   def __init__( self, betOdds ):
      self.amount = 0
      self.odds = betOdds
      self.payout = 0

#   def getBetAmount( self ):
#      return self.amount

   def setBetAmt( self, amount ):
      self.amount = amount

   def calcPayout( self ):
      self.payout = self.amount * self.odds

   def betInput( self, pocket ):
      
      impStr1 = "Place your bet -> $"
      '''
      outStr5 = "You are trying to bet more money than you have"
#      amount = eval( input( ", place your bet -> $" ) )
      amount = eval( input( impStr1 ) )
      while amount > pocket:
#         print( "You are trying to bet more money than you have" )
#         amount = eval( input( ", place your bet -> $" ) )
         print( outStr5 )
         amount = eval( input( impStr1 ) )
      '''
      
      #return amount

   def dispPayout( self ):
      outStr6 = "You won $" + str (self.payout )
#      print( "you won $", self.payout )
      print( outStr6 )

class Game:

   def __init__( self, playerx, playery ):
      self.player = playerx
      self.dealer = playery
      self.impStr2 = "Double Down? enter D or N -> "
      self.impStr3 = "Hit or Stand? enter H or S -> "
      self.impStr4 = "sPlit Hand? enter P or N -> "
      self.impStr5 = "sUrrender Hand? enter U or N -> "
      self.impStr6 = "Play another hand? enter Y or N -> "
      self.outStr20 = "You don't have enough money to double down"

   def initialDeal( self, deckx ):
      for i in range( deckx.topCard, deckx.topCard + 4, 2 ):
         self.player.playerHand.hand.append( deckx.deck[ i ] )
         self.dealer.playerHand.hand.append( deckx.deck[ i + 1 ] )
      deckx.setTopCard( i + 2 )

   def hit( self, playerx, deckx ):
      playerx.playerHand.hand.append( deckx.deck[ deckx.topCard ] )
      deckx.setTopCard( deckx.topCard + 1 )

   def playerInput( self, choice ):
      a = "x"
      while a.upper() != "D" and a.upper() != "H" and a.upper() != "N" \
                      and a.upper() != "P" and a.upper() != "S" \
                      and a.upper() != "U":
         if choice == "D":
#            a = input( "Double Down? enter D or N -> " )
            a = input( self.impStr2 )
#            if a.upper() == "D" and Player.getPlayerPocket() < 2 * Bet.getBetAmount():
#               print( outStr20 )
#               a = "N"            
         if choice == "H":
#            a = input( "Hit or Stand? enter H or S -> " )
            a = input( self.impStr3 )
         if choice == "P":
#            a = input( "sPlit Hand? enter P or N -> " )
            a = input( self.impStr4 )
         if choice == "U":
#            a = input( "sUrrender Hand? enter U or N -> " )
            a = input( self.impStr5 )
         a.upper()
      return a.upper()

   def playAgain( self ):
      a = "x"
      while a.upper() != "N" and a.upper() != "Y" :
#         a = input( "Play another hand? enter Y or N -> " )
         a = input( self.impStr6 )
         a.upper()
      return a.upper()
'''
class Application(Frame):
  #counter = 0
  #array = [[0 for x in range(18)] for x in range(18)]
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.grid()
    self.createLabels()
    #self.Enter_Bet()
    #self.createWidgets()
    #self.Loop()
    
  def Enter_Bet(self):
    root2 = tk()
    Number_Bet = StringVar()
    Money_Owned.set("2500")#Change to the amount of money needed
    
    #self.master.destroy()
    #quit()
  def quite(self, Selection):
    newSelection = Selection.get()
    
    print(newSelection)
  def DealersHand(self, hand):
     self.cell = Label(self, text = "Dealers Hand: " + hand).grid(row=1,column=1)
     
  def DealersTotal(self, total):
     self.cell = Label(self, text = "Total = " + total).grid(row=1,column=5)
     
  def PlayersHand(self,hand):
     self.cell = Label(self, text = "Players Hand: " + hand).grid(row=3,column=1)
     
  def PlayersTotal(self, total):
     self.cell = Label(self, text = "Total = " + total).grid(row=3,column=5)
     
  def PlayerName(self,name):
     self.cell = Label(self, text = "Player 1: " + name).grid(row=2,column=3)
     
  def createLabels(self):#this creates the grid of labels
        self.cell = Label(self, text = "Dealer:").grid(row=0,column=3)
    #Dealers Hand
        #1self.DealersHand("test")   #self.cell = Label(self, text = "DealerHand:").grid(row=1,column=1)
        #self.cell = Label(self, text = "Picture2 = ?").grid(row=1,column=2)
        #self.cell = Label(self, text = "Picture3 = ?").grid(row=1,column=3)
        #1self.DealersTotal()  #self.cell = Label(self, text = "Total = ?").grid(row=1,column=5)
    #Players Hand
           #self.cell = Label(self, text = "Player 1:(Change with actual name)").grid(row=2,column=3)
        #1self.PlayersHand()   #self.cell = Label(self, text = "PlayerHand").grid(row=3,column=1)
        #self.cell = Label(self, text = "Picture2 = ?").grid(row=3,column=2)
        #self.cell = Label(self, text = "Picture3 = ?").grid(row=3,column=3)
        #1self.PlayersHand()   #self.cell = Label(self, text = "Total = ?").grid(row=3,column=5)
    #If Player splits
        #self.cell = Label(self, text = "Player 1 SPLIT:(Change with actual name)").grid(row=4,column=3)
        #self.cell = Label(self, text = "Picture1 = ?").grid(row=5,column=1)
        #self.cell = Label(self, text = "Picture2 = ?").grid(row=5,column=2)
        #self.cell = Label(self, text = "Picture3 = ?").grid(row=5,column=3)
        #self.cell = Label(self, text = "Total = ?").grid(row=5,column=5)
    #Options:
        self.Buttons()
        #self.PlayerMoney()
  def Buttons(self):
     
     Selection = StringVar()
     Hit = Radiobutton(self, text='Hit', variable=Selection, value=1).grid(row=6,column=1)
     Surrender = Radiobutton(self, text='Surrender', variable=Selection, value=2).grid(row=6,column=2)
     Stand = Radiobutton(self, text='Stand', variable=Selection, value=3).grid(row=6,column=3)
     DoubleDown = Radiobutton(self, text='DoubleDown', variable=Selection, value=4).grid(row=6,column=4)
     Split = Radiobutton(self, text='Split', variable=Selection, value=5).grid(row=6,column=5) 
     BuyInsurance = Radiobutton(self, text='BuyInsurance', variable=Selection, value=6).grid(row=6,column=6)
     self.cell = Button(self, text = "Enter",command = lambda Selection = Selection, cvs = Selection: self.quite(cvs)).grid(row=8,column=3)
     self.cell = Label(self, text = "Amount won").grid(row=8,column=4)
     
  def PlayerMoney(self, stash):
     self.cell = Label(self, text = stash).grid(row=8,column=5)
     
'''
     
        

def UserPicked(Selection):
   print(Selection.get())
   '''
   if (Selection.get() == 1):
      Hit()
   else if(Selection.get() == 2):
      Surrender()
   else if (Selection.get() == 3):
      Stand()
   '''
   #else if (Selection.get() == 4
   return Selection.get()

def main():
   
   #root = Tk()
   global root
   #app = Application(root)
   
   #11111111111
   #impStr7 = "Enter number of decks to play with -> "
#   numDecks = eval( input( "Enter number of decks to play with -> " ) )
   #numDecks = eval( input( impStr7 ) )
   #11111111111
   print("1")
   numDecks = 2
   newDeck = Deck( numDecks )                            #Create deck(s) object
   newDeck.shuffleDeck( )                                      #Shuffle deck(s)
#   newDeck.dispDeck( 0, 16 )
   
   player = Player( "Adam", 1000 )                       #Create player objects
   dealer = Player( "Dealer", 1 )
   name = "Adam"
   cell = Label(root, text = "Player 1: " + name).grid(row=2,column=3)
   #app.PlayerName("Adam")
   newGame = Game( player, dealer)                          #Create game object
   #---------------------------------------      
   root.mainloop()     
   outStr7 = newGame.player.name + " Blackjack!"
   outStr8 = newGame.dealer.name + " Blackjack!"
   outStr9 = newGame.player.name + " Wins!"
   outStr10 = newGame.dealer.name + " Wins!"
   outStr19 = newGame.player.name + " loses!" 
   outStr11 = newGame.player.name + "Busted!"
   outStr12 = newGame.dealer.name + "Busted!"
   outStr16 = newGame.player.name + " is surrendering this hand"
   outStr17 = "Push - " + newGame.player.name + "'s bet returned"
   outStr18 = "Not enough cards are left in the deck to play another hand"

   Selection = StringVar()
   Hit = Radiobutton(root, text='Hit', variable=Selection, value=1).grid(row=6,column=1)
   Surrender = Radiobutton(root, text='Surrender', variable=Selection, value=2).grid(row=6,column=2)
   Stand = Radiobutton(root, text='Stand', variable=Selection, value=3).grid(row=6,column=3)
   DoubleDown = Radiobutton(root, text='DoubleDown', variable=Selection, value=4).grid(row=6,column=4)
   Split = Radiobutton(root, text='Split', variable=Selection, value=5).grid(row=6,column=5) 
   BuyInsurance = Radiobutton(root, text='BuyInsurance', variable=Selection, value=6).grid(row=6,column=6)
   UsersPick = Button(root, text = "Enter",command = lambda Selection = Selection, cvs = Selection: UserPicked(cvs)).grid(row=8,column=3)
   cell = Label(root, text = "Amount won:").grid(row=8,column=4)
   
   play = "Y"
   while play == "Y" and newDeck.topCard < ( numDecks * ( 52 - 20 ) ):
      action = " "
      newGame.initialDeal( newDeck )
   
      playerBet = Bet( 1.5 )           #get bet from player - create bet object
      cell = Label(root, text = player.dispStash()).grid(row=8,column=5)
      #app.PlayerMoney(player.dispStash()) #BRADY:returns amount of money they have
#      print( newGame.player.name, end = "" )

########Change betInput
      '''
      impStr1 = "Place your bet -> $"
      outStr5 = "You are trying to bet more money than you have"
#      amount = eval( input( ", place your bet -> $" ) )
      amount = eval( input( impStr1 ) )
      amount = playerBet.betInput( player.pocket )
      while amount > pocket:
#         print( "You are trying to bet more money than you have" )
#         amount = eval( input( ", place your bet -> $" ) )
         print( outStr5 )
         amount = eval( input( impStr1 ) )
       #still prints to screen
      '''
      
      amt = 12
      #amount = playerBet.betInput( player.pocket )#BRADY:change this to read the text field of the bet
      playerBet.setBetAmt( amt )
      player.placeBet( amt )

#      print( '\n', newGame.player.name )            #Display 2 card player hand
      cell = Label(root, text = "Players Hand: " + player.playerHand.dispHand( )).grid(row=3,column=1)
      #app.PlayersHand(player.playerHand.dispHand( )) #BRADY:returns the hand the user has
      player.playerHand.scoreHand( )
      player.playerHand.acesScoring( )
      
      cell = Label(root, text = "Total = " + str(player.playerHand.dispScore( ))).grid(row=3,column=5)
      #app.PlayerTotal(player.playerHand.dispScore( )) #BRADY:returns the score of the player



#      print( '\n', newGame.dealer.name )#Disp 1 card up, 1 card down dealer hand

      cell = Label(root, text = "Dealers Hand: " + dealer.playerHand.dispDealerHand( )).grid(row=1,column=1)
      #print(dealer.playerHand.dispDealerHand( )) #BRADY:returns the dealers hand
      
      
      if player.playerHand.score == 21:                  #Player has a Blackjack
#         print( '\n', newGame.player.name, " Blackjack!", '\n' )
         print( outStr7 )

      dealer.playerHand.scoreHand( )
      if player.playerHand.score == 21 and dealer.playerHand.score == 21:
                                             #Dealer also has a Blackjack - push
         
         cell = Label(root, text = "Dealers Hand: " + dealer.playerHand.dispHand( )).grid(row=1,column=1)
         #print(dealer.playerHand.dispHand( )) #BRADY:returns the dealers hand
#         print( '\n', newGame.dealer.name, " Blackjack!", '\n' )
         print( outStr8 ) #BlackJack
         player.state = "PUSH"

      if player.playerHand.score == 21 and dealer.playerHand.score <= 21:
         dealer.playerHand.dispHand( )
#         print( newGame.player.name, " Wins!" )
         print( outStr9 ) #BRADY:BlackJack
         player.state = "WIN"
         
########## SPLIT ##############################################################
      if player.state == "PLAY":                                #not a blackjack
         if player.playerHand.hand[0].face == player.playerHand.hand[1].face:
            #action = newGame.playerInput( "P" )#BRADY:comment out
            if UsersPick == 5:#BRADY:if certian radiobox
               
               outStr15 = newGame.player.name + " is splitting his " + player.playerHand.hand[0].face + "'s"
               player.state = "SPLIT"
#               print( newGame.player.name, " is splitting his ",
#               player.playerHand.hand[0].face, "'s", '\n' )
               print( outStr15 )#BRADY:comment out
            
########## SURRENDER ##########################################################            
      if player.state == "PLAY":                                #not a blackjack
         #action = newGame.playerInput( "U" )#BRADY:comment out
         if UsersPick == 2:#BRADY:if certian radiobox
            player.state = "SURRENDER"
#            print( newGame.player.name, " is surrendering this hand" )
            print( outStr16 )#BRADY:comment out
          
########## DOUBLE DOWN ########################################################
      if player.state == "PLAY":                         #Player not a blackjack
         #action = newGame.playerInput( "D" )#BRADY:comment out
         if UsersPick == 4:#BRADY:if certian radiobox
            player.state = "DOUBLEDOWN"
            playerBet.setBetAmt( 2 * amt )                    #Double bet amount
            player.placeBet( amt )  #take from player's stash another bet amount
#            print( '\n', newGame.player.name )
            newGame.hit( player, newDeck )
            #print(player.playerHand.dispHand( ))#BRADY:returns the hand the user has
            cell = Label(root, text = "Players Hand: " + player.playerHand.dispHand( )).grid(row=3,column=1)
            player.playerHand.scoreHand( )
            player.playerHand.acesScoring( )
            #print(player.playerHand.dispScore( ))
            cell = Label(root, text = "Total = " + str(player.playerHand.dispScore( ))).grid(row=3,column=5)
            if player.playerHand.score > 21:                      #Player busted
#               print( '\n', newGame.player.name, "Busted!" )
#               print( newGame.dealer.name, " Wins!", '\n' )
               print( outStr11 + outStr10 )
               #print( outStr10 )
               player.state = "LOSE"
            
########## PLAYER GAME PLAY ###################################################
      if player.state == "PLAY":                      #no change from above code
         action = newGame.playerInput( "H" )#BRADY:comment out                 #play player's hand
         while UsersPick == 1 and player.playerHand.score < 21:#BRADY:if certain radiobox
#            print( '\n', newGame.player.name )
            newGame.hit( player, newDeck )
            #print(player.playerHand.dispHand( ))#BRADY:returns the hand the user has
            cell = Label(root, text = "Players Hand: " + player.playerHand.dispHand( )).grid(row=3,column=1)
            
            player.playerHand.scoreHand( )
            player.playerHand.acesScoring( )
            #print(player.playerHand.dispScore( ))
            cell = Label(root, text = "Total = " + str(player.playerHand.dispScore( ))).grid(row=3,column=5)
            
            #if player.playerHand.score < 21:            #Player still not busted
               #action = newGame.playerInput( "H" )#BRADY:comment out
            if player.playerHand.score > 21:                      #Player busted
#               print( '\n', newGame.player.name, "Busted!" )
#               print( newGame.dealer.name, " Wins!", '\n' )
               print( outStr11 + outStr10 )
               #print( outStr10 )
               player.state = "LOSE"

########## DEALER GAME PLAY ###################################################               
      if player.state == "PLAY" or player.state == "DOUBLEDOWN":
                                    #if player's not busted, show dealer's hand
         #print( '\n', newGame.dealer.name )
         
         #print(dealer.playerHand.dispHand( ))#BRADY:returns the hand the dealer has
         cell = Label(root, text = "Dealers Hand: " + dealer.playerHand.dispHand( )).grid(row=1,column=1)
         
         dealer.playerHand.scoreHand( )
         dealer.playerHand.acesScoring( )
         
         #print(dealer.playerHand.dispScore( ))
         cell = Label(self, text = "Total = " + dealer.playerHand.dispScore( )).grid(row=1,column=5)
         
                                     #player's score <= 21, dealer's score < 17
         while dealer.playerHand.score < 17:
            newGame.hit( dealer, newDeck )
            
            #print(dealer.playerHand.dispHand( ))#BRADY:returns the hand the dealer has
            cell = Label(root, text = "Dealers Hand: " + dealer.playerHand.dispHand( )).grid(row=1,column=1)
            
            dealer.playerHand.scoreHand( )
            dealer.playerHand.acesScoring( )
            
            #print(dealer.playerHand.dispScore( ))
            cell = Label(self, text = "Total = " + dealer.playerHand.dispScore( )).grid(row=1,column=5)
            
            if dealer.playerHand.score > 21:         #Dealer busts - player wins
#               print( '\n', newGame.dealer.name, "Busted!" )
#               print( newGame.player.name, " Wins!" )
               print( outStr12 )
               print( outStr9 )
               player.state = "WIN"
                                                 #neither player or dealer busts
         if player.playerHand.score <= 21 and dealer.playerHand.score <= 21:
            if player.playerHand.score <= dealer.playerHand.score:
                                                     #dealer wins - player loses
#               print( newGame.player.name, " Loses", '\n' )
               print( outStr19 )
               player.state = "LOSE"
            else:                                    #player wins - dealer loses
#               print( newGame.player.name, " Wins!" )
               print( outStr9 )
               player.state = "WIN"
              
########## SETTLE UP WITH PLAYER ###############################################
      if player.state == "LOSE":
#         print( newGame.player.name, " loses $", playerBet.amount )
         outStr13 = newGame.player.name + " loses $" + str( playerBet.amount )
         print( outStr13 )
         
         #print(player.dispStash( ))
         cell = Label(root, text = player.dispStash()).grid(row=8,column=5)

      if player.state == "WIN":
         playerBet.calcPayout( )
         outStr14 = newGame.player.name + " wins $" + str( playerBet.payout )
#         print( newGame.player.name, " wins $", playerBet.payout )
         print( outStr14 )                       #return winnings + original bet
         player.winBet( playerBet.payout + playerBet.amount )
         
         print(player.dispStash( ))
         cell = Label(root, text = player.dispStash()).grid(row=8,column=5)

      if player.state == "PUSH":
#         print( '\n', "Push - ", newGame.player.name, "'s bet returned" )
         print( outStr17 )
         player.winBet( playerBet.amount )            #return bet amount on push
         print(player.dispStash( ))

      if player.state == "SURRENDER":
         player.winBet( playerBet.amount / 2 )   #return 1/2 of bet on surrender
         print(player.dispStash( ))
      
      play = newGame.playAgain( )#still prints in this
      if play == "Y":
         hand1 = Hand( )
         hand2 = Hand( )
         newGame.player.playerHand = hand1
         newGame.dealer.playerHand = hand2
         player.state = "PLAY"

   if play == "Y":###delete everything after this
#      print( "Not enough cards are left in the deck to play another hand" )
      print( outStr18 )
   
main()
