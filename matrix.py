from .abnormalConditions import *

'''
每一个Matrix对象都会有自己“专属”的matrix，使用self.matrix便可查看他，或直接打印对象本身查看矩阵
在使用时应当创建一个Matrix对象，保证其余模块能顺利工作。
考虑到numpy的矩阵存储格式，以及它们不应该被改变（维度或是列数），因此所有matrix都是一个元组，这或许在将来可能与numpy对接时提供便利
'''


class Matrix:
    def __init__(self):
        self.matrix = None

    '''
    当你希望打印出一个正常点，好看点的矩阵视图时就用它吧。
    V1.0.0：当前版本默认间隔为5字符，后续版本或许会加以更新控制方法。
    '''

    def __repr__(self):
        if self.matrix is None:
            return 'this matrix is empty!'
        print()
        for i in range(len(self.matrix)):
            if isinstance(self.matrix[i], int):
                print('%5s' % self.matrix[i], end='')
                # print(self.matrix[i], end=' ')
            else:
                for n in range(len(self.matrix[i])):
                    print('%5s' % self.matrix[i][n], end='')
                    # print(self.matrix[i][n], end=' ')
            print()
        return ''

    '''
    加减乘部分的代码多数完全相同，以至于我一直在怀疑当时我为什么要这么写
    '''

    def __add__(self, other):
        if isinstance(other, Matrix) is False:
            raise MatrixTypeError()
        if self.__judge_dimension_add(other) is False:
            raise MatrixSizeError()
        temp = Matrix()
        res = []
        if isinstance(self.matrix[0], int):
            for i in range(len(self.matrix)):
                res.append(self.matrix[i] + other.matrix[i])
            temp.matrix = tuple(res)
            return temp
        lens = len(self.matrix[0])
        for i in range(len(self.matrix)):
            temp_list = []
            for n in range(lens):
                temp_list.append(self.matrix[i][n] + other.matrix[i][n])
            res.append(temp_list)
        temp.matrix = tuple(res)
        return temp

    def __sub__(self, other):
        if isinstance(other, Matrix) is False:
            raise MatrixTypeError()
        if self.__judge_dimension_add(other) is False:
            raise MatrixSizeError()
        temp = Matrix()
        res = []
        if isinstance(self.matrix[0], int):
            for i in range(len(self.matrix)):
                res.append(self.matrix[i] - other.matrix[i])
            temp.matrix = tuple(res)
            return temp
        lens = len(self.matrix[0])
        for i in range(len(self.matrix)):
            temp_list = []
            for n in range(lens):
                temp_list.append(self.matrix[i][n] - other.matrix[i][n])
            res.append(temp_list)
        temp.matrix = tuple(res)
        return temp

    def __mul__(self, other):
        if isinstance(other, Matrix) is False and isinstance(other, int) or isinstance(other, float):
            for i in range(len(self.matrix)):
                for n in range(len(self.matrix[0])):
                    self.matrix[i][n] *= other
        else:
            raise SubTypeError('Matrix or int or float')
        if self.__judge_dimension_add(other) is False:
            raise MatrixSizeError()
        temp = Matrix()
        res = []
        if isinstance(self.matrix[0], int):
            for i in range(len(self.matrix)):
                res.append(self.matrix[i] + other.matrix[i])
            temp.matrix = tuple(res)
            return temp
        lens = len(self.matrix[0])
        for i in range(len(self.matrix)):
            temp_list = []
            for n in range(lens):
                temp_list.append(self.matrix[i][n] * other.matrix[i][n])
            res.append(temp_list)
        temp.matrix = tuple(res)
        return temp

    '''
    当你尝试去迭代一个Matrix对象时，这个对象的矩阵会被“展开”，然后按照从上到下，从左至右依次迭代
    '''

    def __iter__(self):
        if isinstance(self.matrix[0], int):
            return iter(self.matrix)
        else:
            temp = []
            for i in range(len(self.matrix)):
                temp.extend(self.matrix[i])
            return iter(temp)

    '''
    这个judge方法本来是想放在assistfuction里的，后因为这个方法的特殊性以及我并不想让其他类（或是其他计算时）调用这个方法，我就
    把它强性塞在了这里
    '''

    def __judge_dimension_add(self, other):
        if len(self.matrix) != len(other.matrix):
            return False
        elif isinstance(self.matrix, int):
            return True
        elif len(self.matrix[0]) != len(other.matrix[0]):
            return False
        else:
            return True

    '''
    zeros和full其实是一个包含的关系，而zeros存在的原因仅仅是因为这是我在测试时编写的第一个方法
    '''

    def zeros(self, dimension_row, dimension_cul):
        res = list()
        for i in range(dimension_row):
            temp = list()
            for n in range(dimension_cul):
                temp.append(0)
            res.append(temp)
        self.matrix = tuple(res)
        return self.matrix

    def full(self, dimension_row, dimension_cul, num):
        res = []
        for i in range(dimension_row):
            temp = []
            for n in range(dimension_cul):
                temp.append(num)
            res.append(temp)
        self.matrix = tuple(res)
        return self.matrix

    '''
    版本V1.0.0：这个方法还存在一些逻辑上的问题，暂时还没有去修改，但就实际测试来看问题不大
    '''

    def square(self, n, num_list=None, full=False):
        if num_list and full is None:
            raise SubTypeError('list or int')
        if isinstance(num_list, list) is False and num_list is not None:
            raise SubTypeError('list')
        if isinstance(full, int) is False and full is not None:
            raise SubTypeError('int')
        if isinstance(n, int) is False:
            raise SubTypeError('int')
        if full and num_list is None:
            self.full(n, n, full)
        else:
            if ~(len(num_list) % n):
                if full:
                    num = full
                else:
                    num = 0
                while True:
                    if len(num_list) == n ** 2:
                        break
                    num_list.append(num)
            res = []
            for i in range(n):
                res.append(num_list[(i * n): (i + 1) * n])
            self.matrix = tuple(res)
        return self.matrix

    '''
    获取矩阵的方法还是使用最原始的方法
    V1.0.0:当前版本无法改变填充的数字，将会在下个版本添加
    '''

    def get_matrix(self, data_stream):
        if isinstance(data_stream, list) is False:
            raise SubTypeError('list')
        temp_dimension = []
        num_data_dimension = 0
        res = []
        for i in range(len(data_stream)):  # 寻找最长列数
            if isinstance(data_stream[i], int):
                num_data_dimension = 1
                temp_dimension.append(num_data_dimension)
            else:
                if num_data_dimension != len(data_stream[i]):
                    num_data_dimension = len(data_stream[i])
                temp_dimension.append(num_data_dimension)
        for i in range(len(data_stream)):
            temp = []
            if temp_dimension[i] < max(temp_dimension):
                data_stream[i] = [data_stream[i]]
                while True:
                    data_stream[i].append(0)
                    if len(data_stream[i]) == max(temp_dimension):
                        break
            for n in range(len(data_stream[i])):
                temp.append(data_stream[i][n])
            res.append(temp)
        self.matrix = tuple(res)
        return self.matrix

    '''
    相比于numpy我采用了在平日里用起来更多的（也是更加粗暴的）写法，尽管这并不符合python编程标准，但实用主义至上。
    你可以用它直接对原数组进行转置操作，同样也可以选择调用Operation中的transposition()来获得其转置的一个复制，而保证原矩阵不变
    '''

    @property
    def T(self):
        if self.matrix is None:
            raise SubTypeError('matrix')
        res = []
        for i in range(len(self.matrix[0])):
            res.append([])
        for i in range(len(self.matrix[0])):
            for n in range(len(self.matrix)):
                res[i].append(self.matrix[n][i])
        self.matrix = res
        return self

    '''
    你可以使用这个copy来创建一份复制，当然deep_copy或是shallow_copy都可，在这里相当于执行了一次deep_copy
    '''

    @property
    def copy(self):
        temp = Matrix()
        temp.matrix = self.matrix
        return temp
