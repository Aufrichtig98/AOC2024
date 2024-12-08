def print_grid(matrix):
    highest_digit = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > highest_digit:
                highest_digit = matrix[i][j]
    len_highest_digit = len(str(highest_digit))

    print("\n")
    print_string = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            diff_len_spaces  = " " * (len(str(highest_digit)) - len(str(matrix[i][j])))
            print_string += f"{diff_len_spaces}{str(matrix[i][j])} "
        print_string += "\n"
    print(print_string)