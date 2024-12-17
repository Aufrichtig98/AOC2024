import aoc_helper
from collections import defaultdict
def part_one():
    if __name__ == '__main__':
        requests = str()
        map = list()
        with open("input.txt", "rt") as myfile:
            switch = True
            for line in myfile:
                if line == "\n":
                    switch = False
                    continue
                if switch:
                    map.append(list(line.strip("\n"))[1:][:-1])
                else:
                    requests += line.strip("\n")

        map = map[1:][:-1]
        player_pos = 0
        for i in range(len(map)):
            for j in range(len(map[i])):
                if "@" == map[i][j]:
                    player_pos = (i, j)

        for i in requests:
            direction = (0, -1)
            match i:
                case "^":
                    direction = (-1, 0)
                case "v":
                    direction = (1, 0)
                case ">":
                    direction = (0, 1)
            pos_to_move = aoc_helper.add_tuple(player_pos, direction)
            if aoc_helper.out_of_bounce(map, pos_to_move) or map[pos_to_move[0]][pos_to_move[1]] == "#":
                continue
            if map[pos_to_move[0]][pos_to_move[1]] == ".":
                map[player_pos[0]][player_pos[1]] = "."
                player_pos = pos_to_move
                map[pos_to_move[0]][pos_to_move[1]] = "@"

            else:
                possible = True
                while True:
                    pos_to_move = aoc_helper.add_tuple(pos_to_move, direction)
                    if aoc_helper.out_of_bounce(map, pos_to_move) or map[pos_to_move[0]][pos_to_move[1]] == "#":
                        possible = False
                        break
                    if map[pos_to_move[0]][pos_to_move[1]] == ".":
                        break
                if not possible:
                    continue

                current_pos = aoc_helper.add_tuple(player_pos, direction)
                while True:
                    target_pos = aoc_helper.add_tuple(current_pos, direction)
                    map[target_pos[0]][target_pos[1]] = "O"
                    current_pos = target_pos
                    if current_pos == pos_to_move:
                        break
                map[player_pos[0]][player_pos[1]] = "."
                player_pos = aoc_helper.add_tuple(player_pos, direction)
                map[player_pos[0]][player_pos[1]] = "@"

        result = 0
        for i in range(len(map)):
            for j in range(len(map)):
                if map[i][j] == 'O':
                    result += 100 * (i + 1) + (j + 1)
        print(result)


if __name__ == '__main__':
    requests = str()
    map = list()
    with open("input.txt", "rt") as myfile:
        switch = True
        for line in myfile:
            if line == "\n":
                switch = False
                continue
            if switch:
                map.append(list(line.strip("\n"))[1:][:-1])
            else:
                requests += line.strip("\n")

    map = map[1:][:-1]
    player_pos = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if "@" == map[i][j]:
                player_pos = (i,j)

    for i in requests:
        direction = (0,-1)
        match i:
            case "^":
                direction = (-1,0)
            case "v":
                direction = (1,0)
            case ">":
                direction = (0,1)
        pos_to_move = aoc_helper.add_tuple(player_pos, direction)
        if aoc_helper.out_of_bounce(map, pos_to_move) or map[pos_to_move[0]][pos_to_move[1]] == "#":
            continue
        if map[pos_to_move[0]][pos_to_move[1]] == ".":
            map[player_pos[0]][player_pos[1]] = "."
            player_pos = pos_to_move
            map[pos_to_move[0]][pos_to_move[1]] = "@"

        else:
            possible = True
            while True:
                pos_to_move = aoc_helper.add_tuple(pos_to_move, direction)
                if aoc_helper.out_of_bounce(map, pos_to_move) or map[pos_to_move[0]][pos_to_move[1]] == "#":
                    possible = False
                    break
                if map[pos_to_move[0]][pos_to_move[1]] == ".":
                    break
            if not possible:
                continue

            current_pos = aoc_helper.add_tuple(player_pos, direction)
            while True:
                target_pos = aoc_helper.add_tuple(current_pos, direction)
                map[target_pos[0]][target_pos[1]] = "O"
                current_pos = target_pos
                if current_pos == pos_to_move:
                    break
            map[player_pos[0]][player_pos[1]] = "."
            player_pos = aoc_helper.add_tuple(player_pos, direction)
            map[player_pos[0]][player_pos[1]] = "@"


    result = 0
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == 'O':
                result += 100* (i+1) + (j+1)
    print(result)