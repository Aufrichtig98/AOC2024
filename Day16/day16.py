import aoc_helper
from collections import defaultdict
import sys
import random

import debug_helper


def part_one():
    def construct_graph(pos, map, graph, prev_dir, dist, prev):
        directions = aoc_helper.DIRECTION_WITHOUT_DIAG.copy()
        match prev_dir:
            case (1, 0):
                directions.remove((-1, 0))
            case (-1, 0):
                directions.remove((1, 0))
            case (0, 1):
                directions.remove((0, -1))
            case (0, -1):
                directions.remove((0, 1))

        for dir in directions:
            new_pos = aoc_helper.add_tuple(dir, pos)
            if map[new_pos[0]][new_pos[1]] == ".":
                weight = 1 if prev_dir == dir else 1001
                if dist[new_pos] > dist[pos] + weight:
                    prev[new_pos] = pos
                    dist[new_pos] = dist[pos] + weight
                    construct_graph(new_pos, map, graph, dir, dist, prev)
                else:
                    continue

    if __name__ == '__main__':
        sys.setrecursionlimit(100000)
        graph = defaultdict(list)
        requests = list()
        with open("input.txt", "rt") as myfile:
            for line in myfile:
                requests.append(list(line.strip("\n")))
        requests[len(requests) - 2][1] = "."
        requests[1][len(requests[0]) - 2] = "."

        start_pos = (len(requests) - 2, 1)
        end_pos = (1, len(requests[1]) - 2)

        dist = defaultdict(lambda: 2 ** 63 - 1)
        dist[start_pos] = 0
        prev = dict()
        construct_graph(start_pos, requests, graph, (0, 1), dist, prev)
        print(dist[end_pos])


def construct_graph(pos, map, prev_dir, dist, prev, end_pos):
    frontier = list()
    frontier.append((pos, prev_dir))
    while frontier:
        random.seed(random.randint(0, 2**63))
        element = frontier.pop()
        pos = element[0]
        if pos == end_pos and dist[pos] == 85420:
            break
        prev_dir = element[1]
        directions = aoc_helper.DIRECTION_WITHOUT_DIAG.copy()
        random.shuffle(directions)


        match prev_dir:
            case (1, 0):
                directions.remove((-1, 0))
            case (-1, 0):
                directions.remove((1, 0))
            case (0, 1):
                directions.remove((0, -1))
            case (0, -1):
                directions.remove((0, 1))

        for dir in directions:
            new_pos = aoc_helper.add_tuple(dir, pos)
            if map[new_pos[0]][new_pos[1]] == ".":
                weight = 1 if prev_dir == dir else 1001
                if dist[new_pos] > dist[pos] + weight:
                    frontier.append((new_pos, dir))
                    #random.shuffle(frontier)
                    prev[new_pos] = pos
                    dist[new_pos] = dist[pos] + weight
                else:
                    continue



if __name__ == '__main__':

    graph = defaultdict(list)
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(list(line.strip("\n")))
    requests[len(requests) - 2][1] = "."
    requests[1][len(requests[0]) - 2] = "."

    start_pos = (len(requests) - 2, 1)
    end_pos = (1, len(requests[1]) - 2)

    count = 0
    visited_map = list()
    for i in range(len(requests)):
        visited_map.append(len(requests[i]) * [0])
    visited_map[start_pos[0]][start_pos[1]] = 1
    visited_map[end_pos[0]][end_pos[1]] = 1

    while count < 1000:
        print(count)
        dist = defaultdict(lambda: 2 ** 63 - 1)
        prev = dict()
        if not count % 2:
            dist[start_pos] = 0
            construct_graph(start_pos, requests, (0, 1), dist, prev, end_pos)
            previous_pos = end_pos
        else:
            dist[end_pos] = 0
            construct_graph(end_pos, requests, (0, 1), dist, prev, start_pos)
            previous_pos = start_pos
        while prev[previous_pos]:
            visited_map[previous_pos[0]][previous_pos[1]] = 1
            #print(dist[previous_pos], previous_pos)
            previous_pos = prev[previous_pos]
            if previous_pos not in prev:
                break
        debug_helper.print_grid(visited_map, True)
        print(sum([sum(i) for i in visited_map]))

        count += 1

    debug_helper.print_grid(visited_map, True)
    #print(sum([sum(i) for i in visited_map]))
