class MatrixSizeError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'the matrix should be same or right size:'


class MatrixTypeError(Exception):
    def __str__(self):
        return 'input must be a matrix'


class SubTypeError(Exception):
    def __init__(self, types):
        self.type = types

    def __str__(self):
        return 'it must be a {}'.format(self.type)


class IllegalDataError(Exception):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return 'illegal data entered, should be {}'.format(self.info)
