from aoc_helper import *
from collections import defaultdict
def part_one():
    if __name__ == '__main__':
        requests = list()
        with open("input.txt", "rt") as myfile:
            for line in myfile:
                requests.append(line.strip("\n"))
            requests = requests[0]
        fragmented_input = ""

        id = 0
        for i in range(len(requests)):
            fragmented_input += f"{id}|" * int(requests[i]) if i % 2 == 0 else ".|" * int(requests[i])
            if not i % 2:
                id += 1
        fragmented_input = fragmented_input.split("|")[:-1]
        unfragmented_string = list()
        idx = 0
        while idx < len(fragmented_input):
            if idx == len(fragmented_input):
                break
            if fragmented_input[idx] == ".":
                while True:
                    if fragmented_input[-1] == ".":
                        fragmented_input = fragmented_input[:-1]
                    else:
                        break
                unfragmented_string.append(fragmented_input[-1])
                fragmented_input = fragmented_input[:-1]
            else:
                unfragmented_string.append(fragmented_input[idx])
            idx += 1

        checksum = sum([idx * int(i) for idx, i in enumerate(unfragmented_string)])
        print(checksum)


if __name__ == '__main__':
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(line.strip("\n"))
        requests = requests[0]
    fragmented_input = list()

    id = 0
    for i in range(len(requests)):
        fragmented_input.append([f"{id}"] * int(requests[i]) if i % 2 == 0 else ["."] * int(requests[i]))
        if len(fragmented_input[-1]) == 0:
            fragmented_input = fragmented_input[:-1]
        if not i % 2:
            id += 1
    unfragmented = list()

    last_idx = len(fragmented_input) - 1
    while last_idx > 0:
        if "." in fragmented_input[last_idx]:
            last_idx -= 1
            continue
        else:
            for i in range(0, last_idx):
                if len(fragmented_input[i]) >= len(fragmented_input[last_idx]) and "." in fragmented_input[i]:
                    diff = len(fragmented_input[i]) - len(fragmented_input[last_idx])
                    fragmented_input[i] = fragmented_input[last_idx]
                    if diff:
                        fragmented_input.insert(i+1, ["."] * diff)
                        last_idx += 1
                        fragmented_input[last_idx] = ["."] * len(fragmented_input[i])
                    else:
                        fragmented_input[last_idx] = ["."] * len(fragmented_input[i])
                    break
            last_idx -= 1



    checksum = sum([idx * int(i) if i != "." else 0 for idx,i in enumerate(reduce(lambda x,y: x + y, fragmented_input))])
    print(checksum)