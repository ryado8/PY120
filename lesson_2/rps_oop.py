import random
import os


class Move:
    WINNING_MOVES = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "spock": ["rock", "scissors"],
        "lizard": ["spock", "paper"],
    }

    def __init__(self):
        self._name = None

    def __str__(self):
        return self._name

    def __gt__(self, other):
        if not isinstance(other, Move):
            return NotImplemented

        return other._name in Move.WINNING_MOVES[self._name]

    def __lt__(self, other):
        if not isinstance(other, Move):
            return NotImplemented

        return self._name in Move.WINNING_MOVES[other._name]


class Rock(Move):
    def __init__(self):
        self._name = "rock"


class Paper(Move):
    def __init__(self):
        self._name = "paper"


class Scissors(Move):
    def __init__(self):
        self._name = "scissors"


class Lizard(Move):
    def __init__(self):
        self._name = "lizard"


class Spock(Move):
    def __init__(self):
        self._name = "spock"


class Player:
    CHOICES = (Rock(), Paper(), Scissors(), Lizard(), Spock())

    def __init__(self):
        self.move = None


class Human(Player):
    CHOICE_DISPLAY = [
        (
            f"({choice._name[:2]}){choice._name[2:]}"
            if choice._name == "spock"
            else f"({choice._name[0]}){choice._name[1:]}"
        )
        for choice in Player.CHOICES
    ]

    def __init__(self):
        super().__init__()

    def choose(self):
        player_move = input(
            f"Choose a move - {", ".join(self.__class__.CHOICE_DISPLAY)}: "
        ).lower()
        self.move = player_move


class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)


class MatchHistory:
    def __init__(self):
        self._player_moves = []
        self._computer_moves = []

    def _update(self, player_move, computer_move):
        self._player_moves.append(player_move)
        self._computer_moves.append(computer_move)

    def __str__(self):
        return "".join(
            [
                f"Match {idx + 1}: Player chose {self._player_moves[idx]}, Computer chose {self._computer_moves[idx]}\n"
                for idx in range(len(self._player_moves))
            ]
        )


class RPSGame:
    WINNING_SCORE = 5
    CHOICE_DICT = {
        "r": "rock",
        "p": "paper",
        "s": "scissors",
        "l": "lizard",
        "sp": "spock",
    }
    VALID_CHOICES = tuple(CHOICE_DICT.keys()) + tuple(CHOICE_DICT.values())

    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._score = {"player": 0, "computer": 0}
        self._history = MatchHistory()

    def _press_to_continue(self):
        print()
        input("Press enter to continue: ")

    def _display_match_history(self):
        self._clear_screen()
        print(self._history)

    def _continue_or_display_history(self):
        print()
        while True:
            answer = input(
                "Enter 'h' for match history or press enter to continue: "
            ).lower()

            if answer in ("history", "h"):
                self._display_match_history()
            else:
                break

    def _display_welcome_message(self):
        self._clear_screen()
        print(
            f"Welcome to Rock Paper Scissors Lizard Spock! The first to {self.__class__.WINNING_SCORE} points wins!"
        )
        self._press_to_continue()

    def _display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors Lizard Spock. Goodbye!")

    def _clear_screen(self):
        os.system("clear")

    def _clear_screen_with_display(self):
        os.system("clear")
        self._display_score()

    def _display_score(self):
        print(f"Player: {self._score["player"]}   |")
        print(f"Computer: {self._score["computer"]} |")
        print("-------------")

    def _display_winner(self):
        self._clear_screen_with_display()
        print(f"You chose: {self._human.move}")
        print(f"The computer chose: {self._computer.move}")

        if self._human_wins():
            print("You win!")
        elif self._computer_wins():
            print("Computer wins!")
        else:
            print("It's a tie!")

    def _human_wins(self):
        return self._human.move > self._computer.move

    def _computer_wins(self):
        return self._human.move < self._computer.move

    def _game_over(self):
        return max(self._score.values()) == self.__class__.WINNING_SCORE

    def _update_score_and_history(self):
        if self._human_wins():
            self._score["player"] += 1
        elif self._computer_wins():
            self._score["computer"] += 1

        self._history._update(self._human.move, self._computer.move)

    def _reset_score(self):
        for player in self._score:
            self._score[player] = 0

    def _convert_move_to_obj(self, move):
        for choice in Player.CHOICES:
            if move == choice._name:
                return choice

    def _validate_move(self, move):
        while move not in self.__class__.VALID_CHOICES:
            move = input(
                f"Invalid move. Choose a move - {", ".join(Human.CHOICE_DISPLAY)}: "
            ).lower()

        move = (
            self.__class__.CHOICE_DICT[move]
            if move in self.__class__.CHOICE_DICT
            else move
        )
        return self._convert_move_to_obj(move)

    def _validate_answer(self, answer):
        while answer not in ("y", "n", "yes", "no"):
            answer = input(
                "Invalid answer. Would you like to play again? (y/n):"
            ).lower()

        return answer

    def _play_again(self):
        self._clear_screen()
        answer = self._validate_answer(
            input("Would you like to play again? (y/n): ").lower()
        )
        return answer in ("y", "yes")

    def play(self):
        self._display_welcome_message()

        while True:
            self._reset_score()

            while not self._game_over():
                self._clear_screen_with_display()
                self._human.choose()
                self._human.move = self._validate_move(self._human.move)
                self._computer.choose()
                self._update_score_and_history()
                self._display_winner()
                self._continue_or_display_history()

            if not self._play_again():
                break

        self._display_goodbye_message()


game = RPSGame()
game.play()
