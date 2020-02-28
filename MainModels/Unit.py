from dataclasses import dataclass
from Coordinates import Coordinates


@dataclass
class Unit(Coordinates):
    player_id: int
    hp: int
    move_range: int

    def atack(self, x, y):
        if self.X == x and self.Y == y:
            print('baam')
        else:
            print('not today')


test = Unit(1, 2, 3, 4, 5)
print(test)
