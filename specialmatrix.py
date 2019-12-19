from .matrix import Matrix
from .abnormalConditions import *
import random


class Spmatrix(Matrix):

    """
    该类提供各种特殊矩阵的快速创建
    """

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
        n = lens * (1 - sparse_num)
        if n == 0:
            n += 1
        for i in range(dimension):
            index = random.randint(0, lens - 1)
            if temp[index] == 0:
                temp[index] = random.randint(0, 9)
        self.matrix = self.square(dimension, num_list=temp)
        return self.matrix


