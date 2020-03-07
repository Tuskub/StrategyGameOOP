from dataclasses import dataclass
from grounds.ground import Ground
from constants.waterconst import PLAYABLE_FIELD


@dataclass
class Water(Ground):
    _playable_field: bool = PLAYABLE_FIELD
    _img_path: str = 'path/to/img'
