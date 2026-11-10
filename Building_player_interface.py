import random
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)
        self.position = (
            self.position[0] + move[0],
            self.position[1] + move[1]
        )
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [
            (0, 1),   # Up
            (0, -1),  # Down
            (-1, 0),  # Left
            (1, 0)    # Right
        ]

    def level_up(self):
        self.moves.extend([
            (-1, 1),   # Up-left
            (1, 1),    # Up-right
            (-1, -1),  # Down-left
            (1, -1)    # Down-right
        ])