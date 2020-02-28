from dataclasses import dataclass
from ..MainModels.coordinates import Coordinates


@dataclass
class Ground(Coordinates):
    can_movie: bool
