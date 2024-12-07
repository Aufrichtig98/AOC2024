import math

from aoc_helper import *

def part_one():
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            tmp = line.strip("\n").split(":")
            tmp[1] = tmp[1].split(" ")[1:]
            tmp[0] = int(tmp[0])
            tmp[1] = [int(tmp[1][i]) for i in range(len(tmp[1]))]
            requests.append(tmp)

    result = list()

    for i in requests:
        sum_val = i[0]
        equation_size = len(i[1])
        for j in range(2 ** (len(i[1]) - 1)):
            acc = i[1][0]
            for k in range(equation_size - 1):
                if (j >> k) & 1:
                    acc *= i[1][k + 1]
                else:
                    acc += i[1][k + 1]
            if sum_val == acc:
                result.append(i[0])
                break
    print(sum(result))


if __name__ == '__main__':
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            tmp = line.strip("\n").split(":")
            tmp[1] = tmp[1].split(" ")[1:]
            tmp[0] = int(tmp[0])
            tmp[1] = [int(tmp[1][i]) for i in range(len(tmp[1]))]
            requests.append(tmp)

    result = list()

    for i in requests:
        print(i)
        sum_val = i[0]
        equation_size = len(i[1])
        for j in range(4** (len(i[1])-1)):
            acc = i[1][0]
            early_exit = False
            for k in range(equation_size - 1):
                if (j >> 2*k) & 3 == 3:
                    acc *=  i[1][k+1]
                elif (j >> 2*k) & 2 == 2:
                    acc += i[1][k+1]
                elif (j >> 2 * k) & 1 == 1:
                    acc = int(str(acc) + str(i[1][k+1]))
                else:
                    early_exit = True
                    break
            if sum_val == acc and not early_exit:
                result.append(i[0])
                break
    print(sum(result))

