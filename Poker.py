
import random


# Deck class creates and manages playing cards
class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "Jack", "Queen", "King"]

        self.cards = []

        for suit in suits:
            for rank in ranks:
                self.cards.append(rank + " of " + suit)

        random.shuffle(self.cards)

    # Deal one card from the deck
    def deal_card(self):
        return self.cards.pop()


# Display the five cards in the player's hand
def show_hand(hand):
    print("\nYour cards:")

    for i in range(len(hand)):
        print(str(i + 1) + ". " + hand[i])


# Ask the player which cards to replace
def get_replacements():
    while True:
        choice = input(
            "\nEnter card numbers to replace (example: 1, 3, 5): "
        )

        try:
            numbers = []

            for item in choice.split(","):
                number = int(item.strip())

                if number < 1 or number > 5:
                    raise ValueError

                if number in numbers:
                    raise ValueError

                numbers.append(number)

            return numbers

        except ValueError:
            print("Invalid input. Enter numbers 1 through 5.")


# Replace the selected cards with new cards
def replace_cards(hand, deck, numbers):
    for number in numbers:
        hand[number - 1] = deck.deal_card()


# Main program
def main():
    deck = Deck()
    hand = []

    # Deal the first five cards
    for i in range(5):
        hand.append(deck.deal_card())

    print("Welcome to Five Card Poker!")

    show_hand(hand)

    # Get the cards the player wants to replace
    numbers = get_replacements()

    # Draw new cards
    replace_cards(hand, deck, numbers)

    print("\nYour new poker hand:")
    show_hand(hand)

    print("\nThanks for playing!")


# Run the program
if __name__ == "__main__":
    main()
