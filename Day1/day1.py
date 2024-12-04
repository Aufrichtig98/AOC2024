from collections import defaultdict

def part_one():
    if __name__ == '__main__':
        requests_left = list()
        requests_right = list()
        with open("input.txt", "rt") as myfile:
            for line in myfile:
                tmp = line.strip("\n").split(" ")
                requests_left.append(int(tmp[0]))
                requests_right.append(int(tmp[-1]))

        requests_right.sort()
        requests_left.sort()
        result = 0
        for i in range(len(requests_left)):
            result += abs(requests_left[i] - requests_right[i])
        print(result)


if __name__ == '__main__':
    requests_left = list()
    count_dict = defaultdict(int)
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            tmp = line.strip("\n").split(" ")
            requests_left.append(int(tmp[0]))
            count_dict[int(tmp[-1])] += 1


    result = 0
    for i in requests_left:
        result += i * count_dict[i]
    print(result)
