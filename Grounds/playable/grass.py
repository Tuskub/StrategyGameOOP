from dataclasses import dataclass
from Grounds.ground import Ground


@dataclass
class Grass(Ground):
    _is_playble_field = True
    pass
