from dataclasses import dataclass
from Grounds.ground import Ground


@dataclass
class Water(Ground):
    _is_playble_field = False
    pass
