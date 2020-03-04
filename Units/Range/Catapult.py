from dataclasses import dataclass
from units.range_unit import Range


@dataclass
class Catapult(Range):
    _hp: int = 75
    move_range: int = 1
    _damage: int = 100
    _close_damage: int = 50
    atack_range = 10
    img_path = 'path/to/image'
