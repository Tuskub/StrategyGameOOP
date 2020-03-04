from dataclasses import dataclass
from units.unit import Unit


@dataclass
class Melee(Unit):
    __atack_range = 1

    @staticmethod
    def get_atack_range():
        return Melee.__atack_range
