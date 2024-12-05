from aoc_helper import *
from collections import defaultdict
from itertools import permutations

def part_one():
    requests = list()
    constraints = defaultdict(list)
    with open("input.txt", "rt") as myfile:
        switch = True
        for line in myfile:
            tmp = line.strip("\n").strip(" ")
            if tmp == "":
                switch = False
                continue
            if switch:
                tmp = tmp.split("|")
                constraints[int(tmp[0])].append(int(tmp[1]))
            else:
                requests.append([int(i) for i in tmp.split(",")])
    results = list()
    for i in requests:
        found = False
        for j in range(1, len(i)):
            for element in i[:(j+1)]:
                if element in constraints[i[j]]:
                    found = True
                    break
            if found:
                break
        if not found:
            results.append(i[len(i) // 2])

    return results

if __name__ == '__main__':
    # Could also be solved with topo sort but thats way too much effort to implement for a day 5 task
    requests = list()
    constraints = defaultdict(list)
    with open("input.txt", "rt") as myfile:
        switch = True
        for line in myfile:
            tmp = line.strip("\n").strip(" ")
            if tmp == "":
                switch = False
                continue
            if switch:
                tmp = tmp.split("|")
                constraints[int(tmp[0])].append(int(tmp[1]))
            else:
                requests.append([int(i) for i in tmp.split(",")])

    results = list()
    to_fix = list()
    for i in requests:
        found = False
        for j in range(1, len(i)):
            for element in i[:(j+1)]:
                if element in constraints[i[j]]:
                    found = True
                    to_fix.append(i)
                    break
            if found:
                break


    for i in to_fix:
        j = 1
        while j < len(i):
            for idx, element in enumerate(i[:(j+1)]):
                if element in constraints[i[j]]:
                    i[j] ^= i[idx]
                    i[idx] ^= i[j]
                    i[j] ^= i[idx]
                    j = 0
                    break
            j += 1
        results.append(i[len(i) // 2])

    print(sum(results))