class Game:
    count = 0

    def __init__(self, game):
        self.name = game
        Game.count += 1

    def play(self):
        return f"Start the {self.name} game!"

class Bingo(Game):
    def __init__(self, game, name):
        super().__init__(game)
        self.player_name = name


class Scrabble(Game):
    def __init__(self, game, name1, name2):
        super().__init__(game)
        self.player_name1 = name1
        self.player_name2 = name2


bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
print(Game.count)                       # 2
print(scrabble.play())                  # Start the Scrabble game!
print(scrabble.player_name1)            # Jill
print(scrabble.player_name2)            # Sill
print(scrabble.player_name)
# AttributeError: 'Scrabble' object has no attribute 'player_name'