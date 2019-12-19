# pymatrix
一个python3的库，自己在闲余时间写着玩的.....（毕竟不是计算机专业学生，能力有限水平一般。
（目前1.0.0版本还未开发完整，只是备份,食用方法：在python根目录的lib下的site-packages中创建一个文件夹，把这几个文件导进去，import 文件夹名 就好）

此库是作者在闲余时间中抽空写出来的一个对matrix服务的库，与numpy中的matrix略有
不同，也是作者对自己的一种锻炼。

> 本库并没有经过严格的校验，如若应用到科学计算中或许会产生偏差

目录：

<a href='#Matrix'>最基本的类：Matrix</a>

<a href='#Spmatrix'>特殊矩阵：Spmatrix</a>

<a href='#operation'>运算器：Operation</a>

<a href='#abnormalConditions'>常见异常处理</a>

版本：V 1.0.0（不稳定）（2019/12/18更新）


<a href='#history'>历史版本及更新</a>

以下是作者的扯淡：

> 当前版本是第一个版本，也是极其相当不稳定的，部分方法逻辑上的不足与异常处理的
一团糟就足以说明问题（当然还有就是这个文档的不足也是其中之一），不过这也是我爱好所致，
因此无法保证稳定更新，但肯定会更新的（因为我确实有可能用上这个，之前觉得创建一个矩阵太麻烦为啥不自己写一个）。
>
> 当然了，我也不认为有超过一只手能数过来的人会真正看到或是使用这个库或是这篇文档，
如果真有人用这个库或者看这篇文档了，那么
>
> 我会在以后版本会补全docstrings和优化文档的！sen mi ma sai~

<a name='Matrix'></a>
## Matrix

作为整个库中最基本的类，其余所有类几乎都是围绕着这个类进行工作的。在使用时要实例化
一个Matrix的对象(在10位数内都能正常打印，还是挺好看的)：

> x = pymatrix.Matrix()

每个对象都会有且只有一个矩阵来代表。若想建立两个矩阵，还需实例化一个新对象，或使用
copy()方法。每个Matrix对象所包含的矩阵遵循了numpy中的矩阵的表示方法，以元组存储。

此类的对象的迭代将是按行从上到下，从左到右依次迭代其中的值。

<a href='#1'>zeros()方法</a>&emsp;&emsp;
<a href='#2'>full()方法</a>&emsp;&emsp;
<a href='#3'>get_matrix()方法</a>&emsp;&emsp;
<a href='#copy'>copy方法(属性)</a>&emsp;&emsp;
<a href='#4'>矩阵之间的加法</a>&emsp;&emsp;

<a href='#sub'>矩阵之间的减法</a>&emsp;&emsp;
<a href='#mul'>矩阵之间的乘法</a>&emsp;&emsp;
<a href='#transposition'>矩阵转置</a>&emsp;&emsp;
<a href='#square'>square()方法</a>

<a name='1'></a>
#### zeros()

该方法可以快速地建造一个n x m的值全为0的矩阵，格式为zeros(n, m):

> x.zeros(3, 4)  # 创建一个3 x 4的矩阵

其返回值为矩阵的数据形式（内部储存方式），而若print(x)则会打印其表现形式（更加
好看）。

<a name='2'></a>
#### full()

该方法算是zeros()的一个超集，所实现功能可以创造一个n x m的所有值为num的矩阵，
格式为full(n, m, num):

> x.full(3, 4, 1)  # 创建一个3 x 4并将每个值赋1

其返回值同zeros()。然而其实在这个方法中创建与赋值是同时发生的。

<a name='3'></a>
#### get_matrix()

该方法创建一个以传入参数所决定的矩阵，传入的参数必须为list类型，例如：
[[1, 2], [3, 4]]，可以创造一个2 x 2的矩阵，为：

&emsp;&emsp;1&emsp;&emsp;2

&emsp;&emsp;3&emsp;&emsp;4

特别注意：若输入的矩阵“列数”不同，例如：[1, [2, 3], 4]，则会按最高“列数”为基准，
其余空位补0处理，上述列表所创建出来的矩阵为：

&emsp;&emsp;1&emsp;&emsp;0

&emsp;&emsp;2&emsp;&emsp;3

&emsp;&emsp;4&emsp;&emsp;0

格式如下:

> x.get_matrix(list)

<a name='copy'></a>
#### copy

使用copy方法可以快速创建一个Matrix对象的拷贝，该方法被修饰为一个属性，直接调用
即可。

> x = pymatrix.Matrix()
>
> y = x.copy  # 创建了一个x的拷贝，x的所有数据被拷贝到y

<a name='4'></a>
#### 矩阵之间的加法(add)

