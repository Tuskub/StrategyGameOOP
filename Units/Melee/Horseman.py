from dataclasses import dataclass
from units.melee_unit import Melee


@dataclass
class Hourseman(Melee):
    _hp: int = 200
    move_range: int = 10
    _damage: int = 75
    img_path = 'path/to/image'
