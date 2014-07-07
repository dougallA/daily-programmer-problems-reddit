"""
(Easy): Blackjack Checker

Blackjack is a very common card game, where the primary aim is to pick up cards until your hand has a higher value than everyone else but is less than 21. This challenge will look at the outcome of the game, rather than playing the game itself.

The value of a hand is determined by the cards in it.

    Numbered cards are worth their number - eg. a 6 of Hearts is worth 6.

    Face cards (JQK) are worth 10.

    Ace can be worth 1 or 11.

The person with the highest valued hand wins, with one exception - if a person has 5 cards in their hand and it has any value 21 or less, then they win automatically. This is called a 5 card trick.

If the value of your hand is worth over 21, you are 'bust', and automatically lose.

Your challenge is, given a set of players and their hands, print who wins (or if it is a tie game.)
Input Description

First you will be given a number, N. This is the number of players in the game.

Next, you will be given a further N lines of input. Each line contains the name of the player and the cards in their hand, like so:

Bill: Ace of Diamonds, Four of Hearts, Six of Clubs

Would have a value of 21 (or 11 if you wanted, as the Ace could be 1 or 11.)
Output Description

Print the winning player. If two or more players won, print "Tie".
Example Inputs and Outputs
Example Input 1

3
Alice: Ace of Diamonds, Ten of Clubs
Bob: Three of Hearts, Six of Spades, Seven of Spades
Chris: Ten of Hearts, Three of Diamonds, Jack of Clubs

Example Output 1

Alice has won!

Example Input 2

4
Alice: Ace of Diamonds, Ten of Clubs
Bob: Three of Hearts, Six of Spades, Seven of Spades
Chris: Ten of Hearts, Three of Diamonds, Jack of Clubs
David: Two of Hearts, Three of Clubs, Three of Hearts, Five of Hearts, Six of Hearts

Example Output 2

David has won with a 5-card trick!

Notes

Here's a tip to simplify things. If your programming language supports it, create enumerations (enum) for card ranks and card suits, and create structures/classes (struct/class) for the cards themselves - see this example C# code.

For resources on using structs and enums if you haven't used them before (in C#): structs, enums.

You may want to re-use some code from your solution to this challenge where appropriate.
"""

class Card:
    def __init__(self, card_str):
        """ 
        card_str is of the form "Jack of Hearts" or "Six of Clubs"
        """
        


