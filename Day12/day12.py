import aoc_helper
from collections import defaultdict

LEFT_DOWN = [(1,0), (0,1)]

def coord_mapping_2d_to_1d(pos, matrix):
    return len(matrix) * pos[0] + pos[1]

def coord_mapping_1d_to_2d(pos, matrix):
    return pos // len(matrix), pos % len(matrix)

def part_one():
    if __name__ == '__main__':

        garden = list()
        with open("input.txt", "rt") as myfile:
            for line in myfile:
                garden.append(list(line.strip("\n")))

        uf_plots = aoc_helper.UnionFind(range(len(garden) * len(garden[0])))

        for i in range(len(garden)):
            for j in range(len(garden[i])):
                for dir in LEFT_DOWN:
                    new_coord = i + dir[0], j + dir[1]
                    if not aoc_helper.out_of_bounce(garden, new_coord):
                        if garden[i][j] == garden[new_coord[0]][new_coord[1]]:
                            if not uf_plots.connected(coord_mapping_2d_to_1d((i, j), garden),
                                                      coord_mapping_2d_to_1d(new_coord, garden)):
                                uf_plots.union(coord_mapping_2d_to_1d((i, j), garden),
                                               coord_mapping_2d_to_1d(new_coord, garden))

        plots = set()
        for i in uf_plots.component_mapping().values():
            tmp = list()
            for j in i:
                tmp.append(coord_mapping_1d_to_2d(j, garden))
            plots.add(tuple(tmp))
        plots = list(plots)

        result = 0
        for plot in plots:
            area = len(plot)
            perimeter = 0
            for element in plot:
                for coord in aoc_helper.DIRECTION_WITHOUT_DIAG:
                    new_coord = aoc_helper.add_tuple(coord, element)
                    if aoc_helper.out_of_bounce(garden, new_coord):
                        perimeter += 1
                        continue
                    else:
                        if garden[new_coord[0]][new_coord[1]] != garden[element[0]][element[1]]:
                            perimeter += 1
            result += perimeter * area
        print(result)

if __name__ == '__main__':

    garden = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            garden.append(list(line.strip("\n")))

    uf_plots = aoc_helper.UnionFind(range(len(garden) * len(garden[0])))

    for i in range(len(garden)):
        for j in range(len(garden[i])):
            for dir in LEFT_DOWN:
                new_coord = i + dir[0], j + dir[1]
                if not aoc_helper.out_of_bounce(garden, new_coord):
                    if garden[i][j] == garden[new_coord[0]][new_coord[1]]:
                        if not uf_plots.connected(coord_mapping_2d_to_1d((i, j), garden),
                                                  coord_mapping_2d_to_1d(new_coord, garden)):
                            uf_plots.union(coord_mapping_2d_to_1d((i, j), garden),
                                           coord_mapping_2d_to_1d(new_coord, garden))

    plots = set()
    for i in uf_plots.component_mapping().values():
        tmp = list()
        for j in i:
            tmp.append(coord_mapping_1d_to_2d(j, garden))
        plots.add(tuple(tmp))
    plots = list(plots)

    fence_done = list()
    for i in range(len(garden)):
        tmp = list()
        for j in range(len(garden[i])):
            tmp.append({"West": False, "East": False, "South": False, "North": False})


    # Kondition Top/left , TopRiht... or TopLeft And TopRight with Diagonal free

    aoc_helper.DIRECTION_WITHOUT_DIAG.append((1,0))
    result = 0
    for plot in plots:
        area = len(plot)
        perimeter = 0
        for element in plot:
            for i in range(len(aoc_helper.DIRECTION_WITHOUT_DIAG)-1):
                new_coord_one = aoc_helper.add_tuple(aoc_helper.DIRECTION_WITHOUT_DIAG[i], element)
                new_coord_two = aoc_helper.add_tuple(aoc_helper.DIRECTION_WITHOUT_DIAG[i+1], element)
                cord_one_good = False
                cord_two_good = False
                if aoc_helper.out_of_bounce(garden, new_coord_one):
                    cord_one_good = True
                if aoc_helper.out_of_bounce(garden, new_coord_two):
                    cord_two_good = True

                if not cord_one_good:
                    if garden[new_coord_one[0]][new_coord_one[1]] != garden[element[0]][element[1]]:
                        cord_one_good = True
                if not cord_two_good:
                    if garden[new_coord_two[0]][new_coord_two[1]] != garden[element[0]][element[1]]:
                        cord_two_good = True

                if cord_one_good and cord_two_good:
                    perimeter += 1
                    continue

                if aoc_helper.out_of_bounce(garden, new_coord_one) and aoc_helper.out_of_bounce(garden, new_coord_two):
                    continue

                diag = aoc_helper.add_tuple(aoc_helper.DIRECTION_WITHOUT_DIAG[i], aoc_helper.DIRECTION_WITHOUT_DIAG[i+1])
                diag = aoc_helper.add_tuple(element, diag)
                if garden[new_coord_two[0]][new_coord_two[1]] == garden[element[0]][element[1]] and \
                   garden[new_coord_one[0]][new_coord_one[1]] == garden[element[0]][element[1]] and \
                   garden[diag[0]][diag[1]] != garden[element[0]][element[1]]:
                    perimeter += 1
        result += perimeter * area
    print(result)