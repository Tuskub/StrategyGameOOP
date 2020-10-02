from dataclasses import dataclass
from src.game.grounds.ground import Ground
from src.game.constants.grassconts import PLAYABLE_FIELD, IMP_PATH


@dataclass
class Grass(Ground):
    _playable_field: bool = PLAYABLE_FIELD
    img_path: str = IMP_PATH
