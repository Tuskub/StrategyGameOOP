from math import fabs
from dataclasses import dataclass
from mainclass.map import Map


@dataclass
class GameControl:
    map: Map

    def _can_unit_move(self, unit, x, y):
        out_of_range = unit.is_out_of_move_range(x, y)
        if out_of_range:
            return False
        playable_field = self.map.is_playable_field(x, y)
        if not playable_field:
            return False
        for u in self.map.units:
            if u.x == x and u.y == y:
                return False
        return True

    def _can_unit_attack(self, selected, target):
        if selected.player_id == target.player_id:
            return False
        if target.is_dead:
            return False
        dx = fabs(selected.x - target.x)
        dy = fabs(selected.y - target.y)
        return dx <= selected.attack_range and dy <= selected.attack_range

    def move_unit(self, unit, x, y):
        if not self._can_unit_move(unit, x, y):
            return
        unit.move(x, y)
        return

    def attack_unit(self, selected, target):
        if not self._can_unit_attack(selected, target):
            return
        selected.hit_enemy(target)
        if target._hp == 0:
            target.death()
        return
