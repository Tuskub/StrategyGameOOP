from dataclasses import dataclass
from units.melee_unit import Melee
from constants.horsemanconst import HP, MOVE_RANGE, DAMAGE


@dataclass
class Horseman(Melee):
    _hp: int = HP
    move_range: int = MOVE_RANGE
    _damage: int = DAMAGE
    img_path = 'static/img/HorsemanA.png'
