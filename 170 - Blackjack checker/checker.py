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
"""
This is intended for python 3.4 or higher, as I am using enumerators.
"""
import re
class Card:
    card_values = {'Ace': 11, #Handle this special case later
                   'Two': 2, 'Three': 3,'Four': 4,'Five': 5,
                   'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
                   'Ten': 10,'Jack': 10, 'Queen': 10, 'King': 10}
    def __init__(self, card_str):
        """ 
        card_str is of the form "Jack of Hearts" or "Six of Clubs"
        """
        self.rank = self.card_values[card_str.split()[0]]
        self.suit = card_str.split()[2]

class Hand: 
    
    """
    A hand consists of several cards that add up to a value.
    """
    def raw_score(self, values):
        total = 0
        for value in values:
            total += value
        if total > 21:
            return 'bust'
        return total

    def make_score(self):
        """
        Calculates the best possible score of the cards.
        """
        values = [ card.rank for card in self.cards]
        total = 0        
        if 11 not in values:
            total = self.raw_score(values)
        else: 
            ace_locations = [n[0] for n in enumerate(values) if n[1] == 11]
            if self.raw_score(values) is not 'bust':
                total = self.raw_score(values)
            else: #Need to try scaling 11's back to 1's one at a time.
                for location in ace_locations:
                    values[location] = 1
                    total = self.raw_score(values)
                    if self.raw_score(values) is not 'bust':
                        break
        if len(values) == 5 and total is not 'bust':
            return '5-card trick'
        else:
            return total    

    def __init__(self, hand_str):
        """
        hand_str will be of the form 
        'Alice: Ace of Diamonds, Ten of Clubs'
        """
        card_pattern = re.compile(r'\w+\sof\s\w+')
        self.hand_owner = hand_str.split()[0].strip(':')
        self.cards = [Card(card_str) for card_str in re.findall(card_pattern, hand_str)]

def determine_winner(list_of_hands):
    scores = [hand.make_score() for hand in list_of_hands]
    five_card_trick_exists = False
    five_card_tricks = [ hand for hand in list_of_hands 
                         if hand.make_score() == '5-card trick']
    if len(five_card_tricks) > 1:
        return 'Tie'
    best_score = 0
    for score in scores:
        if score == '5-card trick':
            best_score = '5-card trick'
            
            break
        elif score is not 'bust' and score > best_score:
            best_score = score
    winning_hand_indices = [i for i, hand in enumerate(list_of_hands) 
                            if hand.make_score() == best_score]
    if best_score == 0:
        return 'Everyone busts'
    elif len(winning_hand_indices) > 1:
        return 'Tie'
    else:
        return ("The winner is: " 
                + list_of_hands[winning_hand_indices[0]].hand_owner)
    

if __name__ == "__main__":
    hands = []
    for i in range(int(input("How many players are in the game? "))):
        hands.append(Hand(input("Enter player and their cards: ")))
    print(determine_winner(hands))

