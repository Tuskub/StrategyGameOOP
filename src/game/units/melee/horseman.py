from dataclasses import dataclass
from src.game.units.melee_unit import Melee
from src.game.constants.horsemanconst import HP, MOVE_RANGE, DAMAGE, IMG_PLAYER_1_PATH, IMG_PLAYER_2_PATH # noqa


@dataclass
class Horseman(Melee):
    _hp: int = HP
    move_range: int = MOVE_RANGE
    _damage: int = DAMAGE

    def get_img_path(self):
        if self._hp == 0:
            return 'static/img/textures/Grave.png'
        if self.player_id % 2 == 1:
            return IMG_PLAYER_1_PATH
        else:
            return IMG_PLAYER_2_PATH
