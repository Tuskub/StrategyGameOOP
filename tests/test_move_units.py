import pytest
from mainclass.map import Map
from control.game_control import GameControl
from units.range.archer import Archer
from units.range.catapult import Catapult
from units.melee.horseman import Horseman
from units.melee.swordsman import Swordsman
from grounds.playable.grass import Grass


MOVE_POSITION_X = 15
MOVE_POSITION_Y = 15


unit_to_try = ((Archer(14, 14, 1)),
               (Catapult(14, 14, 1)),
               (Horseman(14, 14, 1)),
               (Swordsman(14, 14, 1)))


@pytest.mark.parametrize('unit', unit_to_try)
def test_move_unit(unit):
    map = Map([Grass(14, 14), Grass(15, 15)], [unit])
    gc = GameControl(map)
    gc.move_unit(unit, MOVE_POSITION_X, MOVE_POSITION_Y)
    assert unit.x == MOVE_POSITION_X and unit.y == MOVE_POSITION_Y
