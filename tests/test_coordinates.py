import pytest
from units.range.archer import Archer
from units.range.catapult import Catapult
from units.melee.horseman import Horseman
from units.melee.swordsman import Swordsman
from grounds.playable.grass import Grass
from grounds.unplayable.water import Water


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
