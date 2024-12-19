import aoc_helper
from collections import defaultdict

import debug_helper


def part_one():
    if __name__ == '__main__':
        graph = list()
        width = 71
        height = 71
        for i in range(height):
            graph.append(list())
            for j in range(width):
                graph[i].append(1)

        with open("input.txt", "rt") as myfile:
            counter = 0
            for line in myfile:
                if counter >= 1024:
                    break
                x, y = tuple(aoc_helper.list_of_intstr_to_int(line.strip("\n").split(",")))
                graph[y][x] = 0
                counter += 1

        # start = (0,0)
        # goal = (6,6)
        start = (0, 0)
        goal = (70, 70)
        debug_helper.print_grid(graph, color=True)

        adj_graph = defaultdict(list)

        for i in range(height):
            for j in range(width):
                if graph[i][j] == 0:
                    continue
                for pos in (aoc_helper.get_elments_directions(1, graph, (i, j))):
                    if graph[pos[0]][pos[1]]:
                        adj_graph[(i, j)].append(((pos[0], pos[1]), 1))

        dist, _ = aoc_helper.dijkstra(adj_graph, start)
        print(dist[goal])


if __name__ == '__main__':
    graph = list()
    width = 71
    height = 71
    for i in range(height):
        graph.append(list())
        for j in range(width):
            graph[i].append(1)

    with open("input.txt", "rt") as myfile:
        counter = 0
        for line in myfile:
            print(counter)
            x, y = tuple(aoc_helper.list_of_intstr_to_int(line.strip("\n").split(",")))
            graph[y][x] = 0
            #start = (0,0)
            #goal = (6,6)
            start = (0,0)
            goal = (70,70)

            adj_graph = defaultdict(list)

            for i in range(height):
                for j in range(width):
                    if graph[i][j] == 0:
                        continue
                    for pos in (aoc_helper.get_elments_directions(1, graph, (i,j))):
                        if graph[pos[0]][pos[1]]:
                            adj_graph[(i, j)].append(((pos[0],pos[1]), 1))

            dist, _ = aoc_helper.dijkstra(adj_graph,start)

            if dist[goal] == 2**64-1:
                print(x,y)
                break
            counter += 1