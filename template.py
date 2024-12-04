from aoc_helper import *

def part_one():
    pass


if __name__ == '__main__':
    requests = list()
    with open("test.txt", "rt") as myfile:
        for line in myfile:
            requests.append(line.strip("\n").split(" "))
