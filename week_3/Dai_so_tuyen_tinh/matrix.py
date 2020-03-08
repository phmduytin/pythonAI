def matrix_multi(matrix1, matrix2):
    matrix1_nrow = len(matrix1)
    matrix1_mcol = len(matrix1[0])

    matrix2_mrow = len(matrix2)
    matrix2_kcol = len(matrix2[0])

    matrix_res = [[0] * matrix2_kcol for i in range(matrix1_nrow)]

    for i in range(matrix1_nrow):
        for j in range(matrix2_kcol):
            for k in range(matrix1_mcol):
                matrix_res[i][j] += matrix1[i][k] * matrix2[k][j]

    return matrix_res


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
matrix2 = [
    [1, 1, 2, 1],
    [1, 2, 1, 1],
    [1, 1, 1, 2]]

# Check: matrix1_colum == matrix_row:
matrix1_nrow = len(matrix1)
matrix1_mcol = len(matrix1[0])

matrix2_mrow = len(matrix2)
matrix2_kcol = len(matrix2[0])

if matrix1_mcol == matrix2_mrow:
    res = matrix_multi(matrix1, matrix2)
elif matrix2_kcol == matrix1_nrow:
    res = matrix_multi(matrix2, matrix1)

print(res)

for row in res:
    print('     '.join([str(elem) for elem in row]))
