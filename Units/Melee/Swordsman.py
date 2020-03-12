from dataclasses import dataclass
from units.melee_unit import Melee
from constants.swordsmanconst import HP, MOVE_RANGE, DAMAGE # noqa


@dataclass
class Swordsman(Melee):
    _hp: int = HP
    move_range: int = MOVE_RANGE
    _damage: int = DAMAGE
    img_path = 'static/img/SwordsmanA.png'

    def get_img_path(self):
        if self._hp == 0:
            return 'static/img/Grave.png'
        if self.player_id % 2 == 1:
            return 'static/img/SwordsmanA.png'
        else:
            return 'static/img/SwordsmanB.png'
        
