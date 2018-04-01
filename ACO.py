from world import World
import random
from copy import deepcopy
from math import pow
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Hyperparameters')
parser.add_argument("length", type=int, help="Lenth of the Grid")
parser.add_argument("breadth", type=int, help="Breadth of the Grid")
parser.add_argument("goal_x", type=int, help="Goal Coordinate x")
parser.add_argument("goal_y", type=int, help="Goal Coordinate y")
parser.add_argument("num_ants", type=int, help="Number of Ants")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Display individual paths")
args = parser.parse_args()


a = World((args.breadth, args.length))
print(a)
length = args.length * args.breadth
Q = 1000.0
alpha = 5
beta = 2
num_ants = args.num_ants
goal = (args.goal_x, args.goal_y)
start_node = (0, 0)
epsilon = 0.0005
gen = 50


def euclidean(node):
    dist = ((node.pos[0] - goal[0])**2 + (node.pos[1] - goal[1])**2)**(0.5)
    return 1 / (dist + epsilon)


def choose_max(nodes):
    max_node = nodes[0]
    for node in nodes:
        if(node.pheromone >= max_node.pheromone):
            max_node = node
    return max_node


def choose_prob_max(nodes):
    llist = []
    num_list = list(range(len(nodes)))
    # print(num_list)
    summ = 0.0
    for node in nodes:
        summ = summ + pow(node.pheromone, alpha) * euclidean(node)**beta
    for node in nodes:
        llist.append(pow(node.pheromone, alpha) * euclidean(node)**beta / summ)
    prob_node = np.random.choice(num_list, 1, llist)
    # print(prob_node[0])
    return nodes[prob_node[0]]


for l in range(gen):
    j = 0
    llist = []
    avg_len_gen = 0
    for k in range(num_ants):
        i = 0
        node = start_node
        path = []
        # print(node)
        while(node != goal and i <= length):

            nb = a.get_neigbour(node)
            random.shuffle(nb)
            if (k % 4 != 0):
                move = choose_prob_max(nb)
                # print("PROB")
            else:
                move = choose_max(nb)
                # print("MAX")
            # print(move)
            # print(move,i)
            node = move.pos
            path.append(deepcopy(node))
            i = i + 1
        if (node == goal):
            j = j + 1
            llist.append(deepcopy((path, i)))
            avg_len_gen = avg_len_gen + i
            # print("True", i, j)
    a.evaporate_pheromone(0.6)

    for path in llist:
        plen = path[1]
        u_path = list(set(path[0]))
        for i in range(0, len(u_path)):
            a.update_pheromone(u_path[i], (Q * 0.01 / plen**2 * j))
        if args.verbose:
            a.visualize(start_node, goal, path)

    a.visualize_world()
    print((avg_len_gen / (j + epsilon)))
