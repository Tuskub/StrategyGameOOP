from dataclasses import dataclass
from Units.unit import Unit


@dataclass
class Range(Unit):
    damage = 0
    close_damage = 0
    atack_range = 0
