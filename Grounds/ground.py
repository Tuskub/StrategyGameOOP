from dataclasses import dataclass
from MainModels.coordinates import Coordinates


@dataclass
class Ground(Coordinates):
    _img_path: str

    @classmethod
    def get_is_playble_field(cls):
        return cls._playble_field
