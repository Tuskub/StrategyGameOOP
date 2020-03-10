import pytest
from units.range.archer import Archer
from units.range.catapult import Catapult
from units.melee.horseman import Horseman
from units.melee.swordsman import Swordsman


class TestCanUnitAttack():

    START_POSITION_X = 10
    START_POSITION_Y = 10

    START_POSITION_X_CATAPULT = 20
    START_POSITION_Y_CATAPULT = 20

    archer_test_case = (
        (4, 5, False),
        (5, 4, False),
        (15, 16, False),
        (16, 15, False),
        (5, 5, True),
        (15, 15, True),
        (9, 10, True),
        (12, 7, True)
    )

    catapult_test_case = (
        (10, 9, False),
        (9, 10, False),
        (30, 31, False),
        (31, 30, False),
        (10, 10, True),
        (30, 30, True),
        (11, 15, True),
        (25, 12, True)
    )

    horseman_test_case = (
        (8, 9, False),
        (9, 8, False),
        (11, 12, False),
        (12, 11, False),
        (11, 11, True),
        (10, 11, True),
        (9, 9, True),
        (9, 10, True)
    )

    swordsman_test_case = (
        (8, 9, False),
        (9, 8, False),
        (11, 12, False),
        (12, 11, False),
        (11, 11, True),
        (10, 11, True),
        (9, 9, True),
        (9, 10, True)
    )

    def make_ids(sometest):
        ids = ['Enemy({}, {}) answer = {}'.format(
               t[0], t[1], t[2]) for t in sometest]
        return ids

    @pytest.mark.parametrize('enemy_x, enemy_y, answer',
                             archer_test_case,
                             ids=make_ids(archer_test_case))
    def test_archer(self, enemy_x, enemy_y, answer):
        archer = Archer(self.START_POSITION_X, self.START_POSITION_Y, 1)
        enemy = Archer(enemy_x, enemy_y, 2)
        assert archer.can_attack(enemy) == answer

    @pytest.mark.parametrize('enemy_x, enemy_y, answer',
                             catapult_test_case,
                             ids=make_ids(catapult_test_case))
    def test_catapult(self, enemy_x, enemy_y, answer):
        catapult = Catapult(self.START_POSITION_X_CATAPULT,
                            self.START_POSITION_Y_CATAPULT, 1)
        enemy = Catapult(enemy_x, enemy_y, 2)
        assert catapult.can_attack(enemy) == answer

    @pytest.mark.parametrize('enemy_x, enemy_y, answer',
                             horseman_test_case,
                             ids=make_ids(horseman_test_case))
    def test_horseman(self, enemy_x, enemy_y, answer):
        horseman = Horseman(self.START_POSITION_X, self.START_POSITION_X, 1)
        enemy = Horseman(enemy_x, enemy_y, 2)
        assert horseman.can_attack(enemy) == answer

    @pytest.mark.parametrize('enemy_x, enemy_y, answer',
                             swordsman_test_case,
                             ids=make_ids(swordsman_test_case))
    def test_swordsman(self, enemy_x, enemy_y, answer):
        swordsman = Swordsman(self.START_POSITION_X, self.START_POSITION_X, 1)
        enemy = Swordsman(enemy_x, enemy_y, 2)
        assert swordsman.can_attack(enemy) == answer


class TestCanAttackFriend():

    START_POSITION_X = 10
    START_POSITION_Y = 10
    PLAYER_ID = 1

    test_case = (
        (Archer(START_POSITION_X, START_POSITION_Y, PLAYER_ID),
         Horseman(START_POSITION_X + 1, START_POSITION_Y + 1, PLAYER_ID)),
        (Catapult(START_POSITION_X, START_POSITION_Y, PLAYER_ID),
         Horseman(START_POSITION_X + 1, START_POSITION_Y + 1, PLAYER_ID)),
        (Horseman(START_POSITION_X, START_POSITION_Y, PLAYER_ID),
         Horseman(START_POSITION_X + 1, START_POSITION_Y + 1, PLAYER_ID)),
        (Swordsman(START_POSITION_X, START_POSITION_Y, PLAYER_ID),
         Horseman(START_POSITION_X + 1, START_POSITION_Y + 1, PLAYER_ID))
    )

    test_friend_ids = ['{}_id({}). Friend {}_id({})'.format(
                       t[0].__class__.__name__, t[0].player_id,
                       t[1].__class__.__name__, t[1].player_id)
                       for t in test_case]

    @pytest.mark.parametrize('unit, friend', test_case, ids=test_friend_ids)
    def test_attack_friend(self, unit, friend):
        assert not unit.can_attack(friend)
