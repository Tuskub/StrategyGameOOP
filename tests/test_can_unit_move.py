import pytest
from mainclass.map import Map
from control.game_control import GameControl
from units.range.archer import Archer
from units.range.catapult import Catapult
from units.melee.horseman import Horseman
from units.melee.swordsman import Swordsman
from grounds.playable.grass import Grass
from grounds.unplayable.water import Water


class TestMoveOnEmpty():

    START_POSITION_X = 10
    START_POSITION_Y = 10

    START_POSITION_X_HOURSE = 20
    START_POSITION_Y_HOURSE = 20

    archer = Archer(START_POSITION_X, START_POSITION_Y, 1)
    catapult = Catapult(START_POSITION_X, START_POSITION_Y, 1)
    horseman = Horseman(START_POSITION_X_HOURSE, START_POSITION_Y_HOURSE, 1)
    swordsman = Swordsman(START_POSITION_X, START_POSITION_Y, 1)

    archer_test_cases = (
        (6, 7, False),
        (7, 6, False),
        (14, 13, False),
        (13, 14, False),
        (10, 10, False),
        (9, 10, True),
        (11, 10, True),
        (7, 7, True),
        (13, 13, True)
    )

    catapult_test_cases = (
        (8, 9, False),
        (9, 8, False),
        (10, 10, False),
        (11, 12, False),
        (12, 11, False),
        (9, 10, True),
        (11, 10, True),
        (9, 9, True),
        (11, 11, True)
    )

    horseman_test_cases = (
        (10, 9, False),
        (9, 10, False),
        (30, 31, False),
        (31, 30, False),
        (20, 20, False),
        (10, 10, True),
        (30, 30, True),
        (11, 15, True),
        (25, 12, True)
    )

    swordsman_test_cases = (
        (4, 5, False),
        (5, 4, False),
        (15, 16, False),
        (16, 15, False),
        (10, 10, False),
        (5, 5, True),
        (15, 15, True),
        (9, 10, True),
        (12, 7, True)
    )

    def make_ids(some_tests):
        ids = ['Coordinates({}, {}), answer = {}'.format(
               t[0], t[1], t[2]) for t in some_tests]
        return ids

    @pytest.mark.parametrize('test_x, test_y, answer',
                             archer_test_cases,
                             ids=make_ids(archer_test_cases))
    def test_archer(self, test_x, test_y, answer):
        map = Map(list(), [self.archer])
        gc = GameControl(map)
        can_move = gc._can_unit_move(self.archer, test_x, test_y)
        assert answer == can_move

    @pytest.mark.parametrize('test_x, test_y, answer',
                             catapult_test_cases,
                             ids=make_ids(catapult_test_cases))
    def test_catapult(self, test_x, test_y, answer):
        map = Map(list(), [self.catapult])
        gc = GameControl(map)
        can_move = gc._can_unit_move(self.catapult, test_x, test_y)
        assert answer == can_move

    @pytest.mark.parametrize('test_x, test_y, answer',
                             horseman_test_cases,
                             ids=make_ids(horseman_test_cases))
    def test_horseman(self, test_x, test_y, answer):
        map = Map(list(), [self.horseman])
        gc = GameControl(map)
        can_move = gc._can_unit_move(self.horseman, test_x, test_y)
        assert answer == can_move

    @pytest.mark.parametrize('test_x, test_y, answer',
                             swordsman_test_cases,
                             ids=make_ids(swordsman_test_cases))
    def test_swordsman(self, test_x, test_y, answer):
        map = Map(list(), [self.swordsman])
        gc = GameControl(map)
        can_move = gc._can_unit_move(self.swordsman, test_x, test_y)
        assert answer == can_move


class TestOnGrassOrWater():
    START_POSITION_X = 14
    START_POSITION_Y = 14

    GRASS_POSITION_X = 15
    GRASS_POSITION_Y = 15
    WATER_POSITION_X = 13
    WATER_POSITION_Y = 13

    archer = Archer(START_POSITION_X, START_POSITION_Y, 1)
    catapult = Catapult(START_POSITION_X, START_POSITION_Y, 1)
    horseman = Horseman(START_POSITION_X, START_POSITION_Y, 1)
    swordsman = Swordsman(START_POSITION_X, START_POSITION_Y, 1)
    grass = Grass(GRASS_POSITION_X, GRASS_POSITION_Y)
    water = Water(WATER_POSITION_X, WATER_POSITION_Y)

    units = (
        archer,
        catapult,
        horseman,
        swordsman
    )

    tests_ids = ['{}'.format(u.__class__.__name__) for u in units]

    @pytest.mark.parametrize('unit', units, ids=tests_ids)
    def test_move(self, unit):
        map = Map([self.grass, self.water], [unit])
        gc = GameControl(map)
        grass_x, grass_y = self.grass.get_coordinates()
        assert gc._can_unit_move(unit, grass_x, grass_y)
        water_x, water_y = self.water.get_coordinates()
        assert not gc._can_unit_move(unit, water_x, water_y)


class TestToUnit():
    START_POSITION_X = 14
    START_POSITION_Y = 14

    archer = Archer(START_POSITION_X - 1, START_POSITION_Y - 1, 2)

    units = (
        Archer(START_POSITION_X, START_POSITION_Y, 1),
        Catapult(START_POSITION_X, START_POSITION_Y, 1),
        Horseman(START_POSITION_X, START_POSITION_Y, 1),
        Swordsman(START_POSITION_X, START_POSITION_Y, 1)
    )

    test_ids = ['{} move to Archer'.format(u.__class__.__name__)
                for u in units]

    @pytest.mark.parametrize('unit', units, ids=test_ids)
    def test_to_unit(self, unit):
        map = Map(list(), [self.archer, unit])
        gc = GameControl(map)
        target_x, target_y = self.archer.get_coordinates()
        assert not gc._can_unit_move(unit, target_x, target_y)
