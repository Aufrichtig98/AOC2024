from aoc_helper import *
from collections import defaultdict

def dfs(pos, edge_graph, nodes, seen):
    if nodes[pos[0]][pos[1]] == 9:
        seen[pos[0]][pos[1]] += 1
    if not edge_graph[(pos[0],pos[1])]:
        return
    for edge in edge_graph[(pos[0], pos[1])]:
        dfs(edge, edge_graph, nodes, seen)
def part_one():
    def dfs(pos, edge_graph, nodes, seen):
        if nodes[pos[0]][pos[1]] == 9:
            seen[pos[0]][pos[1]] = 1
        if not edge_graph[(pos[0], pos[1])]:
            return
        for edge in edge_graph[(pos[0], pos[1])]:
            dfs(edge, edge_graph, nodes, seen)

    def part_one():
        pass

    if __name__ == '__main__':
        requests = list()
        edge_graph = defaultdict(list)
        with open("test.txt", "rt") as myfile:
            for line in myfile:
                requests.append(list_of_intstr_to_int(["100" if i == "." else i for i in list(line.strip("\n"))]))

        for i in range(len(requests)):
            for j in range(len(requests[i])):
                for direction in [-1, 1]:
                    pos = (i + direction, j)
                    if not out_of_bounce(requests, pos):
                        if requests[pos[0]][pos[1]] - requests[i][j] == 1:
                            edge_graph[(i, j)].append(pos)
                    pos = (i, j + direction)
                    if not out_of_bounce(requests, pos):
                        if requests[pos[0]][pos[1]] - requests[i][j] == 1:
                            edge_graph[(i, j)].append(pos)

        for i in range(len(requests)):
            for j in range(len(requests[i])):
                if requests[i][j] == 0:
                    edge_graph[(-1, -1)].append((i, j))

        seen = list()
        for i in requests:
            seen.append([0] * len(i))

        result = 0

        for pos in edge_graph[(-1), (-1)]:
            seen = list()
            for i in requests:
                seen.append([0] * len(i))
            dfs(pos, edge_graph, requests, seen)
            result += sum([sum(i) for i in seen])
        print(result)


if __name__ == '__main__':
    requests = list()
    edge_graph = defaultdict(list)
    with open("test.txt", "rt") as myfile:
        for line in myfile:
            requests.append(list_of_intstr_to_int(["100" if i == "." else i for i in list(line.strip("\n"))]))

    for i in range(len(requests)):
        for j in range(len(requests[i])):
            for direction in [-1,1]:
                pos = (i + direction, j)
                if not out_of_bounce(requests, pos):
                    if  requests[pos[0]][pos[1]] - requests[i][j] == 1:
                        edge_graph[(i,j)].append(pos)
                pos = (i, j + direction)
                if not out_of_bounce(requests, pos):
                    if  requests[pos[0]][pos[1]] - requests[i][j] == 1:
                        edge_graph[(i,j)].append(pos)

    for i in range(len(requests)):
        for j in range(len(requests[i])):
            if requests[i][j] == 0:
                edge_graph[(-1,-1)].append((i,j))

    seen = list()
    for i in requests:
        seen.append([0]*len(i))

    result = 0

    for pos in edge_graph[(-1),(-1)]:
        seen = list()
        for i in requests:
            seen.append([0] * len(i))
        dfs(pos, edge_graph, requests,seen)
        result += sum([sum(i) for i in seen])
    print(result)