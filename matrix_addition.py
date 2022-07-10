def matrix_addition(matrix_1, matrix_2):
    if len(matrix_1) != len(matrix_2):
        return 'Both matrix need to have same dimension';
    else:
        new_matrix = [];
        row = [];
        for i in range(len(matrix_1)):
            if len(matrix_1[i]) != len(matrix_2[i]):
                return 'Both matrix need to have same dimension';
            else:
                for j in range(len(matrix_1[i])):
                    row.append(matrix_1[i][j] + matrix_2[i][j]);
                new_matrix.append(row);
                row = [];
    return new_matrix;

def print_matrix(matrix):
    # print([[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))])
    # print('\n'.join(str( '\t'.join([str(column) for column in row])) for row in matrix));
    print('\n'.join(str('\t'.join([str(column) for column in row]))for row in matrix))

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

new_matrix = matrix_addition(matrix_1,matrix_2);
print('The result matrix is: ');
if type(new_matrix) is list:
    print_matrix(new_matrix);
else:
    print(new_matrix);