你可以使用正常的加法来对两个尺寸相同的矩阵进行对应元素的加法：

例如，有两个矩阵a, b，他们都是Matrix的一个实例化对象，且都有相同尺寸

> c = a + b

则c为经过加法运算后的矩阵，同样也为Matrix的一个实例化对象。

<a name='sub'></a>
#### 矩阵之间的减法

同矩阵之间的加法一样，用正常的减法对两个尺寸完全相同的矩阵进行对应元素的减法。

> c = a - b  # both a and b are a object of Matrix

<a name='mul'></a>
#### 矩阵之间的乘法

如同加减法一样，直接使用便可(同时可以与一个常数进行运算)。

> c = a * b  

<a name='transposition'></a>
#### 矩阵的转置

> x.T  # x必须是一个有值的矩阵

该方法会直接对x进行转置操作，若想对原矩阵进行保留，则需要在其前面添加复制对象
（相当于是提前对x进行一次拷贝）

> y = x.copy
>
> x.T

转置方法返回的是该对象。

<a name='square'></a>
#### square()方法：

调用该方法可以创建一个n x n的矩阵：

> pymatrix.Matrix.square(n, num_list=None, full=None)

其中n参数必填，num\_list, full两个参数至少填一个：num\_list参数为一个长度不长于
n ^ 2的列表，否则超出部分将被裁剪。若只有num\_list参数，则在创建矩阵时空位用0
补齐，若同时添加num\_list与full参数，则在补空位时使用full所传递的int来补。若
只传入full参数，则创建一个所有元素值均为full的n x n矩阵。

示例：

> m = pymatrix.Matrix()
>
> m.square(3, num_list=[1,2,3,4,5])
>
> print(m)

    m:
        1   2   3
        4   5   0
        0   0   0
        
> m.square(3, num_list=[1,2,3,4,5], full=1)

    m:
        1   2   3
        4   5   1
        1   1   1
        
<a name='Spmatrix'></a>
## Spmatrix

Spmatrix是Matrix的一个子类，其主要作用是创建一些特殊矩阵来使用，正如你所见，
Matrix就像橡皮泥一样你需要自己捏成一个成像，而Spmatrix只需要输入相应的参数，
就能创建一个“预设”的矩阵。

<a href='#sparse'>稀疏矩阵</a>

<a name='sparse'></a>
#### 稀疏矩阵sparse()

你可以创造一个n x n的稀疏矩阵，稀疏矩阵的非零值为1-9的随机数字，而矩阵的稀疏程度
默认为0.1（只有不超过占比0.1的元素值为非零整数），这个参数可以自定义，
但不能低于0.7。

> sparse(n, sparse_num=0.7)

例如：

> n = pymatrix.Spmatrix()
>
> n.sparse(6)

    n:
        0   0   0   0   0   0
        0   0   0   0   0   0
        0   9   0   0   4   0
        5   1   0   0   0   0
        0   0   9   0   0   0
        0   0   0   0   0   1
        

<a name='operation'></a>
## Operation

此类承包了对于Matrix类的所有非加减乘的运算，往往你需要实例化一个此类的对象，然后
就像你用计算器一样把矩阵输入，然后得到你想要的结果，正如字面意思一样，它只是一个
计算器，他并不会对Matrix类的对象进行直接修改。

> op = pymatrix.Operation()

<a href='#mul'>矩阵乘法</a>&emsp;&emsp;
<a href='#trans'>矩阵转置</a>

<a name='mul'></a>
#### 矩阵乘法

使用该方法将实现计算两个矩阵相乘的效果，其返回值为结果矩阵（Matrix对象）。

> x.get_matrix([[1, 2, 3], [4, 5, 6]])
>
> y.get_matrix([[1, 2], [3, 4], [5, 6]])
>
> res = op.mul(x, y)
>
> print(res)

得到的结果如下：

    res:
        22 28
        49 64

<a name='trans'></a>
#### 矩阵转置

> pymatrix.Operation.transposition(Matrix)

该矩阵转置与Matrix类中的转置效果一致，只不过它不会影响到被转置的矩阵，同时
返回一个结果矩阵(Matrix)。

<a name='abnormalConditions'></a>
## 常见异常处理

所有此库的异常：

> MatrixSizeError: 当两个矩阵不满足运算律所要求的大小时，出现此类异常
>
> MatrixTypeError：应当传入一个Matrix对象，且该对象的matrix不为空
>
> SubTypeError: 传入参数时没有成功读取到正确的参数（数据类型不对）
>
> IllegalDataError: 传入参数时没有正确填写参数（数据范围不对）

<a name='history'></a>
## 历史版本及更新内容

#### 2019/12/18 V 1.0.0：

> pymatrix诞生
