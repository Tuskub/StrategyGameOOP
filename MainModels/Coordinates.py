class Coordinates:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def get_hash_code(self):
        return (self.X * 397) ** self.Y
