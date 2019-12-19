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
        pass


