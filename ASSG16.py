"""16. Imagine you are creating a Super Mario game. You need to define
a class to represent Mario. What would it look like? If you aren't
familiar with SuperMario, use your own favorite video or board game
to model a player."""

class SuperMario():
    def __init__(self, name, score, coins, world, time, lives):
        self.name = name
        self.score = score
        self.coins = coins
        self.world = world
        self.time = time
        self.lives = lives

