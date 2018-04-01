class Node:
    pos = (0, 0)
    pheromone = 0

    def __init__(self, pos, pheromone):
        self.pos = pos
        self.pheromone = pheromone

    def __repr__(self):
        return "Pos=(%s), Pheromone=%s" % (self.pos, self.pheromone)

    def __str__(self):
        return "Pos=(%s), Pheromone=%s" % (self.pos, self.pheromone)
