def generate_substrings(input_line, length):
    substings = list()
    current_string = " " * length
    for i in input_line:
        current_string = current_string[1:] + i
        substings.append(current_string)
    return substings

def rotate_matrix_90_degree(matrix):
    return list(zip(*(matrix[::-1])))

def out_of_bounce(matrix, position):
    x = len(matrix[0])
    y = len(matrix)
    if position[1] >= x:
        return True
    if position[1] < 0:
        return True
    if position[0] >= y:
        return True
    if position[0] < 0:
        return True
    return False