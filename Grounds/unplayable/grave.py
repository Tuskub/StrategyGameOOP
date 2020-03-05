from dataclasses import dataclass
from grounds.ground import Ground


@dataclass
class Grave(Ground):
    _playble_field = False
    _img_path: str = 'path/to/img'
