from Grounds.playable.grass import Grass
from Grounds.not_playable.water import Water
from Grounds.not_playable.grave import Grave


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
