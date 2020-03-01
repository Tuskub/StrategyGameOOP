from dataclasses import dataclass
from Units.range_unit import Range


@dataclass
class Catapult(Range):
    _hp: int = 75
    move_range: int = 1
    damage = 100
    close_damage = 50
    atack_range = 10
    img_path = 'path/to/image'
