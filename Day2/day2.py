import copy

def part_one():
    if __name__ == '__main__':
        requests = list()
        with open("input.txt", "rt") as myfile:
            for line in myfile:
                requests.append(list())
                for i in line.strip("\n").split(" "):
                    requests[-1].append(int(i))

        safe_reports = 0

        for i in requests:
            safe = True
            for j in range(len(i) - 1):
                if i[j] < i[j + 1] and abs(i[j] - i[j + 1]) > 0 and abs(i[j] - i[j + 1]) <= 3:
                    continue
                else:
                    safe = False
                    break
            if safe:
                safe_reports += 1

        for i in requests:
            safe = True
            for j in range(len(i) - 1):
                if i[j] > i[j + 1] and abs(i[j] - i[j + 1]) > 0 and abs(i[j] - i[j + 1]) <= 3:
                    continue
                else:
                    safe = False
                    break
            if safe:
                safe_reports += 1

        print(safe_reports)


if __name__ == '__main__':
    if __name__ == '__main__':
        requests = list()
        with open("input.txt", "rt") as myfile:
            for line in myfile:
                requests.append(list())
                for i in line.strip("\n").split(" "):
                    requests[-1].append(int(i))

        safe_reports = 0



        for i in requests:
            for k in range(len(i)):
                copy_req = copy.deepcopy(i)
                copy_req.pop(k)
                safe = True
                for j in range(len(copy_req) - 1):
                    if copy_req[j] < copy_req[j + 1] and abs(copy_req[j] - copy_req[j + 1]) > 0 and abs(copy_req[j] - copy_req[j + 1]) <= 3:
                        continue
                    else:
                        safe = False
                        break
                if safe:
                    safe_reports += 1
                    break

        for i in requests:
            for k in range(len(i)):
                copy_req = copy.deepcopy(i)
                copy_req.pop(k)
                safe = True
                for j in range(len(copy_req) - 1):
                    if copy_req[j] > copy_req[j + 1] and abs(copy_req[j] - copy_req[j + 1]) > 0 and abs(copy_req[j] - copy_req[j + 1]) <= 3:
                        continue
                    else:
                        safe = False
                        break
                if safe:
                    safe_reports += 1
                    break

    print(safe_reports)