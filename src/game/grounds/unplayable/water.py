from dataclasses import dataclass
from src.game.grounds.ground import Ground
from src.game.constants.waterconst import PLAYABLE_FIELD, IMG_PATH


@dataclass
class Water(Ground):
    _playable_field: bool = PLAYABLE_FIELD
    img_path = IMG_PATH
