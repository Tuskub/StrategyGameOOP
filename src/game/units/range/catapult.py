from dataclasses import dataclass
from src.game.units.range_unit import Range
from src.game.constants.catapultconst import HP, MOVE_RANGE, CLOSE_DAMAGE, DAMAGE, ATTACK_RANGE, IMG_PLAYER_1_PATH, IMG_PLAYER_2_PATH # noqa


@dataclass
class Catapult(Range):
    player_id: int
    attack_range: int = 10
    _hp: int = 75
    move_range: int = 1
    _damage: int = 100
    _close_damage: int = 50

    def get_img_path(self):
        if self._hp == 0:
            return 'static/img/textures/Grave.png'
        if self.player_id % 2 == 1:
            return IMG_PLAYER_1_PATH
        else:
            return IMG_PLAYER_2_PATH
