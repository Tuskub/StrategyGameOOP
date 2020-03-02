from dataclasses import dataclass
from Units.melee_unit import Melee


@dataclass
class Swordsman(Melee):
    _hp: int = 100
    move_range: int = 5
    _damage: int = 50
    img_path = 'path/to/image'
