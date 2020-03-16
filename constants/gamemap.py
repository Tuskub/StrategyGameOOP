from units.range.archer import Archer
from units.range.catapult import Catapult
from units.melee.horseman import Horseman
from units.melee.swordsman import Swordsman
from grounds.playable.grass import Grass
from grounds.unplayable.water import Water


templates_map = [
    'ggggggggggggggggwg',
    'gggggggcggggggggww',
    'ggcggaghgggggggggg',
    'ggagggagsggggggggg',
    'ggggaggsgggggggggg',
    'wwwwwwwwgggggggggg',
    'gggggggggggggggggg',
    'gggggggggggggggggg',
    'wwwwwggwwwwggwwwww',
    'wwwwwggwwwwggwwwww',
    'gggggggggggggggggg',
    'gggggggggggggggggg',
    'ggggggggggwwwwwwww',
    'ggggggggggHgggHggg',
    'ggggggggggggSSSggg',
    'ggggggggggHgSgggAg',
    'wwggggggggggSggACg',
    'gwgggggggggggggggg'
]

new_map = [
    'ggggggggggggggggwggggggg',
    'gggggggcggggggggwwgggggg',
    'ggcggaHhgggggggggggggggg',
    'ggagggagsggggggggggggggg',
    'ggggaggsgggggggggggggggg',
    'wwwwwwwwgggggggggggggggg',
    'gggggggggggggggggggggggg',
    'gggggggggggggggggggggggg',
    'wwwwwggwwwwggwwwwwgggggg',
    'wwwwwggwwwwggwwwwgggHggw',
    'ggggggggggggggggAggCgSgg',
    'gggggggggggggggggggAgSgg',
    'ggggggggggwwwwwwwggggggw'
]

test_map = [
    'ggggggggggggggggwggggggg',
    'gggggggcggggggggwwgggggg',
    'ggcggaHhgggggggggggggggg',
    'ggagggagsggggggggggggggg',
    'ggggaggsgggggggggggggggg',
    'wwwwwwwwgggggggggggggggg',
    'gggggggggggggggggggggggg',
    'gggggggggggggggggggggggg',
    'wwwwwggwwwwggwwwwwgggggg',
    'wwwwwggwwwwggwwwwggggggw',
    'gggggggggggggggggggggggg',
    'gggggggggggggggggggggggg',
    'ggggggggggwwwwwwwggggggw'
]

ground_list = list()
unit_list = list()


def _create_ground(symbol, x, y):
    if symbol == 'w':
        return Water(x + 1, y + 1)
    else:
        return Grass(x + 1, y + 1)


def _create_unit(symbol, x, y):
    x += 1
    y += 1
    if symbol.lower() == 'a':
        return Archer(x, y, 1) if symbol.islower() else Archer(x, y, 2)
    if symbol.lower() == 'c':
        return Catapult(x, y, 1) if symbol.islower() else Catapult(x, y, 2)
    if symbol.lower() == 'h':
        return Horseman(x, y, 1) if symbol.islower() else Horseman(x, y, 2)
    if symbol.lower() == 's':
        return Swordsman(x, y, 1) if symbol.islower() else Swordsman(x, y, 2)
    return None


def generate_map():
    for i in range(13):
        for j in range(24):
            ground = _create_ground(test_map[i][j], i, j)
            ground_list.append(ground)
            unit = _create_unit(test_map[i][j], i, j)
            if unit is not None:
                unit_list.append(unit)
    return ground_list, unit_list
