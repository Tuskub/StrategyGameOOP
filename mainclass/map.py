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

    def get_unit_by_point(self, x, y):
        coord = (x, y)
        for u in self.units:
            if u.get_coordinates() == coord:
                return u
        return None

    def end_game(self):
        fp_all_alive = True
        fp_all_dead = True
        sp_all_dead = True
        sp_all_alive = True

        for unit in self.units:
            if unit.player_id == 1:
                if unit.is_dead is True:
                    fp_all_alive = False
                else:
                    fp_all_dead = False
            if unit.player_id == 2:
                if unit.is_dead is True:
                    sp_all_alive = False
                else:
                    sp_all_dead = False
        return fp_all_alive, fp_all_dead, sp_all_alive, sp_all_dead
