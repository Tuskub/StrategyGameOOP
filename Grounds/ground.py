from dataclasses import dataclass
from MainModels.coordinates import Coordinates


@dataclass
class Ground(Coordinates):
    _img_path: str
    _is_playble_field = None

    @classmethod
    def get_is_playble_field(cls):
        return cls._is_playble_field
