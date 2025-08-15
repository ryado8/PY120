import random
import math


class GuessingGame:

    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.reset()

    def validate_answer(self):
        guess = input(f"Enter a number between {self.low} and {self.high}: ").strip()
        if guess.isdigit():
            while int(guess) not in range(self.low, self.high + 1):
                print(
                    f"Invalid guess. Enter a number between {self.low} and {self.high}: "
                )
                guess = int(input().strip())

        return guess

    def reset(self):
        self.answer = random.randint(self.low, self.high)
        self.number_of_guesses = int(math.log2(self.high - self.low + 1)) + 1

    def play(self):
        self.reset()
        while self.number_of_guesses > 0:
            print(f"You have {self.number_of_guesses} guesses remaining.")
            guess = self.validate_answer()

            if guess == self.answer:
                print("That's the number!")
                break

            if guess > self.answer:
                print("Your guess is too high.")
            elif guess < self.answer:
                print("Your guess is too low.")
            self.number_of_guesses -= 1

        if self.number_of_guesses > 0:
            print("You won!")
        else:
            print("You have no more guesses. You lost!")


game = GuessingGame(501, 1500)
game.play()

# You have 10 guesses remaining.
# Enter a number between 501 and 1500: 104
# Invalid guess. Enter a number between 501 and 1500: 1000
# Your guess is too low.

# You have 9 guesses remaining.
# Enter a number between 501 and 1500: 1250
# Your guess is too low.

# You have 8 guesses remaining.
# Enter a number between 501 and 1500: 1375
# Your guess is too high.

# You have 7 guesses remaining.
# Enter a number between 501 and 1500: 80
# Invalid guess. Enter a number between 501 and 1500: 1312
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 501 and 1500: 1343
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 501 and 1500: 1359
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 501 and 1500: 1351
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 501 and 1500: 1355
# That's the number!

# You won!

# game.play
# You have 10 guesses remaining.
# Enter a number between 501 and 1500: 1000
# Your guess is too high.

# You have 9 guesses remaining.
# Enter a number between 501 and 1500: 750
# Your guess is too low.

# You have 8 guesses remaining.
# Enter a number between 501 and 1500: 875
# Your guess is too high.

# You have 7 guesses remaining.
# Enter a number between 501 and 1500: 812
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 501 and 1500: 843
# Your guess is too high.

# You have 5 guesses remaining.
# Enter a number between 501 and 1500: 820
# Your guess is too low.

# You have 4 guesses remaining.
# Enter a number between 501 and 1500: 830
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 501 and 1500: 835
# Your guess is too low.

# You have 2 guesses remaining.
# Enter a number between 501 and 1500: 836
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 501 and 1500: 837
# Your guess is too low.

# You have no more guesses. You lost!
