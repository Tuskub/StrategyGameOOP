from dataclasses import dataclass


@dataclass
class Coordinates:
    X: int
    Y: int

    def get_hash_code(self):
        return (self.X * 397) ** self.Y
