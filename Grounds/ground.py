from dataclasses import dataclass
from model.coordinates import Coordinates


@dataclass
class Ground(Coordinates):

    @classmethod
    def get_is_playble_field(cls):
        return cls._playble_field
