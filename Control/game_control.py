from dataclasses import dataclass
from mainclass.map import Map


@dataclass
class GameControl:
    map: Map

    def _can_unit_move(self, unit, x, y):
        out_of_range = unit.is_out_of_move_range(x, y)
        if out_of_range:
            print('Out of move range!')
            return False
        playable_field = self.map.is_playable_field(x, y)
        if not playable_field:
            print('It\'s not playable field!')
            return False
        free_field = self.map.is_free_field(x, y)
        if not free_field:
            print('Some unit is here!')
            return False
        return True

    def move_unit(self, unit, x, y):
        if not self._can_unit_move(unit, x, y):
            return
        unit.move(x, y)
        return

    def attack_unit(self, selected, target):
        if not selected.can_attack(target):
            return
        selected.hit_enemy(target)
        if target._hp == 0:
            target.die()
        return
