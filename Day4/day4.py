from aoc_helper import *

def move_direction(matrix, position, direction):
    substring = matrix[position[0]][position[1]]
    for i in range(3):
        position = tuple(map(lambda i,j: i + j, position, direction))
        if out_of_bounce(matrix, position):
            return ""
        substring += matrix[position[0]][position[1]]
    return substring


def move_direction_part2(matrix, position, direction):
    substring = ""
    for i in range(1):
        position = tuple(map(lambda i,j: i + j, position, direction))
        if out_of_bounce(matrix, position):
            return ""
        substring += matrix[position[0]][position[1]]
    return substring

def part_one():
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(list(line.strip("\n").split(" ")[0]))

    count = 0
    for i in range(0, len(requests)):
        for j in range(0, len(requests[0])):
            count += move_direction(requests, (i, j), (0, 1)) == "XMAS"
            count += move_direction(requests, (i, j), (0, -1)) == "XMAS"
            count += move_direction(requests, (i, j), (1, 0)) == "XMAS"
            count += move_direction(requests, (i, j), (-1, 0)) == "XMAS"
            count += move_direction(requests, (i, j), (1, 1)) == "XMAS"
            count += move_direction(requests, (i, j), (1, -1)) == "XMAS"
            count += move_direction(requests, (i, j), (-1, -1)) == "XMAS"
            count += move_direction(requests, (i, j), (-1, 1)) == "XMAS"

    print(count)


if __name__ == '__main__':
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(list(line.strip("\n").split(" ")[0]))

    count = 0
    for i in range(0, len(requests)):
        for j in range(0, len(requests[0])):
            if not requests[i][j] == "A":
                continue
            diag = move_direction_part2(requests, (i, j), (1, 1)) + "A" \
            + move_direction_part2(requests, (i, j), (-1, -1))
            if not (diag == "SAM" or diag == "MAS"):
                continue

            diag = move_direction_part2(requests, (i, j), (1, -1)) + "A" \
                    + move_direction_part2(requests, (i, j), (-1, 1))

            if diag == "SAM" or diag == "MAS":
                count += 1


    print(count)