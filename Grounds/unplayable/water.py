from dataclasses import dataclass
from grounds.ground import Ground


@dataclass
class Water(Ground):
    _playble_field = False
    _img_path: str = 'path/to/img'
