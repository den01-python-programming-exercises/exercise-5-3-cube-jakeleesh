class Cube:
    def __init__(self, edge_length):
        self.edge_length = edge_length

    def volume(self):
        return self.edge_length ** 3

    def __str__(self):
        return "The length of the edge is " + str(self.edge_length) + " and the volume " + str(self.volume())