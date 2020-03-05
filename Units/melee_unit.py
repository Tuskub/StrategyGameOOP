from dataclasses import dataclass
from units.unit import Unit


@dataclass
class Melee(Unit):
    attack_range: int = 1

    def get_atack_range():
        return Melee.attack_range
