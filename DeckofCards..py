#Jason Lambert
#CSI261
#DeckofCards

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
                 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.deck = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, num_cards):
        dealt_cards = self.deck[:num_cards]
        self.deck = self.deck[num_cards:]
        return dealt_cards

    def cards_left(self):
        return len(self.deck)

# Main program
def main():
    print("Card Dealer\n")
    deck = Deck()
    deck.shuffle()
    print("I have shuffled a deck of 52 cards.\n")

    try:
        num = int(input("How many cards would you like ?: "))
        if num < 1 or num > 52:
            print("Please enter a number between 1 and 52.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    print("\nHere are your cards:")
    hand = deck.deal(num)
    for card in hand:
        print(card)

    print(f"\nThere are {deck.cards_left()} cards left in the deck.")
    print("\nGood luck!")
    input("Press any key to continue\n")
    print("Saving Your Work")

if __name__ == "__main__":
    main()