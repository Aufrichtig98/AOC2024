import aoc_helper
from collections import defaultdict
def part_one():
    pass


if __name__ == '__main__':
    requests = list()
    instr_pointer = 0
    program = list()
    register = [0,0,0]

    with open("input.txt", "rt") as myfile:
        register[0] = int(myfile.readline().strip("\n").split("Register A: ")[-1])
        register[1] = int(myfile.readline().strip("\n").split("Register B: ")[-1])
        register[2] = int (myfile.readline().strip("\n").split("Register C: ")[-1])
        myfile.readline()
        program = aoc_helper.list_of_intstr_to_int(myfile.readline().strip("\n").split("Program: ")[-1].split(","))

    output = ""

    def combo(combo_operand):
        match combo_operand:
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 3
            case 4:
                return register[0]
            case 5:
                return register[1]
            case 6:
                return register[2]
            case 6:
                return -1

    while instr_pointer < len(program):
        operand = program[instr_pointer+1]

        match program[instr_pointer]:
            case 0:
                register[0] = register[0] // (2**combo(operand))
            case 1:
                register[1] ^= operand
            case 2:
                register[1] = combo(operand) % 8
            case 3:
                instr_pointer = instr_pointer if register[0] == 0 else operand
                if register[0] != 0:
                    continue
            case 4:
                register[1] ^= register[2]
            case 5:
                output += f"{combo(operand) % 8},"
            case 6:
                register[1] = register[0] // (2 ** combo(operand))
            case 7:
                register[2] = register[0] // (2 ** combo(operand))

        instr_pointer += 2

    if output[-1] == ",":
        print(output[:-1])
    else:
        print(output)
