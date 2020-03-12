from dataclasses import dataclass
from grounds.ground import Ground
from constants.grassconts import PLAYABLE_FIELD


@dataclass
class Grass(Ground):
    _playable_field: bool = PLAYABLE_FIELD
    img_path: str = 'static/img/GrassA.png'
