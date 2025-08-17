import random
import os


class MoveDisplayMixin:
    def display_moves(self, moves):
        freq_dict = {}
        result = []

        for name in moves:
            first_char = name[0].lower()
            freq_dict[first_char] = freq_dict.get(first_char, 0) + 1

            idx = freq_dict[first_char]
            result.append(f"({name[:idx]}){name[idx:]}")

        return ", ".join(result)


class Move:
    MOVE_DICT = {
        "r": "rock",
        "p": "paper",
        "s": "scissors",
        "l": "lizard",
        "sp": "spock",
    }
    VALID_MOVES = tuple(MOVE_DICT.keys()) + tuple(MOVE_DICT.values())
    WINNING_MOVES = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "spock": ["rock", "scissors"],
        "lizard": ["spock", "paper"],
    }

    def __init__(self):
        self._name = ""

    @property
    def name(self):
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
        super().__init__()
        self._name = "rock"


class Paper(Move):
    def __init__(self):
        super().__init__()
        self._name = "paper"


class Scissors(Move):
    def __init__(self):
        super().__init__()
        self._name = "scissors"

class Lizard(Move):
    def __init__(self):
        super().__init__()
        self._name = "lizard"


class Spock(Move):
    def __init__(self):
        super().__init__()
        self._name = "spock"

class Player:
    MOVES = (Rock(), Paper(), Scissors(), Lizard(), Spock())
    MOVE_NAMES = [move.name for move in MOVES]

    def __init__(self):
        self.move = None


class Human(MoveDisplayMixin, Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        player_move = input(
            f"Choose a move - {self.display_moves(Player.MOVE_NAMES)}: "
        ).lower()
        self.move = player_move


class Computer(Player):
    OPPONENT_DICT = {"1": "Default", "2": "Hal", "3": "R2D2", "4": "Daneel"}
    VALID_SELECTION = OPPONENT_DICT.keys()
    NAMES = OPPONENT_DICT.values()

    def __init__(self):
        super().__init__()
        self._name = "Default"
        self._description = "Moves are chosen completely at random"

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def choose(self):
        self.move = random.choice(Player.MOVES)


class Hal(Computer):
    SCISSORS_AFFINITY = 3

    def __init__(self):
        super().__init__()
        self._name = "Hal"
        self._description = "Has a strange affinity for Scissors"
        self._moves = Player.MOVES + tuple(
            [Scissors() for _ in range(self.__class__.SCISSORS_AFFINITY)]
        )

    def choose(self):
        self.move = random.choice(self._moves)


class R2D2(Computer):
    def __init__(self):
        super().__init__()
        self._name = "R2D2"
        self._description = "Only chooses Rock for its moves"

    def choose(self):
        self.move = Rock()


class Daneel(Computer):
    def __init__(self, history):
        super().__init__()
        self._name = "Daneel"
        self._description = (
            "Copies the Player's move in the previous round"
            " or randomly if first round"
        )
        self._history = history

    def choose(self):
        if len(self._history.player_moves):
            self.move = self._history.player_moves[-1]
        else:
            self.move = random.choice(Player.MOVES)


class MatchHistory:
    def __init__(self):
        self._player_moves = []
        self._computer_moves = []

    @property
    def player_moves(self):
        return self._player_moves

    def update(self, player_move, computer_move):
        self._player_moves.append(player_move)
        self._computer_moves.append(computer_move)

    def __str__(self):
        return "".join(
            [
                f"Match {i + 1}: Player chose {self._player_moves[i].name},"
                f" Computer chose {self._computer_moves[i].name}\n"
                for i in range(len(self._player_moves))
            ]
        )


class Opponents:
    def __init__(self, history):
        self.types = (Computer(), Hal(), R2D2(), Daneel(history))


class RPSGame:
    WINNING_SCORE = 5

    def __init__(self):
        self._human = Human()
        self._computer = None
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
            f"Welcome to Rock Paper Scissors Lizard Spock!"
            f" The first to {self.__class__.WINNING_SCORE} points wins!"
        )
        self._press_to_continue()

    def _display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors Lizard Spock. Goodbye!")

    def _clear_screen(self):
        os.system("clear")

    def _clear_screen_with_display(self):
        os.system("clear")
        self._display_score()

    def _display_chosen_opponent(self):
        print()
        print(f"You chose {self._computer.name}!")
        self._press_to_continue()

    def _display_score(self):
        print(f"Player: {self._score["player"]}   |")
        print(f"Computer: {self._score["computer"]} |")
        print("-------------")

    def _display_match_winner(self):
        if self._human_wins():
            print("You win! You are the ultimate victor!")
        else:
            print("Computer wins! Better luck next time!")

    def _display_round_winner(self):
        if self._human_wins():
            print("You win!")
        elif self._computer_wins():
            print("Computer wins!")
        else:
            print("It's a tie!")

    def _display_winner(self):
        self._clear_screen_with_display()
        print(f"You chose: {self._human.move.name}")
        print(f"The computer chose: {self._computer.move.name}")
        print()

        if self._game_over():
            self._display_match_winner()
        else:
            self._display_round_winner()

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

        self._history.update(self._human.move, self._computer.move)

    def _reset_score(self):
        for player in self._score:
            self._score[player] = 0

    def _request_opponent(self):
        self._clear_screen()
        print("List of your opponents:")
        print()
        for num, opponent in Computer.OPPONENT_DICT.items():
            print(
                f"{num}. {opponent} - "
                f"{self._convert_opponent_to_obj(opponent).description}"
            )
            print()

        return input("Choose an opponent (1-4): ")

    def _validate_opponent(self, opponent):
        while opponent not in Computer.VALID_SELECTION:
            opponent = input("Invalid opponent. Choose an opponent (1-4): ")

        return self._convert_opponent_to_obj(Computer.OPPONENT_DICT[opponent])

    def _convert_opponent_to_obj(self, name):
        for opponent in Opponents(self._history).types:
            if name == opponent.name:
                return opponent
        return None

    def _convert_move_to_obj(self, move):
        for player_move in Player.MOVES:
            if move == player_move.name:
                return player_move
        return None

    def _validate_move(self, move):
        while move not in Move.VALID_MOVES:
            move = input(
                "Invalid move. Choose a move - "
                f"{self._human.display_moves(Player.MOVE_NAMES)}: "
            ).lower()

        move = Move.MOVE_DICT[move] if move in Move.MOVE_DICT else move
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
            self._computer = self._validate_opponent(self._request_opponent())
            self._display_chosen_opponent()

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
