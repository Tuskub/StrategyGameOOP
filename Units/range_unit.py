from dataclasses import dataclass
from units.unit import Unit
from math import fabs


@dataclass
class Range(Unit):

    def _get_damage(self, other):
        mod_dx = fabs(self.x - other.x)
        mod_dy = fabs(self.y - other.y)
        if (mod_dx == 1 or mod_dx == 0) and (mod_dy == 1 or mod_dy == 0):
            return self._close_damage
        return self._damage
