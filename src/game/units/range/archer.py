from dataclasses import dataclass
from src.game.units.range_unit import Range
from src.game.constants.archerconst import HP, MOVE_RANGE, CLOSE_DAMAGE, DAMAGE, ATTACK_RANGE, IMG_PLAYER_1_PATH, IMG_PLAYER_2_PATH # noqa


@dataclass
class Archer(Range):
    attack_range: int = ATTACK_RANGE
    _hp: int = HP
    move_range: int = MOVE_RANGE
    _damage: int = DAMAGE
    _close_damage: int = CLOSE_DAMAGE

    def get_img_path(self):
        if self._hp == 0:
            return 'static/img/textures/Grave.png'
        if self.player_id % 2 == 1:
            return IMG_PLAYER_1_PATH
        else:
            return IMG_PLAYER_2_PATH
