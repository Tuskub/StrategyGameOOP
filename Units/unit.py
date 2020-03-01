from dataclasses import dataclass
from MainModels.coordinates import Coordinates


@dataclass
class Unit(Coordinates):
    player_id: int
    _hp: int
    move_range: int

    def take_damage(self, damage: int):
        self._hp -= damage
        return
