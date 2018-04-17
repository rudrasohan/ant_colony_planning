from world import World
import random
from copy import deepcopy
from math import pow
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Hyperparameters')
parser.add_argument("alpha", type=float, help="Parameter Alpha")
parser.add_argument("beta", type=float, help="Parameter Beta")
parser.add_argument("Q", type=int, help="Parameter Q")
parser.add_argument("num_ants", type=int, help="Number of Ants")
parser.add_argument("num_gen", type=int, help="Number of Generations")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Display individual paths")
args = parser.parse_args()


a = World()
print(a)
length = a.size[0]*a.size[1]
Q = args.Q
alpha = args.alpha
beta = args.beta
num_ants = args.num_ants
gen = args.num_gen
goal = a.goal
start_node = a.start
epsilon = 0.0005


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
    #print(nodes)
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

def get_path(start, goal):
    node = goal
    path = []
    f = False
    a.visited[goal] = 1
    j = 0
    while(node != start and not f):
        nb = a.get_neigbour(node)
        print(nb)
        for i in nb:
            if(i.pos == start_node):
                path.append(deepcopy(i.pos))
                f = True
                j = j + 1
        if (not f):
            move = choose_max(nb)
            a.visited[move.pos] = 1
            node = move.pos
            path.append(deepcopy(node))
            j = j + 1
    return (path, j)


a.visualize_world()

for l in range(gen):
    j = 0
    llist = []
    avg_len_gen = 0
    for k in range(num_ants):
        i = 0
        node = start_node
        path = []
        a.visited.clear()
        a.visited[a.start] = 1
        # print(node)
        while(node != goal and i <= length):

            nb = a.get_neigbour(node)
            random.shuffle(nb)
            #print(not nb)
            if not nb:
                break
            if (i%4 != 0):
                move = choose_prob_max(nb)
            else:
                move = choose_max(nb)
                # print("MAX")
            #print(type(move.pos))
            a.visited[move.pos] = 1
            # print(move,i)
            node = move.pos
            path.append(deepcopy(node))
            i = i + 1
        if (node == goal):
            j = j + 1
            llist.append(deepcopy((path, i)))
            avg_len_gen = avg_len_gen + i
            # print("True", i, j)
        #print(a)
    a.evaporate_pheromone(0.6)

    for path in llist:
        plen = path[1]
        u_path = list(set(path[0]))
        for i in range(0, len(u_path)):
            a.update_pheromone(u_path[i], (Q * 0.01 / plen**2 * j))
        if args.verbose:
            a.visualize(start_node, goal, path)

    #a.visualize_world()
    print((avg_len_gen / (j + epsilon)))

a.visualize_world()
a.visited.clear()
pth = get_path(start_node, goal)
print(pth)
a.visualize(start_node, goal, pth)