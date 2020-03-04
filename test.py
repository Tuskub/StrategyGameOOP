from MainModels.coordinates import Coordinates
from MainModels.player import Player
from MainModels.map import Map
from grounds.playable.grass import Grass
from grounds.unplayable.water import Water
from grounds.unplayable.grave import Grave
from units.melee.horseman import Hourseman
from units.melee.swordsman import Swordsman
from units.range.archer import Archer
from units.range.catapult import Catapult
from control.game_control import GameControl


# ------ Grounds Test -------
grass = Grass(1, 0, 'tete')
print(grass)
water = Water(0, 1, 'test')
print(water)
grave = Grave(2, 1, 'toto')
print("Grass is playable? %s" % Grass.get_is_playble_field())
print("Water is playable? %s" % Water.get_is_playble_field())
print("Grave is playable? %s" % Grave.get_is_playble_field())
grass_x, grass_y = grass.get_coordinates()
water_x, water_y = water.get_coordinates()
grave_x, grave_y = grave.get_coordinates()
print([grass_x, grass_y])
print([water_x, water_y])
print([grave_x, grave_y])

print('--------HORSEMAN-----------')
hourseman = Hourseman(2, 2, 5)
print(hourseman)
print("Hourseman damage = %s" % hourseman._damage)
print('--------SWORDMAN-----------')
swordsman = Swordsman(1, 1, 10)
print(swordsman)
print("Swordsman damage = %s" % swordsman._damage)
print('--------ARCHER-----------')
archer = Archer(2, 0, 2)
print(archer)
print("Archer damage = %s" % archer._damage)
print("Archer close damage = %s" % archer._close_damage)
print('--------CATAPULT-----------')
catapult = Catapult(1, 1, 2)
print(catapult)
print("Catapult damage = %s" % catapult._damage)
print("Cataplt close damage = %s" % catapult._close_damage)
print('-------------Test Damage----------------')
print('hourseman attack swordsman')
hourseman.give_damage(swordsman)
print(swordsman)
print('catapult attack hourseman')
catapult.give_damage(hourseman)
print(hourseman)
print('-------------Test Move----------------')
print(hourseman)
hourseman.move(Coordinates(1, 3))
print(hourseman)
print('catapult attack hourseman')
catapult.give_damage(hourseman)
print(hourseman)
print('-------------Map and Player----------------')
map = Map([water, grass, grave], [hourseman, swordsman, archer, catapult])
# print(map.grounds.get_is_playble_field())
gc = GameControl(map)
print(gc.can_unit_move(catapult, 100, 3))
print(map.grounds)
print(gc.map.grounds)
water.get_is_playble_field()
print("Water %s" % gc.can_unit_move(catapult, water.x, water.y))
print("Grass %s" % gc.can_unit_move(catapult, grass.x, grass.y))
print("Grave %s" % gc.can_unit_move(catapult, grave.x, grave.y))
grass_list = [Grass(0, 0, 't'), Grass(0, 1, 'r'), Grass(0, 2, 'r'),
              Grass(1, 0, 't'), Grass(1, 1, 't'), Grass(1, 2, 't'),
              Water(2, 0, 't'), Grass(2, 1, 't'), Grass(2, 2, 't'),
              Water(3, 0, 't'), Water(3, 1, 't'), Water(3, 2, 't')]
unit_list = [Swordsman(0, 2, 2), Archer(0, 0, 2),
             Catapult(1, 0, 2), Hourseman(2, 2, 2)]
new_map = Map(grass_list, unit_list)
new_gc = GameControl(new_map)
print('Test units move')
catapult.move(Coordinates(1, 1))
print('Try move on Archer %s' % new_gc.can_unit_move(catapult, 0, 0))
print('Try move on Swordsman %s' % new_gc.can_unit_move(catapult, 0, 2))
print('Try move on Catapult %s' % new_gc.can_unit_move(catapult, 1, 0))
print('Try move on Hourseman %s' % new_gc.can_unit_move(catapult, 2, 2))
print('Try out of range move 1000 1000 %s' % new_gc.can_unit_move(catapult, 1000, 1000))
print('Try out of range move 1, 3 %s' % new_gc.can_unit_move(catapult, 1, 4))
print('Try move on water 2 0 %s' % new_gc.can_unit_move(catapult, 2, 0))
print('Try move on Grass 0 1 %s' % new_gc.can_unit_move(catapult, 0, 1))
