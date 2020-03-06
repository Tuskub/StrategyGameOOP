from dataclasses import dataclass
from units.unit import Unit
from constants.meleeconst import ATTACK_RANGE


@dataclass
class Melee(Unit):
    attack_range: int = ATTACK_RANGE

    def get_atack_range():
        return Melee.attack_range
