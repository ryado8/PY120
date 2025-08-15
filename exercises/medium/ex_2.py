import random


class GuessingGame:

    def __init__(self):
        self.reset()

    @staticmethod
    def validate_answer():
        guess = int(input("Enter a number between 1 and 100: ").strip())
        while guess not in range(1, 101):
            print("Invalid guess. Enter a number between 1 and 100: ")
            guess = int(input().strip())

        return guess

    def reset(self):
        self.counter = 7
        self.answer = random.randint(1, 100)

    def play(self):
        self.reset()
        while self.counter > 0:
            print(f"You have {self.counter} guesses remaining.")
            guess = GuessingGame.validate_answer()

            if guess == self.answer:
                print("That's the number!")
                break

            if guess > self.answer:
                print("Your guess is too high.")
            elif guess < self.answer:
                print("Your guess is too low.")
            self.counter -= 1

        if self.counter > 0:
            print("You won!")
        else:
            print("You have no more guesses. You lost!")


game = GuessingGame()
game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 104
# Invalid guess. Enter a number between 1 and 100: 50
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 75
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 85
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 0
# Invalid guess. Enter a number between 1 and 100: 80
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 81
# That's the number!

# You won!

game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 50
# Your guess is too high.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 25
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 37
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 31
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 34
# Your guess is too high.

# You have 2 guesses remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have no more guesses. You lost!
