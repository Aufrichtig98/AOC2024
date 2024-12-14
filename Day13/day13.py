import aoc_helper
from collections import defaultdict
from z3 import *

def part_one():
    cranes = list()
    with open("input.txt", "rt") as myfile:
        cranes.append(list())
        counter = 0
        for line in myfile:
            if line == "\n":
                continue
            line = line.strip("\n").split(":")[1].strip(" ")
            line = line.split(", ")
            if counter % 3 == 0 or counter % 3 == 1:
                cranes[-1].append((int(line[0].split("X+")[-1]), int(line[1].split("Y+")[-1])))
            else:
                cranes[-1].append((int(line[0].split("X=")[-1]), int(line[1].split("Y=")[-1])))
                cranes.append(list())
            counter += 1
        cranes = cranes[:-1]
    result = 0
    for crane_game in cranes:
        solver = Solver()
        button_one = Int("i")
        button_two = Int("j")
        solver.add(button_one >= 0)
        solver.add(button_two >= 0)
        solver.add(button_one <= 100)
        solver.add(button_two <= 100)
        solver.add(button_one * crane_game[0][0] + button_two * crane_game[1][0] == crane_game[2][0])
        solver.add(button_one * crane_game[0][1] + button_two * crane_game[1][1] == crane_game[2][1])

        # appearently sat is a keyword or type in z3 that says if its satisfiable
        if solver.check() == sat:
            # model gives the solutions
            solution = solver.model()
            # To get the ints we need to call as_long
            result += 3 * solution[button_one].as_long() + solution[button_two].as_long()

    print(result)


if __name__ == '__main__':
    prin
    cranes = list()
    with open("input.txt", "rt") as myfile:
        cranes.append(list())
        counter = 0
        for line in myfile:
            if line == "\n":
                continue
            line = line.strip("\n").split(":")[1].strip(" ")
            line = line.split(", ")
            if counter % 3 == 0 or counter % 3 == 1:
                cranes[-1].append((int(line[0].split("X+")[-1]), int(line[1].split("Y+")[-1])))
            else:
                cranes[-1].append((int(line[0].split("X=")[-1]) + 10000000000000, int(line[1].split("Y=")[-1])+ 10000000000000))
                cranes.append(list())
            counter += 1
        cranes = cranes[:-1]
    result = 0
    for crane_game in cranes:
        solver = Solver()
        button_one = Int("i")
        button_two = Int("j")
        solver.add(button_one >= 0)
        solver.add(button_two >= 0)
        solver.add(button_one*crane_game[0][0] + button_two*crane_game[1][0] == crane_game[2][0])
        solver.add(button_one * crane_game[0][1] + button_two * crane_game[1][1] == crane_game[2][1])

        #appearently sat is a keyword or type in z3 that says if its satisfiable
        if solver.check() == sat:
            #model gives the solutions
            solution = solver.model()
            # To get the ints we need to call as_long
            result += 3 * solution[button_one].as_long() + solution[button_two].as_long()

    print(result)
