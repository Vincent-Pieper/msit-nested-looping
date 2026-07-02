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


print_triangle(n=20)




def prevent_mult_by_zero(row, column):
    if row == 0:
        row = 1
    if column == 0:
        column = 1
    return row, column

def adjust_spacing_and_print(n, print_number):
    str_number = str(print_number)
    while len(str_number) < len(str(n * n))+1: # spreads the printed matrix depending on the longest int + 1
        str_number += " "
    print(str_number, end="")

def print_multiplication_table(n):
    for row in range(n+1):
        for column in range(n+2): #  one more step for the line break
            if column == n + 1: #  prints line break
                print()
            elif column == 0 and row == 0: #  prints the top-left empty space
                adjust_spacing_and_print(n, print_number="")
            elif row == 0 : # prints the header in row 0
                row, column = prevent_mult_by_zero(row, column)
                adjust_spacing_and_print(n, print_number = row * column)
            elif column == 0 or column == 1: #  prints the column header and first column 'column in (0, 1)'
                adjust_spacing_and_print(n, print_number=row)
            else: #  prints everything between the column 1 and the print break
                #  row, column = prevent_mult_by_zero(row, column) - not needed anymore
                adjust_spacing_and_print(n, print_number=row * column)

print_multiplication_table(n=20)