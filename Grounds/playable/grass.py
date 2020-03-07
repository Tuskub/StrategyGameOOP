from dataclasses import dataclass
from grounds.ground import Ground
from constants.grassconts import PLAYABLE_FIELD


@dataclass
class Grass(Ground):
    _playable_field: bool = PLAYABLE_FIELD
    _img_path: str = 'path/to/img'
