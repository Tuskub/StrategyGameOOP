import unittest
from mainclass.map import Map
from grounds.playable.grass import Grass
from grounds.unplayable.water import Water
from units.melee.horseman import Hourseman
from units.melee.swordsman import Swordsman
from units.range.archer import Archer
from units.range.catapult import Catapult
from control.game_control import GameControl


class TestGetCoordinates(unittest.TestCase):

    def setUp(self):
        self.archer = Archer(1, 2, 2)
        self.catapult = Catapult(3, 4, 2)
        self.hourseman = Hourseman(5, 6, 2)
        self.swordsman = Swordsman(7, 8, 2)
        self.grass = Grass(9, 10)
        self.water = Water(11, 12)

    def test_get_coordinatest(self):
        test_case_list = [
            [self.archer, (1, 2)],
            [self.catapult, (3, 4)],
            [self.hourseman, (5, 6)],
            [self.swordsman, (7, 8)],
            [self.grass, (9, 10)],
            [self.water, (11, 12)],
        ]
        for test in test_case_list:
            with self.subTest(test):
                self.assertEqual(test[0].get_coordinates(), test[1])


class TestMoveUnit(unittest.TestCase):
    MOVE_POSITION_X = 15
    MOVE_POSITION_Y = 15

    def setUp(self):
        self.archer = Archer(14, 14, 2)
        self.catapult = Catapult(14, 14, 2)
        self.hourseman = Hourseman(14, 14, 2)
        self.swordsman = Swordsman(14, 14, 2)
        self.unit_list = [
            self.archer,
            self.catapult,
            self.hourseman,
            self.swordsman
        ]
        self.grounds_list = [Grass(14, 14), Grass(15, 15)]

    def test_move_units(self):
        map = Map(self.grounds_list, self.unit_list)
        gc = GameControl(map)
        for u in self.unit_list:
            with self.subTest(u):
                gc.move_unit(u, self.MOVE_POSITION_X, self.MOVE_POSITION_Y)
                self.assertEqual(self.MOVE_POSITION_X, self.archer.x)
                self.assertEqual(self.MOVE_POSITION_Y, self.archer.y)
