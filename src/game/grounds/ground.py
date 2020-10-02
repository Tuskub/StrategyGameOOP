from dataclasses import dataclass
from src.game.mainclass.coordinates import Coordinates


@dataclass
class Ground(Coordinates):

    def get_playable_field(self):
        return self._playable_field
