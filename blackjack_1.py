# blackjack.py

from random import shuffle

faces = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace" )
suits = ( "Clubs", "Diamonds", "Hearts", "Spades" )
values = ( 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11 )

class Card:

   def __init__( self, face, suit, value ):
      self.face = face
      self.suit = suit
      self.value = value

class Deck:

   def __init__( self, numDecks ):
      self.deck = []
      for k in range( 0, numDecks ):
         for i in range( 0, 4 ):
            for j in range( 0, 13 ):
               self.deck.append( Card( faces[j], suits[i], values[j] ) )

   def shuffleDeck( self ):
      shuffle( self.deck )

   def dispDeck( self, start, stop ):
      for i in range( start, stop ):
         print( self.deck[ i ].face, " of ", self.deck[ i ].suit )

class Hand:

   def __init__( self ):
      self.hand = []

class Play:

   def __init__( self ):
      self.player1Hand = Hand
      self.dealerHand = Hand

   def initialDeal( self, deck ):
      for i in range( 0, 4, 2 ):
         self.player1Hand.append( deck[ i ] )
         self.dealerHand.append( deck[ i + 1 ] )
                  
      

      

def main():
   print( "In Main\n" )
   newDeck = Deck( 2 )
   newDeck.shuffleDeck( )
   newDeck.dispDeck( 0, 104 )

   newPlay = Play( )
   newPlay.initialDeal( newDeck )
main()
      

   
      
