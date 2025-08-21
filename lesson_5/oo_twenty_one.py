import random
import os


def prompt(msg):
    print(f"==> {msg}")


def clear_screen():
    os.system("clear")


def display_underline():
    prompt("--------------------------------")


def press_to_continue():
    print()
    input("Press enter to continue: ")


class Card:
    FACE_CARDS = ("J", "Q", "K")
    FACE_VALUE = 10
    ACE_VALUE = 11

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def stringify(self):
        return f"{self.rank}{self.suit}"

    def value(self):
        if self.rank in self.__class__.FACE_CARDS:
            return self.__class__.FACE_VALUE

        if self.rank == "A":
            return self.__class__.ACE_VALUE

        return self.rank


class Deck:
    RANKS = tuple(range(2, 11)) + ("J", "Q", "K", "A")
    SUITS = ("♥", "♦", "♣", "♠")

    def __init__(self):
        self.reset()

    def reset(self):
        cards = [
            Card(rank, suit)
            for rank in self.__class__.RANKS
            for suit in self.__class__.SUITS
        ]
        random.shuffle(cards)
        self.cards = cards

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, cards):
        self._cards = cards

    def deal_card(self, participant):
        participant.hand.append(self.cards.pop())


class Participant:
    def __init__(self):
        self._hand = []

    @property
    def hand(self):
        return self._hand

    def convert_to_str(self, hand):
        return [card.stringify() for card in hand]

    def hand_value(self):
        ranks = [card.rank for card in self.hand]
        total = sum([card.value() for card in self.hand])

        for _ in range(ranks.count("A")):
            if total > TwentyOneGame.TWENTY_ONE:
                total -= Card.FACE_VALUE

        return total

    def is_busted(self):
        return self.hand_value() > TwentyOneGame.TWENTY_ONE

    def join_hand(self):
        return ", ".join((self.convert_to_str(self.hand)))

    def reset_hand(self):
        self.hand.clear()


class Player(Participant):
    def __init__(self, balance):
        super().__init__()
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    def increase_balance(self):
        self.balance += 1

    def decrease_balance(self):
        self.balance -= 1

    def reset_balance(self, balance):
        self.balance = balance

    def is_broke(self):
        return self.balance == 0

    def is_rich(self):
        return self.balance == 10


class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self._hidden = None

    def hide_card(self):
        self._hidden = True

    def reveal_card(self):
        self._hidden = False

    def join_hand(self):
        if self._hidden:
            return ", ".join([self.hand[0].stringify(), "[hidden]"])

        return super().join_hand()

    def hand_value(self):
        if self._hidden:
            return "unknown"

        return super().hand_value()


class TwentyOneGame:
    PLAYER_BALANCE = 5
    DEALER_STAY = 17
    TWENTY_ONE = 21

    def __init__(self):
        self.deck = Deck()
        self.player = Player(TwentyOneGame.PLAYER_BALANCE)
        self.dealer = Dealer()

    @staticmethod
    def _validate_decision(decision):
        while decision not in ("h", "hit", "s", "stay"):
            prompt("Not a valid decision. Would you like to (h)it or (s)tay?")
            decision = input().strip().lower()

        return decision

    @staticmethod
    def _validate_answer(answer):
        while answer not in ("y", "yes", "n", "no"):
            prompt("Not a valid answer. Would you like to play again (y/n)?")
            answer = input().strip().lower()

        return answer

    def deal_cards(self):
        for _ in range(2):
            self.deck.deal_card(self.player)
            self.deck.deal_card(self.dealer)

    def display_hands(self):
        prompt(f"Dealer's hand: {self.dealer.join_hand()}")
        prompt(f"Player's hand: {self.player.join_hand()}")
        display_underline()

    def display_hand_values(self):
        prompt(f"Dealer's total is {self.dealer.hand_value()}")
        prompt(f"Player's total is {self.player.hand_value()}")
        display_underline()

    def main_screen(self):
        clear_screen()
        self.display_balance()
        display_underline()
        self.display_hands()
        self.display_hand_values()

    def reshuffle_if_low(self):
        # allows dealing up to 40 cards (~75% penetration) before reshuffle.
        cards_left = len(self.deck.cards)
        if cards_left <= 12:
            clear_screen()
            prompt(f"There are only {cards_left} cards left in the deck.")
            prompt("Shuffling new deck for the next round...")
            press_to_continue()
            self.deck.reset()

    def new_round(self):
        self.dealer.hide_card()
        self.dealer.reset_hand()
        self.player.reset_hand()
        self.reshuffle_if_low()

    def player_turn(self):
        while True:
            self.main_screen()
            prompt("Would you like to (h)it or (s)tay? ")
            decision = input().strip().lower()
            decision = TwentyOneGame._validate_decision(decision)

            if decision in ("hit", "h"):
                self.deck.deal_card(self.player)

            if self.player.is_busted() or (decision in ("s", "stay")):
                break

        self.main_screen()
        if decision in ("s", "stay"):
            prompt("Player decides to stay.")
            press_to_continue()

    def dealer_turn(self):
        self.dealer.reveal_card()

        while True:
            if self.player.is_busted():
                break

            self.main_screen()

            if self.dealer.hand_value() >= TwentyOneGame.DEALER_STAY:
                break

            if self.dealer.hand_value() < TwentyOneGame.DEALER_STAY:
                prompt("Dealer hits.")
                self.deck.deal_card(self.dealer)
                press_to_continue()

        self.main_screen()

    def display_welcome_message(self):
        clear_screen()
        prompt("Welcome to Twenty One!")
        prompt(
            f"Your player balance is ${self.player.balance}. "
            "Each round requires a bet of $1."
        )
        prompt("The game will end when you go broke "
               "or increase your balance to $10.")
        prompt("Good luck!")
        press_to_continue()

    def display_goodbye_message(self):
        clear_screen()
        prompt("Thank you for playing. See you next time!")

    def determine_result(self):
        result = ''

        if self.player.is_busted():
            result = "player_bust"
        elif self.dealer.is_busted():
            result = "dealer_bust"
        elif self.player.hand_value() > self.dealer.hand_value():
            result = "player_win"
        elif self.dealer.hand_value() > self.player.hand_value():
            result = "dealer_win"
        else:
            result = "tie"

        return result

    def update_balance(self):
        match self.determine_result():
            case "player_bust":
                self.player.decrease_balance()
            case "dealer_bust":
                self.player.increase_balance()
            case "player_win":
                self.player.increase_balance()
            case "dealer_win":
                self.player.decrease_balance()

    def display_result(self):
        self.main_screen()

        match self.determine_result():
            case "player_bust":
                prompt("Player busts. Dealer wins!")
            case "dealer_bust":
                prompt("Dealer busts. Player wins!")
            case "player_win":
                prompt("Player wins!")
            case "dealer_win":
                prompt("Dealer wins!")
            case "tie":
                prompt("It's a tie!")

        press_to_continue()

    def display_balance(self):
        prompt(f"Player's current balance: ${self.player.balance}")

    def play_again(self):
        prompt("Would you like to play again (y/n)?")
        answer = input().strip().lower()
        answer = TwentyOneGame._validate_answer(answer)

        return answer in ("yes", "y")

    def start(self):
        self.display_welcome_message()

        while True:
            self.player.reset_balance(TwentyOneGame.PLAYER_BALANCE)

            while not (self.player.is_broke() or self.player.is_rich()):
                self.new_round()
                self.deal_cards()
                self.player_turn()
                self.dealer_turn()
                self.update_balance()
                self.display_result()

            if not self.play_again():
                break

        self.display_goodbye_message()


game = TwentyOneGame()
game.start()
