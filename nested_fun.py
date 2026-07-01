def create_matrix(n):
    matrix = []
    for row in range(n * 2 - 1):
        new_row = []
        if row < n: # define length of each row
            row_len = row + 1
        else:
            row_len = n * 2 - 1 - row
        for column in range(row_len):
            new_row.append(column + 1) # adds ascending numbers in each column until the max length of each row
        matrix.append(new_row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            if row[-1] > element: # if last item in the row is bigger than the current element, don't do a line break
                print(str(element) + " ", end="")
            elif row[-1] == element: # if last item in the row is the same as the current element, do a line-break after printing
                print(str(element) + " ")


def print_triangle(n):
    matrix = create_matrix(n)
    print_matrix(matrix)


print_triangle(n=5)