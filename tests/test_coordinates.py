import pytest
from src.game.units.range.archer import Archer
from src.game.units.range.catapult import Catapult
from src.game.units.melee.horseman import Horseman
from src.game.units.melee.swordsman import Swordsman
from src.game.grounds.playable.grass import Grass
from src.game.grounds.unplayable.water import Water


@pytest.mark.parametrize('unit, coordinate',
                         [
                             (Archer(1, 2, 1), (1, 2)),
                             (Catapult(3, 4, 1), (3, 4)),
                             (Horseman(5, 6, 1), (5, 6)),
                             (Swordsman(7, 8, 1), (7, 8)),
                             (Grass(9, 10), (9, 10)),
                             (Water(11, 12), (11, 12))
                         ])
def test_get_coordinates(unit, coordinate):
    unit_coord = unit.get_coordinates()
    assert unit_coord == coordinate
