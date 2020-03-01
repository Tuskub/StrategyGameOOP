from dataclasses import dataclass
from Units.melee_unit import Melee


@dataclass
class Hourseman(Melee):
    _hp: int = 200
    move_range: int = 10
    damage = 75
    img_path = 'path/to/image'
