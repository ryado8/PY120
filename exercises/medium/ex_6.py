import random


class Card:
    VALUES = {
        "Jack": 11,
        "Queen": 12,
        "King": 13,
        "Ace": 14,
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def value(self):
        return Card.VALUES.get(self.rank, self.rank)

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        return self.value < other.value

    def __gt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        return self.value > other.value

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        return self.rank == other.rank and self.suit == other.suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    RANKS = list(range(2, 11)) + ["Jack", "Queen", "King", "Ace"]
    SUITS = ["Hearts", "Clubs", "Diamonds", "Spades"]

    def __init__(self):
        self.cards = []
        self._setup_new_deck()

    def _setup_new_deck(self):
        self.cards = [Card(rank, suit) for rank in Deck.RANKS for suit in Deck.SUITS]

        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            self._setup_new_deck()

        return self.cards.pop()


class PokerHand:
    def __init__(self, deck):
        self.hand = [deck.draw() for _ in range(5)]
        self.ranks = self._get_ranks()
        self.suits = self._get_suits()
        self.unique_ranks = set(self.ranks)

    def print(self):
        for card in self.hand:
            print(card)

    def _get_ranks(self):
        return [card.rank for card in self.hand]

    def _get_suits(self):
        return [card.suit for card in self.hand]

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
            return "High card"

    def _is_royal_flush(self):
        return {"Ace", "King", "Queen", "Jack", 10} == set(self.ranks) and self._is_flush()

    def _is_straight_flush(self):
        return self._is_straight() and self._is_flush()

    def _is_n_of_a_kind(self, num):
        return len([rank for rank in self.unique_ranks if self.ranks.count(rank) == num]) == 1

    def _is_four_of_a_kind(self):
        return self._is_n_of_a_kind(4)

    def _is_full_house(self):
        return self._is_three_of_a_kind() and self._is_pair()

    def _is_flush(self):
        return len(set(self.suits)) == 1

    def _is_straight(self):
        sorted_hand = sorted(self.hand, key = lambda card: card.value)

        for idx in range(len(sorted_hand) - 1):
            if sorted_hand[idx].value + 1 != sorted_hand[idx + 1].value:
                return False

        return True

    def _is_three_of_a_kind(self):
        return self._is_n_of_a_kind(3)

    def _is_two_pair(self):
        return len([rank for rank in self.unique_ranks if self.ranks.count(rank) == 2]) == 2

    def _is_pair(self):
        return self._is_n_of_a_kind(2)



hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes


class TestDeck(Deck):
    def __init__(self, cards):
        self.cards = cards


# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")
