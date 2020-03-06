from dataclasses import dataclass
from mainclass.coordinates import Coordinates
from constants.unitsconst import IS_DEAD


@dataclass
class Unit(Coordinates):
    player_id: int
    is_dead: bool = IS_DEAD

    def _take_damage(self, damage: int):
        self._hp = max(self._hp - damage, 0)

    def hit_enemy(self, other):
        other._take_damage(self._get_damage(other))

    def _get_damage(self, other=None):
        return self._damage

    def move(self, x, y):
        self.x = x
        self.y = y

    def death(self):
        self.is_dead = True
        self.attack_range = 0
        self.move_range = 0
        print('I\'m dead')
