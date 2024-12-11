import aoc_helper
from collections import defaultdict
import math

def rule_set(digit):
    if digit == 0:
        return [1]
    digit = str(digit)
    if len(digit) % 2 == 0:
        return [int(digit[:len(digit)//2]), int(digit[len(digit)//2:])]
    else:
        return [int(digit)*2024]

def part_one():
    if __name__ == '__main__':

        requests = list()
        with open("input.txt", "rt") as myfile:
            for line in myfile:
                requests.append(aoc_helper.list_of_intstr_to_int(line.strip("\n").split(" ")))
            requests = requests[0]

        pre_computing = [[0]]
        for i in range(1, 40):
            pre_computing.append([])
            for j in pre_computing[i - 1]:
                pre_computing[i] += rule_set(j)
        result_digit = 0
        result = requests
        for i in range(25):
            tmp = list()
            for j in result:
                if j == 0:
                    result_digit += len(pre_computing[25 - i])
                else:
                    tmp += rule_set(j)
            result = tmp.copy()
        print(len(result) + result_digit)


if __name__ == '__main__':
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(aoc_helper.list_of_intstr_to_int(line.strip("\n").split(" ")))
        requests = requests[0]



    result_digit = 0
    results = defaultdict(int)
    for i in requests:
        results[i] += 1

    for i in range(75):
        new_dict = defaultdict(int)
        for key,value in results.items():
            for j in rule_set(key):
                new_dict[j] += value
        results = new_dict.copy()

    print(sum(value for key,value in results.items()))