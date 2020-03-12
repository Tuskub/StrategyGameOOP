from dataclasses import dataclass
from units.melee_unit import Melee
from constants.horsemanconst import HP, MOVE_RANGE, DAMAGE


@dataclass
class Horseman(Melee):
    _hp: int = HP
    move_range: int = MOVE_RANGE
    _damage: int = DAMAGE

    def get_img_path(self):
        if self._hp == 0:
            return 'static/img/Grave.png'
        if self.player_id % 2 == 1:
            return 'static/img/HorsemanA.png'
        else:
            return 'static/img/HorsemanB.png'
