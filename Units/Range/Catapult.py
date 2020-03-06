from dataclasses import dataclass
from units.range_unit import Range
from constants.catapultconst import HP, MOVE_RANGE, CLOSE_DAMAGE, DAMAGE, ATTACK_RANGE # noqa


@dataclass
class Catapult(Range):
    _hp: int = 75
    move_range: int = 1
    _damage: int = 100
    _close_damage: int = 50
    attack_range: int = 10
    _img_path = 'path/to/image'
