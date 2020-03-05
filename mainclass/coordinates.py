from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: int

    def get_coordinates(self):
        return self.x, self.y
