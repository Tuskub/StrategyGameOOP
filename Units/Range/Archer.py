from dataclasses import dataclass
from units.range_unit import Range
from constants.archerconst import HP, MOVE_RANGE, CLOSE_DAMAGE, DAMAGE, ATTACK_RANGE # noqa


@dataclass
class Archer(Range):
    attack_range: int = ATTACK_RANGE
    _hp: int = HP
    move_range: int = MOVE_RANGE
    _damage: int = DAMAGE
    _close_damage: int = CLOSE_DAMAGE
    _img_path = 'path/to/image'
