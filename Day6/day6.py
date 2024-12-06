from aoc_helper import *
import copy
directions = [(-1,0), (0,1), (1,0), (0,-1)]

def part_one():
    if __name__ == '__main__':
        requests = list()
        with open("input.txt", "rt") as myfile:
            for line in myfile:
                requests.append(list(line.strip("\n")))

        map = list()
        for _ in range(len(requests)):
            map.append([0] * len(requests[0]))

        guard_pos = (0, 0)
        for i in range(len(requests)):
            for j in range(len(requests[i])):
                if requests[i][j] == "^":
                    guard_pos = (i, j)
                    map[i][j] = 0
                    continue
                if requests[i][j] == ".":
                    map[i][j] = 0
                else:
                    map[i][j] = 1

        visited_map = list()
        for _ in range(len(requests)):
            visited_map.append([0] * len(requests[0]))

        current_direction = 0
        while True:
            visited_map[guard_pos[0]][guard_pos[1]] = 1

            if out_of_bounce(map, (
            guard_pos[0] + directions[current_direction][0], guard_pos[1] + directions[current_direction][1])):
                break
            if map[guard_pos[0] + directions[current_direction][0]][
                guard_pos[1] + directions[current_direction][1]] == 1:
                current_direction = (current_direction + 1) % 4
            else:
                guard_pos = (
                guard_pos[0] + directions[current_direction][0], guard_pos[1] + directions[current_direction][1])


if __name__ == '__main__':
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(list(line.strip("\n")))

    map = list()
    for _ in range(len(requests)):
        map.append([0] * len(requests[0]))

    start_pos = (0,0)
    for i in range(len(requests)):
        for j in range(len(requests[i])):
            if requests[i][j] == "^":
                start_pos = (i,j)
                map[i][j] = 0
                continue
            if requests[i][j] == ".":
                map[i][j] = 0
            else:
                map[i][j] = 1
    guard_pos = start_pos

    visited_map = list()
    for _ in range(len(requests)):
        visited_map.append([0] * len(requests[0]))


    current_direction = 0
    boulder_locations = list()
    for _ in range(len(requests)):
        boulder_locations.append([0] * len(requests[0]))

    while True:
        visited_map[guard_pos[0]][guard_pos[1]] = 1
        if out_of_bounce(map, (guard_pos[0] + directions[current_direction][0], guard_pos[1] + directions[current_direction][1])):
            break
        if map[guard_pos[0] + directions[current_direction][0]] [guard_pos[1] + directions[current_direction][1]] == 1:
            current_direction = (current_direction + 1) % 4
        else:
            guard_pos = (guard_pos[0] + directions[current_direction][0], guard_pos[1] + directions[current_direction][1])

    possible_boulder_list = list()
    for i in range(len(requests)):
        for j in range(len(requests[i])):
            if visited_map[i][j]:
                possible_boulder_list.append((i,j))

    result = 0
    result_pos = list()

    for i in possible_boulder_list:
        map_copy = copy.deepcopy(map)
        map_copy[i[0]][i[1]] = 1
        found_exit = False
        previous_direction_changes = [(-1, -2), (-1, -3), (-1, -4), (-1, -5), (-1, -6)]
        guard_pos = start_pos
        visited_map = list()
        current_direction = 0

        while True:
            if out_of_bounce(map_copy, (
            guard_pos[0] + directions[current_direction][0], guard_pos[1] + directions[current_direction][1])):
                found_exit = True
                break
            if map_copy[guard_pos[0] + directions[current_direction][0]][
                guard_pos[1] + directions[current_direction][1]] == 1:
                if guard_pos != previous_direction_changes[-1]:
                    previous_direction_changes.append(guard_pos)
                if len(set(previous_direction_changes)) != len(previous_direction_changes):
                    break

                current_direction = (current_direction + 1) % 4
            else:
                guard_pos = (
                guard_pos[0] + directions[current_direction][0], guard_pos[1] + directions[current_direction][1])

        if not found_exit:
            result += 1
            result_pos.append(i)

    print(result)