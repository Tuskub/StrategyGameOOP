from dataclasses import dataclass
from Coordinates import Coordinates


@dataclass
class Unit(Coordinates):
    player_id: int
    hp: int
    move_range: int
    attack_range: int

    def death(self):
        print('I\'m dead !!!')
