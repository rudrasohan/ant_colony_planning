from node import Node
from copy import deepcopy
import json
import numpy as np


class World:
    size = (5, 5)
    grid = []
    obstacles = []

    def __init__(self, size):
        self.size = size
        grid = []
        obs = []
        for i in range(size[0]):
            llist = []
            for j in range(size[1]):
                llist.append(deepcopy(Node((i, j), 0.5)))
            grid.append(deepcopy(llist))
        data = json.load(open('obstacle.json'))
        pos = data["positions"]
        for i in range(data["num_obstacle"]):
            coor = pos[i]
            obs.append(deepcopy((coor[0], coor[1])))
            grid[coor[0]][coor[1]].pheromone = 0.0
        self.obstacles = obs
        self.grid = grid

    def __str__(self):
        return "Size=(%s)\nWorld:\n%s\nObstacles:%s" % (self.size, self.grid, self.obstacles)

    def get_neigbour(self, pos):
        nbh = []
        action_set = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for act in action_set:
            nb = (pos[0] + act[0], pos[1] + act[1])
            if (nb[0] < self.size[0] and nb[1] < self.size[1] and nb[0] >= 0 and nb[1] >= 0):
                nbh.append(deepcopy(Node(nb,self.grid[nb[0]][nb[1]].pheromone)))
        return nbh

    def evaporate_pheromone(self, roh):
        grid = []
        for i in range(self.size[0]):
            llist = []
            for j in range(self.size[1]):
                llist.append(deepcopy(Node((i, j), self.grid[i][j].pheromone * (1 - roh))))
            grid.append(deepcopy(llist))
        self.grid = grid

    def update_pheromone(self, pos, val):
        ph = self.grid[pos[0]][pos[1]].pheromone + val
        self.grid[pos[0]][pos[1]].pheromone = ph

    def visualize(self, start, goal, path):
        mat = np.zeros(self.size)
        mat[start[0]][start[1]] = 1
        mat[goal[0]][goal[1]] = 999
        for p in path[0]:
            mat[p[0]][p[1]] = 2
        print(mat)

    def visualize_world(self):
        mat = np.zeros(self.size)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                mat[i][j] = self.grid[i][j].pheromone
        print(mat)
