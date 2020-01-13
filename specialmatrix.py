from .matrix import Matrix
from .abnormalConditions import *
import random
import copy


class Spmatrix(Matrix):

    """
    该类提供各种特殊矩阵的快速创建
    """

    def __init__(self):
        super().__init__()
        self.matrix = None

    '''
    V1.0.0：创建一个稀疏矩阵，目前来说逻辑层上还有较大问题，尽量避免在当前版本使用该方法（尽管使用起来还好）
    '''

    def sparse(self, dimension, sparse_num=0.9):
        if sparse_num < 0.7:
            raise IllegalDataError('greater than 0.7')
        temp = []
        for i in range(dimension ** 2):
            temp.append(0)
        lens = len(temp)
        n = int(lens * (1 - sparse_num))
        if n == 0:
            n += 1
        for i in range(n):
            index = random.randint(0, lens - 1)
            if temp[index] == 0:
                temp[index] = random.randint(0, 9)
        self.square(dimension, num_list=temp)
        return self.matrix

    def uper_ting(self, n, model=1, full=None):
        matrix_list = []
        if model == 1:
            temp = []
            for i in range(n):
                temp.append(1)
            for i in range(n):
                copy_l = copy.deepcopy(temp)
                for j in range(i):
                    copy_l.pop(0)
                    copy_l.append(0)
                matrix_list.append(copy_l)
            self.get_matrix(matrix_list)
            return self.matrix
        elif model == 2:
            temp = []
            for i in range(n):
                temp.append(1)
            for i in range(n):
                copy_l = copy.deepcopy(temp)
                for j in range(i):
                    copy_l.pop()
                    copy_l.insert(0, 0)
                matrix_list.append(copy_l)
            self.get_matrix(matrix_list)
            return self.matrix
        elif model == 3:
            temp = []
            for i in range(n):
                temp.append(0)
            for i in range(n):
                copy_l = copy.deepcopy(temp)
                for j in range(i + 1):
                    copy_l.pop(0)
                    copy_l.insert(n - 1, 1)
                matrix_list.append(copy_l)
            self.get_matrix(matrix_list)
            return self.matrix

    def three_digonal(self, n, datalist=None):
        if n < 3:
            raise MatrixSizeError('biger than 3')
        if datalist is None:
            datalist = []
            i = 4 + (n - 2) * 3
            for m in range(i):
                datalist.append(1)
        else:
            if len(datalist) < 4 + (n - 2) * 3:
                i = 4 + (n - 2) * 3 - len(datalist)
                for m in range(i):
                    datalist.append(1)
        index_list = []
        _ = 1
        i = 0
        while i < n ** 2:
            if _ <= 2:
                index_list.append(i)
                _ += 1
                i += 1
            else:
                _ = 0
                i += n - 2
        index_int = 0
        for i in range(n ** 2):
            if i != index_list[index_int]:
                datalist.insert(i, 0)
            else:
                index_int += 1
        self.square(n, datalist[:n ** 2])