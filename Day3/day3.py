import re
def part_one():
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(line.strip("\n"))

    solution = 0

    for line in requests:
        match = "xxx"
        for i in range(len(line)):
            match = match[1:] + line[i]
            if match == "mul":
                i += 1
                if i >= len(line):
                    break
                multi = ""
                while line[i] != ")":
                    multi += line[i]
                    i += 1
                    if i >= len(line):
                        break
                digits = multi[1:].split(",")
                if len(digits) != 2:
                    continue
                if not digits[0].isdigit() or not digits[1].isdigit():
                    continue
                solution += int(digits[0]) * int(digits[1])
    print(solution)


if __name__ == '__main__':
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(line.strip("\n"))

    solution = 0

    doing_stuff = "xon't()"
    do_flag = True
    for line in requests:
        match = "xxx"
        for i in range(len(line)):
            match = match[1:] + line[i]
            doing_stuff = doing_stuff[1:] + line[i]
            if "do()" in doing_stuff:
                do_flag = True
            if "don't()" in doing_stuff:
                do_flag = False
            if match == "mul":
                i += 1
                doing_stuff = doing_stuff[1:] + line[i]
                if "do()" in doing_stuff:
                    do_flag = True
                if "don't()" in doing_stuff:
                    do_flag = False
                if i >= len(line):
                    break
                multi = ""
                while line[i] != ")":
                    multi += line[i]
                    i += 1
                    doing_stuff = doing_stuff[1:] + line[i]
                    if "do()" in doing_stuff:
                        do_flag = True
                    if "don't()" in doing_stuff:
                        do_flag = False
                    if i >= len(line):
                        break

                digits = multi[1:].split(",")
                if len(digits) != 2:
                    continue
                if not digits[0].isdigit() or not digits[1].isdigit():
                    continue
                if do_flag:
                    solution += int(digits[0]) * int(digits[1])
    print(solution)
