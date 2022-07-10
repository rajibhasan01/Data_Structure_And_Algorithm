def matrix_multiplication(matrix_1, matrix_2):
    if len(matrix_1) == 0 or len(matrix_2) == 0:
        return 'Matrix should have atleast one row and column';
    matrix_shape_1 = [len(matrix_1), len(matrix_1[0])];
    matrix_shape_2 = [len(matrix_2), len(matrix_2[0])];
    if matrix_shape_1[1] != matrix_shape_2[0]:
        return 'Matrix dimension for multiplication is not matched';
    
    row = [];
    new_matrix = [];
    sum = 0;
    for i in range(len(matrix_1)):
        for j in range(len(matrix_2[0])):
            for k in range(len(matrix_2)):
                sum += matrix_1[i][k] * matrix_2[k][j];
            row.append(sum);
            sum = 0;
        new_matrix.append(row);
        row = [];

    return new_matrix;

    
def print_matrix(matrix):
    print('\n'.join(str('\t'.join([str(column) for column in row])) for row in matrix));

row_1 = list(map(int, input('Enter the 1st row of 1st matrix: ').strip().split()));
row_2 = list(map(int, input('Enter the 2nd row of 1st matrix: ').strip().split()));
matrix_1 = [row_1, row_2];
print('The first matrix is: ');
print_matrix(matrix_1);
row_1 = list(map(int, input('Enter the 1st row of 2nd matrix: ').strip().split()));
row_2 = list(map(int, input('Enter the 2nd row of 2nd matrix: ').strip().split()));
print('The second matrix is: ');
matrix_2 = [row_1, row_2];
print_matrix(matrix_2);

new_matrix = matrix_multiplication(matrix_1,matrix_2);
print('The result matrix is: ');
if type(new_matrix) is list:
    print_matrix(new_matrix);
else:
    print(new_matrix);