from dataclasses import dataclass
from grounds.ground import Ground


@dataclass
class Grass(Ground):
    _playble_field = True
    _img_path: str = 'path/to/img'
