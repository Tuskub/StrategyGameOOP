from dataclasses import dataclass
from grounds.ground import Ground


@dataclass
class Water(Ground):
    _playble_field = False
    pass
