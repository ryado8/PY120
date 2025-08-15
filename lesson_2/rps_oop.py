import random
import os

class Player:
    CHOICES = ("rock", "paper", "scissors", "lizard", "spock")

    def __init__(self):
        self.move = None

class Human:
    CHOICE_DISPLAY = [f"({choice[:2]}){choice[2:]}" if choice == "spock" else f"({choice[0]}){choice[1:]}" for choice in Player.CHOICES]

    def __init__(self):
        super().__init__()

    def choose(self):
        player_move = input(f"Choose a move - {", ".join(self.CHOICE_DISPLAY)}: ").lower()
        self.move = player_move


class Computer:
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)


class RPSGame:
    WINNING_SCORE = 5
    CHOICE_DICT = {"r": "rock", "p": "paper", "s": "scissors", "l": "lizard", "sp": "spock"}
    VALID_CHOICES = tuple(CHOICE_DICT.keys()) + tuple(CHOICE_DICT.values())
    WINNING_MOVES = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "spock": ["rock", "scissors"],
        "lizard": ["spock", "paper"]
    }

    def __init__(self):
        self._human = Human()
        self._computer = Computer()
        self._score = {"player": 0, "computer": 0}

    def _press_to_continue(self):
        input("Press enter to continue:")

    def _display_welcome_message(self):
        self._clear_screen()
        print(f"Welcome to Rock Paper Scissors Lizard Spock! The first to {self.WINNING_SCORE} points wins!")
        self._press_to_continue()

    def _display_goodbye_message(self):
        print("Thanks for playing Rock Paper Scissors Lizard Spock. Goodbye!")

    def _human_wins(self):
        return self._computer.move in RPSGame.WINNING_MOVES[self._human.move]

    def _computer_wins(self):
        return self._human.move in RPSGame.WINNING_MOVES[self._computer.move]

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
            print('You win!')
        elif self._computer_wins():
            print('Computer wins!')
        else:
            print("It's a tie!")
        print()

        self._press_to_continue()

    def _game_over(self):
        return max(self._score.values()) == self.WINNING_SCORE

    def _update_score(self):
        if self._human_wins():
            self._score["player"] += 1
        elif self._computer_wins():
            self._score["computer"] += 1

    def _reset_score(self):
        for player in self._score:
            self._score[player] = 0

    def _validate_move(self, move):
        while move not in self.VALID_CHOICES:
            move = input(f"Invalid move. Choose a move - {", ".join(Human.CHOICE_DISPLAY)}: ").lower()

        return self.CHOICE_DICT[move] if move in self.CHOICE_DICT else move

    def _validate_answer(self, answer):
        while answer not in ('y', 'n', 'yes', 'no'):
            answer = input("Invalid answer. Would you like to play again? (y/n):").lower()

        return answer

    def _play_again(self):
        self._clear_screen()
        answer = self._validate_answer(input('Would you like to play again? (y/n): ').lower())
        return answer in ('y', 'yes')

    def play(self):
        self._display_welcome_message()

        while True:
            self._reset_score()

            while not self._game_over():
                self._clear_screen_with_display()
                self._human.choose()
                self._human.move = self._validate_move(self._human.move)
                self._computer.choose()
                self._update_score()
                self._display_winner()

            if not self._play_again():
                break

        self._display_goodbye_message()

game = RPSGame()
game.play()