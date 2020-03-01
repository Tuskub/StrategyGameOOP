from Grounds.playable.grass import Grass
from Grounds.not_playable.water import Water
from Grounds.not_playable.grave import Grave
from Units.melee_unit import Melee
from Units.Melee.horseman import Hourseman
from Units.Melee.swordsman import Swordsman
from Units.Range.archer import Archer
from Units.Range.catapult import Catapult


# ------ Grounds Test -------
grass = Grass(1, 2, 'tete')
print(grass)
water = Water(2, 1, 'test')
print(water)
grave = Grave(4, 5, 'toto')
print("Grass is playable? %s" % Grass.get_is_playble_field())
print("Water is playable? %s" % Water.get_is_playble_field())
print("Grave is playable? %s" % Grave.get_is_playble_field())
grass_x, grass_y = grass.get_coordinates()
water_x, water_y = water.get_coordinates()
grave_x, grave_y = grave.get_coordinates()
print([grass_x, grass_y])
print([water_x, water_y])
print([grave_x, grave_y])


# ------ Units Test -------
melee = Melee(1, 2, 100, 2, 100)
print(melee)
print(Melee.get_atack_range())
melee.take_damage(30)
print(melee)
# --------HORSEMAN-----------
hourseman = Hourseman(1, 2, 5)
print(hourseman)
hourseman.take_damage(100)
print(hourseman)
print("Horsman damage = %s" % Hourseman.damage)
# --------SWORDMAN-----------
swordsman = Swordsman(1, 1, 10)
print(swordsman)
swordsman.take_damage(100)
print(swordsman)
print("Swordsman damage = %s" % Swordsman.damage)
# --------ARCHER-----------
archer = Archer(1, 2, 2)
print(archer)
archer.take_damage(100)
print(archer)
print("Archer damage = %s" % Archer.damage)
print("Archer close damage = %s" % Archer.close_damage)
# --------CATAPULT-----------
catapult = Catapult(1, 2, 2)
print(catapult)
catapult.take_damage(100)
print(catapult)
print("Catapult damage = %s" % Catapult.damage)
print("Cataplt close damage = %s" % Catapult.close_damage)
