from math import fabs
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

    def die(self):
        self.is_dead = True
        self.attack_range = 0
        self.move_range = 0
        self.img_path = 'static/img/Grave.png'

    def is_out_of_move_range(self, x, y):
        out_of_range = (fabs(self.x - x) > self.move_range or
                        fabs(self.y - y) > self.move_range)
        return out_of_range

    def can_attack(self, other):
        if self.player_id == other.player_id:
            return False
        if other.is_dead:
            return False
        dx = fabs(self.x - other.x)
        dy = fabs(self.y - other.y)
        return dx <= self.attack_range and dy <= self.attack_range
