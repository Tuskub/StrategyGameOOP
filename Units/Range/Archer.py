from dataclasses import dataclass
from Units.range_unit import Range


@dataclass
class Archer(Range):
    _hp: int = 50
    move_range: int = 3
    damage = 50
    close_damage = 25
    atack_range = 5
    img_path = 'path/to/image'
