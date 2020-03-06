from dataclasses import dataclass
from units.melee_unit import Melee
from constants.hoursemanconst import HP, MOVE_RANGE, DAMAGE


@dataclass
class Hourseman(Melee):
    _hp: int = HP
    move_range: int = MOVE_RANGE
    _damage: int = DAMAGE
    img_path = 'path/to/image'
