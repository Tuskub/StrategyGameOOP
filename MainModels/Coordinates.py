from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: int

    def get_hash_code(self):
        return (self.x * 397) ** self.y

    def get_coordinates(self):
        return self.x, self.y
