from math import fabs
from dataclasses import dataclass
from MainModels.map import Map


@dataclass
class Game_control:
    map: Map

    def can_unit_move(self, unit, x, y):
        out_of_range = (fabs(unit.x - x) > unit.move_range or
                        fabs(unit.y - y) > unit.move_range)
        if(out_of_range):
            return False
        for g in self.map.grounds:
            not_playable_field = (not g.get_is_playble_field()) and g.x == x and g.y == y
            if not_playable_field:
                return False
        for u in self.map.units:
            if u.x == x and u.y == y:
                return False
        return True
