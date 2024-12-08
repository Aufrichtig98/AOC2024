from aoc_helper import *
def part_one():
    requests = list()
    antennas = defaultdict(list)
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(list(line.strip("\n")))
    anti_nodes = list()
    for i in range(len(requests)):
        anti_nodes.append([0] * len(requests[0]))
    for i in range(len(requests)):
        for j in range(len(requests[i])):
            if requests[i][j] != ".":
                antennas[requests[i][j]].append((i, j))

    for value in antennas.values():
        for i in range(len(value)):
            for j in range(i + 1, len(value)):
                coords_diff_one = get_diff_coord(value[i], value[j])

                new_koord = (value[i][0] + coords_diff_one[0], value[i][1] + coords_diff_one[1])
                if not (out_of_bounce(requests, new_koord) or new_koord == value[j]):
                    anti_nodes[new_koord[0]][new_koord[1]] = 1
                new_koord = (value[i][0] - coords_diff_one[0], value[i][1] - coords_diff_one[1])
                if not (out_of_bounce(requests, new_koord) or new_koord == value[j]):
                    anti_nodes[new_koord[0]][new_koord[1]] = 1
                new_koord = (value[j][0] + coords_diff_one[0], value[j][1] + coords_diff_one[1])
                if not (out_of_bounce(requests, new_koord) or new_koord == value[i]):
                    anti_nodes[new_koord[0]][new_koord[1]] = 1
                new_koord = (value[j][0] - coords_diff_one[0], value[j][1] - coords_diff_one[1])
                if not (out_of_bounce(requests, new_koord) or new_koord == value[i]):
                    anti_nodes[new_koord[0]][new_koord[1]] = 1

    print(sum([sum(i) for i in anti_nodes]))

def get_diff_coord(pos_one, pos_two):
    return pos_one[0] - pos_two[0], pos_one[1]-pos_two[1]


if __name__ == '__main__':
    requests = list()
    antennas = defaultdict(list)
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(list(line.strip("\n")))
    anti_nodes = list()
    for i in range(len(requests)):
        anti_nodes.append([0] * len(requests[0]))
    for i in range(len(requests)):
        for j in range(len(requests[i])):
            if requests[i][j] != ".":
                antennas[requests[i][j]].append((i,j))

    for value in antennas.values():
        for i in range(len(value)):
            for j in range(i+1,len(value)):
                coords_diff_one = get_diff_coord(value[i], value[j])

                new_koord = (value[i][0] + coords_diff_one[0], value[i][1] + coords_diff_one[1])
                while not (out_of_bounce(requests, new_koord)):
                    anti_nodes[new_koord[0]][new_koord[1]] = 1
                    new_koord =add_tuple(new_koord, coords_diff_one)
                new_koord = (value[i][0] - coords_diff_one[0], value[i][1] - coords_diff_one[1])
                while not (out_of_bounce(requests, new_koord)):
                    anti_nodes[new_koord[0]][new_koord[1]] = 1
                    new_koord =add_tuple(new_koord, coords_diff_one, substract=True)
                new_koord = (value[j][0] + coords_diff_one[0], value[j][1] + coords_diff_one[1])
                while not (out_of_bounce(requests, new_koord)):
                    anti_nodes[new_koord[0]][new_koord[1]] = 1
                    new_koord =add_tuple(new_koord, coords_diff_one)
                new_koord = (value[j][0] - coords_diff_one[0], value[j][1] - coords_diff_one[1])
                while not (out_of_bounce(requests, new_koord)):
                    anti_nodes[new_koord[0]][new_koord[1]] = 1
                    new_koord =add_tuple(new_koord, coords_diff_one, substract=True)

    print(sum([sum(i) for i in anti_nodes]))