from .matrix import Matrix
from .abnormalConditions import *


class Functions:
    @staticmethod
    def same_dimension(matl, matr):
        if isinstance(matl, Matrix) and isinstance(matr, Matrix) is False:
            raise MatrixTypeError()
        cull = len(matl.matrix[0])
        rowr = len(matr.matrix)
        if rowr == cull:
            return True
        else:
            return False

    @staticmethod
    def get_information(matl, matr):
        rowl = len(matl.matrix)
        if isinstance(matl.matrix[0], int):
            pass
        else:
            cull = len(matl.matrix[0])
        rowr = len(matr.matrix)
        if isinstance(matr.matrix[0], int):
            pass
        else:
            culr = len(matr.matrix[0])
        return rowl, cull, rowr, culr