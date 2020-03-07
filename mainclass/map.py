from dataclasses import dataclass


@dataclass
class Map:
    grounds: list
    units: list

    def is_playable_field(self, x, y):
        for g in self.grounds:
            not_playable_field = ((not g.get_playable_field()) and
                                  g.x == x and g.y == y)
            if not_playable_field:
                return False
        return True

    def is_free_field(self, x, y):
        for u in self.units:
            if u.x == x and u.y == y:
                return False
        return True
