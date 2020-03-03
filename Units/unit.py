from dataclasses import dataclass
from MainModels.coordinates import Coordinates


@dataclass
class Unit(Coordinates):
    player_id: int

    def take_damage(self, damage: int):
        self._hp -= damage
        return

    def give_damage(self, other):
        other.take_damage(self._get_damage(other))
        return

    def _get_damage(self, other=None):
        return self._damage

    def move(self, coordinates):
        self.x = coordinates.x
        self.y = coordinates.y
        return
