from Grounds.playable.grass import Grass
from Grounds.not_playable.water import Water


grass = Grass(1, 2, 'tete')
print(grass)
water = Water(2, 1, 'test')
print(water)
print("Grass is playable? %s" % Grass.get_is_playble_field())
print("Water is playable? %s" % Water.get_is_playble_field())
