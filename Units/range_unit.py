from dataclasses import dataclass
from Units.unit import Unit


@dataclass
class Range(Unit):
    damage: int
    close_damage: int
    atack_range: int
