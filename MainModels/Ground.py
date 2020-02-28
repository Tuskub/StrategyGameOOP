from dataclasses import dataclass
from Coordinates import Coordinates


@dataclass
class Ground(Coordinates):
    can_movie: bool
