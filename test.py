from pymatrix import Matrix
from pymatrix.magicmatrix import MagicMatrix
from pandas import read_csv, read_excel
from pymatrix.xlsx import xlsx
import pandas
from tonumpy.tonp import tonumpy
from topandas.topd import topandas
from pymatrix import Operation
from pymatrix.specialmatrix import Spmatrix
from pymatrix.game import Game

# g = Game('easy')
s = Spmatrix()
s.sparse(5)
print(s)
