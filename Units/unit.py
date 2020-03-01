from dataclasses import dataclass
from MainModels.coordinates import Coordinates


@dataclass
class Unit(Coordinates):
    player_id: int
    hp: int
    move_range: int
    attack_range: int
