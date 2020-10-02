from dataclasses import dataclass
from grounds.ground import Ground
from constants.waterconst import PLAYABLE_FIELD, IMG_PATH


@dataclass
class Water(Ground):
    _playable_field: bool = PLAYABLE_FIELD
    img_path = IMG_PATH
