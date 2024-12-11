import math
from collections import defaultdict
from functools import reduce

DISTANCES = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]

def generate_substrings(input_line, length):
    substings = list()
    current_string = " " * length
    for i in input_line:
        current_string = current_string[1:] + i
        substings.append(current_string)
    return substings

def rotate_matrix_90_degree(matrix, pos):
    return list(zip(*(matrix[::-1]))), (pos[1], len(matrix) - pos[0] - 1)

def out_of_bounce(matrix, position):
    x = len(matrix[0])
    y = len(matrix)
    if position[1] >= x:
        return True
    if position[1] < 0:
        return True
    if position[0] >= y:
        return True
    if position[0] < 0:
        return True
    return False

def get_elments_directions(reach, matrix, pos, dist=DISTANCES):
    result = list()
    for distances in dist:
        tmp = list()
        position = pos
        for i in range(reach):
            position = tuple(map(lambda m, j: m + j, position, distances))
            if out_of_bounce(matrix, position):
                continue
            tmp.append(matrix[position[0]][position[1]])
        result.append(tmp)
    return result

def get_diff_coord(pos_one, pos_two):
    return pos_one[0] - pos_two[0], pos_one[1]-pos_two[1]

def add_tuple(tuple_one,tuple_two, substract=False):
    if substract:
        return tuple_one[0] - tuple_two[0] ,tuple_one[1] - tuple_two[1]
    return tuple_one[0] + tuple_two[0], tuple_one[1] + tuple_two[1]

def list_of_intstr_to_int(input):
    return list(map(int, input))

#Loops break this needs visited matrix to stop that
def dfs(pos, edge_graph, nodes, seen):
    if nodes[pos[0]][pos[1]] == 9:
        seen[pos[0]][pos[1]] += 1
    if not edge_graph[(pos[0],pos[1])]:
        return
    for edge in edge_graph[(pos[0], pos[1])]:
        dfs(edge, edge_graph, nodes, seen)