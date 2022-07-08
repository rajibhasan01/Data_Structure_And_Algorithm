def print_matrix():
    matrix_1 = list(map(str, input('Enter the first matrix: ').strip().split()));
    matrix_2 = list(map(str, input('Enter the 2nd matrix: ').strip().split()));
    matrix_1 = " ".join(matrix_1);
    matrix_2 = " ".join(matrix_2);
    print(matrix_1);
    print(matrix_2);

print_matrix()