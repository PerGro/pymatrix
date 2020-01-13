from .matrix import Matrix
from .abnormalConditions import *
from .assistfuction import Functions


class Operation(Functions):
    def __init__(self):
        pass

    @staticmethod
    def mul(matl, matr):
        if isinstance(matl, Matrix) and isinstance(matr, Matrix) is False:
            raise SubTypeError('matrix')
        if Functions.same_dimension(matl, matr) is False:
            raise MatrixSizeError()
        matrix = Matrix()
        matrix.matrix = []
        rowl, cull, rowr, culr = Functions.get_information(matl, matr)
        for i in range(rowl):
            matrix.matrix.append([])
        for j in range(rowl):
            for i in range(culr):
                temp = []
                for n in range(cull):
                    temp.append(matl.matrix[j][n] * matr.matrix[n][i])
                matrix.matrix[j].append(sum(temp))
        return matrix

    @staticmethod
    def transposition(mat):
        if mat.matrix is None:
            raise SubTypeError('matrix')
        res = []
        for i in range(len(mat.matrix[0])):
            res.append([])
        for i in range(len(mat.matrix[0])):
            for n in range(len(mat.matrix)):
                res[i].append(mat.matrix[n][i])
        matrix = Matrix()
        matrix.matrix = res
        return matrix

    @staticmethod
    def determinant(mat):
        if len(mat.matrix) != len(mat.matrix[0]):
            raise MatrixSizeError()
        res = 0
        res_list = []
        num_list = list(range(len(mat.matrix)))
        Functions.perm(num_list, res_list, 0)
        for i in range(len(res_list)):
            temp_list = res_list[i]
            mi = 1 if Functions.inverse_number(temp_list) else -1
            temp = mi
            row = 0
            for j in range(len(temp_list)):
                col = temp_list[j]
                temp *= mat.matrix[row][col]
                row += 1
            res += temp
        return res

    @staticmethod
    def cut(mat, cut_row, cut_col):
        temp = mat.copy
        if isinstance(cut_row, list):
            begin_r = cut_row[0]
            end_r = cut_row[1]
        else:
            begin_r = cut_row
            end_r = len(temp)
        if isinstance(cut_col, list):
            begin_c = cut_col[0]
            end_c = cut_col[1]
        else:
            begin_c = cut_col
            end_c = len(temp.matrix[0])
        temp.matrix = temp.matrix[begin_r:end_r]
        for i in range(len(temp)):
            temp.matrix[i][:] = temp.matrix[i][begin_c:end_c]
        return temp

    @staticmethod
    def adjoint(mat):
        if len(mat.matrix) != len(mat.matrix[0]):
            raise MatrixSizeError('should be same size')
        res = Matrix()
        res_list = []
        for i in range(len(mat)):
            for j in range(len(mat)):
                mi = 1 if (i + j) % 2 == 0 else -1
                res_list.append((mi * Operation.determinant(Matrix(Functions.find_cofactor(mat, i, j)))))
        res.square(len(mat), res_list)
        return res

    @staticmethod
    def inverse(mat, acc=2):
        det = Operation.determinant(mat)
        if det == 0:
            print('this matrix do not have its inverse matrix')
            return
        temp = Operation.transposition(Operation.adjoint(mat))
        return Matrix.square(Matrix(), len(mat), Functions.split_matrix_thorough(temp * round(1/det, acc)))


