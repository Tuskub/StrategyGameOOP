from model.map import Map
from grounds.playable.grass import Grass
from grounds.unplayable.water import Water
from units.melee.horseman import Hourseman
from units.melee.swordsman import Swordsman
from units.range.archer import Archer
from units.range.catapult import Catapult
from control.game_control import GameControl


grass_list = [Grass(0, 0, 't'), Grass(0, 1, 'r'), Grass(0, 2, 'r'),
              Grass(1, 0, 't'), Grass(1, 1, 't'), Grass(1, 2, 't'),
              Water(2, 0, 't'), Grass(2, 1, 't'), Grass(2, 2, 't'),
              Water(3, 0, 't'), Water(3, 1, 't'), Water(3, 2, 't')]
swordsman = Swordsman(0, 2, 2)
print(swordsman)
archer = Archer(0, 0, 1)
print(archer)

catapult = Catapult(1, 1, 2)
print(catapult)
hourseman = Hourseman(2, 2, 1)
print(hourseman)
unit_list = [swordsman, archer, catapult, hourseman]
map = Map(grass_list, unit_list)
gc = GameControl(map)
