from dataclasses import dataclass
from units.range_unit import Range


@dataclass
class Archer(Range):
    _hp: int = 50
    move_range: int = 3
    _close_damage: int = 25
    _damage: int = 50
    atack_range = 5
    img_path = 'path/to/image'
