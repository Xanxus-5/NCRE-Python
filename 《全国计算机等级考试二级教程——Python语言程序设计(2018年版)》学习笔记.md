# 《全国计算机等级考试二级教程——Python语言程序设计(2018年版)》学习笔记

## 一、基本概念

静态语言：编译方式执行（如C语言）；

脚本语言：解释方式执行（如Python语言）；

Python重要特点：

1. 具有通用性；
2. 语法简介；
3. 生态高产；

具体特点：

1. 平台无关；
2. 强制可续；
3. 支持中文；
4. 格式多样；
5. 类库便捷

例子：

```python
#斐波那契数列（F(n) = F(n-2) + F(n-1)）, n >= 2)
a, b = 0, 1
while a < 1000 :
    print(a, end = ',')
a, b = b, a + b
```

```python
#计算圆半径
r = 25
area = 3.1415 * r * r
print(area)
print('{:.2f}'.format(area)) #两位小数
```

```python
#绘制五角星
from turtle import *
color('red', 'red')
begin_fill()
for i in range(5):
    fd(200)
    rt(144)
end_fill()
done()
```

```python
#程序运行计时
import time
limit = 10 * 1000 * 1000
start = time.perf_counter()
while True:
    limit -= 1
    if limit <= 0:
        break
delta = time.perf.counter() - start
print('时间是:{}秒'.format(delta))
```

```python
#绘制七种圆圈
import turtle
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
for i in range(7):
    c = color[i]
    turtle.color(c.c)
    turtle.begin_fill()
    turtle.rt(360/7)
    turtle.circle(50)
    turtle.end_fill()
turtle.done()
```



## 二、Python基本语法元素

缩进：表示程序的逻辑。指每行语句开始前的空白局域，用来表示Python程序之间的包含和层次关系。

变量：可以随时命名、赋值、使用。

命名：首字符不能是数字，中间不能出现空格，长度无限制。

保留字（keyword）：
|    \    |   \   |   \    |   \    |    \     |    \     |
| :-----: | :---: | :----: | :----: | :------: | :------: |
|   and   |  as   | assert | break  |  class   | continue |
|   def   |  del  |  elif  |  else  |  except  |  False   |
| finally |  for  |  from  | global |    if    |  import  |
|   in    |  is   | lambda |  None  | nonlocal |   not    |
|   or    | pass  | return |  True  |   try    |  while   |
|  with   | yield |        |        |          |          |

数字类型：整数、浮点数、复数

字符串：双引号与单引号作用相同

- 切片：[N : M]格式获取字符串的子串（从N到M但不包含M）。

赋值：<变量> = <表达式>

引用：

```python
import <库名称>
<库名称>.<函数名称>()
```

input()：<变量> = input("<提示性文字>")

```python
a = input('请输入：')
# >请输入: X
print(a)
# >X
```

eval()：去掉字符串最外侧的引号。<变量> = eval("<字符串>")

print()：

1. 仅输出：print('<字符串>')；

2. 仅输出一个或多个变量：print('<变量1>', '<变量2>', ... , '<变量n>')；

3. 混合：print(<模板>.format('<变量1>', '<变量2>'...)。例：

   ```python
   a, b = 3, 66
   print('数字{}和数字{}的和是{}'.format(a, b, a+b))
   # >数字3和数字66的和是69
   ```

4. 默认会在最后增加一个换行，或用：print('<内容>', end = '<结尾>')

实例解析——倒背如流：

```python
s = input('请输入一段文本：')
i = len(s) - 1
while i >= 0 :
    print(s[i], end = '')
    i = i - 1
```

```python
s = input('请输入一段文本：')
i = -1
while i >= -1 * len(s):
    print(s[i], end = '')
    i = i -1
```



## 三、基本数据类型

### 1.整数类型

|   种类   | 引导符号 |                         描述                          |
| :------: | :------: | :---------------------------------------------------: |
|  十进制  |    无    |                           \                           |
|  二进制  | 0b 或 0B |          由字符0和1组成，例：0b1010，0B1010           |
|  八进制  | 0o 或 0O |          由字符0到7组成，例：0o1010，0O1010           |
| 十六进制 | 0x 或 0X | 由字符0到9、a 到 f 或 A 到 F 组成，例：0x1010，0X1010 |

*不同进制的整数可以直接运算*

### 2.浮点数类型

必须带有小数部分，小数可以是0。

科学计算法使用字母 e 或 E 作为幂的符号，以10为基数。

不确定尾数：两个浮点数运算，有一定概率在运算结果后增加一些不确定尾数

```python
>>> 0.1 + 0.2
0.30000000004
```

round()函数：对字符串四舍五入。

`round(1.2345, 2) = 1.23 `

### 3.复数类型

基本单位元素 j 或 J ， <a href="https://www.codecogs.com/eqnedit.php?latex=\fn_cs&space;j&space;=&space;\sqrt{-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\fn_cs&space;j&space;=&space;\sqrt{-1}" title="j = \sqrt{-1}" /></a>，叫做“虚数单位”。

复数可以看作是二元有序实数对（a, b），表示 a + bj，a 是实数部分，b 是虚数部分。

*当 b 是1时，‘1’不能省略，即'1j'*

对于复数 z，可以用 z.real 和 z.imag 分别获得它的实部和虚部

```python
>>> (1.23e4 + 5.67e4j).real
12300.0
>>> (1.23e4 + 5.67e4j).imag
56700.0
>>> 1.23e4 + 5.67e4j.imag #先获得5.67e4j的虚部，再与1.23e4进行求和计算
69000.0
```

### 4.运算操作符

| 操作符 |                             描述                             |
| :----: | :----------------------------------------------------------: |
| x + y  |                              和                              |
| x - y  |                              差                              |
| x * y  |                              积                              |
| x / y  |                     商，产生结果为浮点数                     |
| x // y |           整数商，即：不大于 x 与 y 之商的最打整数           |
| x % y  |                     商的余数，称为模运算                     |
|   -x   |                      负值，即 x * (-1)                       |
|   +x   |                            x本身                             |
| x ** y | x 的 y 次幂，即：<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{120}&space;\fn_cs&space;\large&space;x^{y}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{120}&space;\fn_cs&space;\large&space;x^{y}" title="\large x^{y}" /></a> |

基本规则：

- 整数和浮点数混合运算，输出结果是浮点数；

- 整数之间运算，产生结果类型与操作符相关，/ 的结果是浮点数；

- 整数或浮点数与复数运算，输出结果是复数；

  例：

  ```python
  >>> 1010 / 10
  101.0
  >>> 1010.0 // 3
  336.0
  >>> 1010.0 % 3
  2.0
  >>> 10 - (1 + 1j) #等价于(10 - 1) - 1j
  (9 - 1j)
  ```

**所有二元运算操作符都可以与赋值符号（=）相连，形成增强赋值操作符（+=，-=等）。用 'op' 表示运算操作符，增强赋值操作符的用法如下：**

​	x op= y 等价于 x = x op y，op 与 = 之间不用加空格

### 5. 运算函数

|           函数            |                        描述                         |
| :-----------------------: | :-------------------------------------------------: |
|          abs(x)           |                      x的绝对值                      |
|       divmod(x, y)        | (x // y, x % y)，输出为二元组形式（也称为元组类型） |
| pow(x, y) 或 pow(x, y ,z) |           x ** y 或 (x ** y) % z，幂运算            |
|  round(x) 或 round(x, d)  |            对 x 四舍五入，保留 d 位小数             |
|   max(a, b, c, d, ...)    |                       最大值                        |
|   min(a, b, c, d, ...)    |                       最小值                        |

### 6.字符串类型及格式化

单行字符串可以由一对单引号或双引号作为边界表示

多行字符串可以由一对三单引号或三双引号作为边界表示

反斜杠字符（\）表示“转义”，即该字符与后面相邻的一个字符共同组成了新的含义。

- \n：换行；
- \\\：反斜杠
- \t：制表符

*\ 的额外作用：续行*

### 7.format()

<字符串>.format(<逗号分隔的参数>)

*若在字符串中直接输出大括号，使用 {{}} 表示 {}

{<参数符号>:<格式控制标记>}

|       <填充>       |           <对齐>           |      <宽度>      |           <,（英文逗号）>            |                  <.精度>                   | <类型>                                             |
| :----------------: | :------------------------: | :--------------: | :----------------------------------: | :----------------------------------------: | -------------------------------------------------- |
| 用于填充的单个字符 | < 左对齐；> 右对齐；^ 居中 | 槽的设定输出宽度 | 数字的千位分隔符，适用于整数和浮点数 | 浮点数小数部分的精度或字符串的最大输出长度 | 整数类型：b, c, d, o, x, X；浮点数类型：e, E, f, % |

整数类型：

- b：二进制；
- c：对应的Unicode字符；
- d：十进制；
- o：八进制；
- x：小写十六进制；
- X：大写十六进制

浮点类型：

- e：对应的小写字母 e 的指数；
- E：对应的 E 的指数
- f：标准浮点；
- %：百分比 

```python
>>> '{:.2f}'.format(3.14159) #输出小数后2位
'3.14'
>>> '{:X}'.format(1010) #输出十六进制形式
'3F2'
>>> '{:.5}'.format('这是一个很长的字符串') #输出前5位
'这是一个很'
>>> '{:-^10}'.format('PYTHON') #居中并以 - 填充
'--PYTHON--'
```

### 8. 字符串操作符

|     操作符     |                   描述                    |
| :------------: | :---------------------------------------: |
|     x + y      |           连接两个字符串 x 与 y           |
| x * n 或 n * x |             复制 n 次字符串 x             |
|     x in s     | 如果 x 是 s 的字符串，返回True，否则False |

### 9.字符串处理函数

|  函数  |                        描述                         |
| :----: | :-------------------------------------------------: |
| len(x) | 返回 x 的长度，也可以返回其他组合数据类型的元素个数 |
| str(x) |                 返回 x 的字符串形式                 |
| chr(x) |          返回 Unicode 编码 x 对应的单字符           |
| ord(x) |              返回 x 表示的 Unicod 编码              |
| hex(x) |       返回整数 x 对应十六进制的小写形式字符串       |
| oct(x) |        返回整数 x 对应八进制的小写形式字符串        |

### 10.字符串处理方法

|            方法             |                         描述                         |
| :-------------------------: | :--------------------------------------------------: |
|        str.lower(x)         |                  返回 str 全部小写                   |
|        str.upper(x)         |                  返回 str 全部大写                   |
|    str.split(sep = None)    | 返回由 str 根据 sep 被分割构成的列表，默认以空格分割 |
|       str.count(sub)        |                 返回 sub 出现的次数                  |
|    str.replace(old, new)    |             返回 old 被替换为 new 的 str             |
| str.center(width, fillchar) |            字符串居中函数，fillchar 可选             |
|      str.strip(chars)       |          从 str 中去掉其左右 chars 中的字符          |
|       str.join(iter)        |        将 iter 变量的每一个元素后增加一个 str        |

例：

```python
>>> 'Python is an excellent language.'.replace('a', '#')
'Python is #n excellent l#ngu#ge.'
>>> 'Python'.center(20, '=')
'===Python==='
>>> 'Python'.center(2, '=')
'Python' #当 width 小于 str 长度，返回 str
>>> '   ==Python==   '.strip(' =n')
'Pytho'
>>> ','.join('12345')
'1,2,3,4,5'
```

### 11.类型判断和类型间转换

type(x)：对 x 进行类型判断，适用于任何数据类型

```python
n = eval(input('请输入一个数字：'))
if type(n) == type(123):
    print('输入的是整数')
elif type(n) == type(11.3):
    print('输入的是浮点数')
else :
    print('无法判断')
```

int(x)：将 x 转为整数

float(x)：将 x 转为浮点数

str(x)：将 x 转为字符串

### 12.实例解析——凯撒密码

见 CEncode.py  CDecode.py  CCEncode.py  CCDecode.py

*Unicode 范围：*

- *65 - 90 : A - Z*
- *97 - 122 : a - z*
- *0x4e00 - 0x9FA5 : 汉字* 



## 四、程序的控制结构

### 1.程序流程图

*具体图省略*

描述一个计算问题的程序过程有多种方式：IPO、流程图、伪代码和程序代码。

### 2.程序控制结构

三种基本结构：

1. 顺序结构：按照线性顺序依次执行；
2. 分支结构：根据条件判断结果而选择不同向前执行路径；
3. 循环结构：根据条件判断结果向后执行的一种运行方式。

### 3.if

#### A.单分支结构

```python
if <条件> :
    <语句块>
```

<条件>可一个或多个，用 and 与 or 连接多个条件。

#### B.二分支结构

```python
if <条件> :
    <语句块1>
else :
    <语句块2>
```

更简洁的表达方式：适合<语句块1>和<语句块2>都只包含简单表达式的情况。

`<表达式1> if <条件> else <表达式2>`

```python
s = eval(input('请输入一个整数：'))
token = '' if s % 3 == 0 and s % 5 == 0 else "不"
print('这个数字{}能够同时被3和5整除。'.format(token))
```

#### C.多分支结构

```python
if <条件1> :
    <语句1>
elif <条件2> :
    <语句2>
    ...
else :
    <语句N>
```

**按照多分支结构的代码顺序依次评估判断条件，寻找并执行第一个结果为 True 条件对应的语句块，然后跳过整个 if - elif -else 结构。（只有条件为 False 才会进入 elif）

```python
score = eval(input('输入成绩：'))
if score >= 90 :
    grade = 'A'
elif score >= 80 :
    grade = 'B'
elif score >= 70 :
    grade = 'C'
elif score >= 60 :
    grade = 'D'
else :
    grade = 'E'
print('对应的等级是：{}'.format(grade))
```



判断条件及组合：判断条件可以使用任何能够产生 True 或 False 的语句或函数

| 操作符 | 数学符号 |   含义   |
| :----: | :------: | :------: |
|   <    |    <     |   小于   |
|   <=   |  $\leq$  | 小于等于 |
|   >=   |  $\geq$  | 大于等于 |
|   >    |    >     |   大于   |
|   ==   |    =     |   等于   |
|   !=   |  $\neq$  |  不等于  |

Python 中，任何非零的数值、非空的数据类型都等价于 True，反之可以可直接用作判断条件。

```python
>>> 0 == False 
True
>>> '' == True
False
```

not : 否；and : 与；or : 或

### 4.for 遍历循环

```python
for <循环变量> in <遍历结构> :
    <语句>
```

遍历结构可以是字符串、文件、range()函数或组合数据类型等。

字符串：

```python
for <循环变量> in <字符串> :
    <语句块>
```

range()函数：可以制定语句块的循环次数。

```python
for <循环变量> in range(<循环次数>) : 
    <语句块>
```

扩展模式：

```python
for <变量> in <结构> :
    <语句1>
else :
    <语句2>
```

当 for 循环正常结束后，程序会执行 else 语句。

### 5. while 无限循环

```python
while <条件> :
    <语句块>
```

<条件>与 if 一样，结果为 True 或 False。

当判断条件为 True，执行循环体语句，结束后再次判断条件；当 False，循环终止，执行与 while 同级别缩进的后续语句。

else 扩展：

```python
while <条件> :
    <语句1>
else :
    <语句2>
```

### 6.break  continue

break : 用来跳出最内层 for 或 while 循环，脱离后从循环后的代码继续执行。

```python
while True :
    s = input('请输入名字(按Q退出)：')
    if s == 'Q' :
        break
    print('输入的是：', s)
print('程序退出')
```

continue : 结束当前当次循环，跳出循环体下面尚未执行的语句，但不跳出整个循环。

```python
for s in 'PYTHON' :
    if s == 'Y' :
        continue
    print(s, end = '')
```

### 7.try  except

Python 用 try 和 except 进行异常处理。

```python
try :
    <语句1>
except :
    <语句2>
```

语句1是正常执行的程序内容，当执行这个语句发生异常时，则执行 except 后的语句2。

```python
try :
    n = eval(input('请输入一个数字：'))
    print('输入数字的3次方的值为：', n ** 3)
except :
    print('输入错误，请输入一个数字！')
```

### 8.实例解析——猜数字游戏

```python
import random
target = random.randint(1, 1000)
count = 0
while True :
    guess = eval(input('请输入一个猜测的整数（1至1000）：'))
    count = count + 1
    if guess > target :
        print('大了')
    elif guess < target :
        print('小了')
    else :
        print('猜对了')
        break
print('此轮的猜测次数是：', count)
```

```python
import random
target = random.randint(1, 1000)
count = 0
while True :
    try :
    	guess = eval(input('请输入一个猜测的整数（1至1000）：'))
    except :
        print('输入有误，请重试。')
        continue
    count = count + 1
    if guess > target :
        print('大了')
    elif guess < target :
        print('小了')
    else :
        print('猜对了')
        break
print('此轮的猜测次数是：', count)
```

## 五、函数和代码复用

### 1.函数的定义：def

```python
def <函数名>(<参数列表>) :
    <函数体>
    return <返回值列表>
```

```python
def fact(n) :
    s = 1
    for i in range(1, n+1):
        s *= i
    return s
print (fact(100))
```

使用步骤：

1. 函数定义；
2. 函数调用；
3. 函数执行；
4. 函数返回

### 2.函数的参数传递

#### （1）可选参数传递

```python
def <函数名>(<非可选参数>, <可选参数> = <默认值>) :
    <函数体>
    return
```

```python
>>> def multiply(x, y = 10) :
    print(x * y)
>>> mulitply(99)
990
>>> multiply(99, 2) 
198
```

#### （2）参数名称传递

```python
>>> def multiply(x, y = 10) :
    print(x * y)
>>> multiply(x = 99)
990
>>> multiply(y = 2, x = 99)
198
```

**不需要保持参数传递的顺序，参数之间的顺序可以任意调整。**

#### （3）函数的返回值

return 语句用来结束函数并将程序返回到函数被调用的位置继续执行。

### 3.变量的作用域

#### （1）局部变量

在函数内部定义的变量，仅在函数内部有效，当函数退出时变量将不再存在。

```python
>>> def mul(x, y = 10) :
    z = x * y #z是局部变量
    return z
>>> s = mul(99, 2)
>>> print(s)
198
>>> print(z)
error : ...
```

#### （2）全局变量

在函数之外定义的变量，在程序执行全过程有效。全局变量在函数内部使用时，需提前使用 global 声明。

```python
>>> n = 2 #n是全局变量
>>> def mul(x, y = 10) :
    global n
    return x * y * n
>>> s = mul (99, 2)
>>> print(s)
396
```

### 4.代码复用

好处：

- 避免相同功能代码在被调用处重复编写；
- 当更新函数功能时，所有被调用处的功能都被更新。

模块化设计：指通过函数的封装功能将程序划分为主程序、子程序和子程序间关系的表达。

模块化设计基本要求：

- 紧耦合：尽可能合理划分功能块，功能块内部耦合紧密；
- 松耦合：模块间关系尽可能简单，功能块之间耦合度低。

耦合性：指程序结构中各模块之间相互关联的程度，它取决于各模块间接口的复杂程度和调用方式。

- 紧耦合：模块或系统间关系紧密，存在较多或复杂的相互调用。缺点：更新一个模块可能导致其他模块变化，复用较困难。
- 松耦合：一般基于消息或协议实现，系统间交互简单。

### 5.实例解析——软文的诗词风

略

## 六、组合数据类型

### 1.基本概念

能够表示多个数据的类型成为组合数据类型

- 集合类型：元素集合，元素之间无序，相同元素在集合中唯一存在；
- 序列类型：元素向量，元素之间存在先后关系，通过序号访问，元素之间不排他；
- 映射类型：“键——值”数据项的组合，每个元素是一个键值对，表示为(key, value)。

#### （1）集合类型

包含0个或多个数据的无序组合，用大括号表示，集合中的元素可以动态增加或删除。

元素类型只能是不可变数据类型：整数、浮点数、字符串。

**使用集合类型能够过滤掉重复元素**

```python
>>> T = {1010, '1010', 12.3, 1010, 1010}
>>> print(T)
{1010, '1010', 12.3}
```

| 操作符及运算 | 描述                                                 |
| :----------: | :--------------------------------------------------- |
|    S - T     | 返回一个新集合，包括在集合 S 中但不在集合 T 中的元素 |
|    S & T     | 返回一个新集合，包括同时在集合 S 和 T 中的元素       |
|    S ^ T     | 返回一个新集合，包括集合 S 和 T 中非共同元素         |
|    S \| T    | 返回一个新集合，包括集合 S 和 T 中所有元素           |

| 函数或方法  | 描述                                                 |
| :---------: | ---------------------------------------------------- |
|  S.add(x)   | 如果数据项 x 不在集合 S 中，将 x 增加到 S            |
| S.remove(x) | 如果 x 在集合 S 中，移除 x；不在则产生 KeyError 异常 |
|  S.clear()  | 移除 S 中所有数据项                                  |
|   len(S)    | 返回集合 S 元素个数                                  |
|   x in S    | 如果 x 是 S 的元素，返回 True；否则 False            |
| x not in S  | 如果 x 不是 S 的元素，返回 True；否则 False          |

set(x) 函数将其他的组合数据类型变成集合类型，也可以生成空集合变量。

```python
>>> S = set('知之为知之不知为不知')
>>> S
{'不', '为', '之', '知'}
>>> for i in S :
    print(i, end = '')
不为之知
```

#### （2）序列类型

|     操作符     | 描述                                                     |
| :------------: | -------------------------------------------------------- |
|     x in s     | 如果 x 是 s 的元素，返回 True，否则 False                |
|   x not in s   | 如果 x 不是 s 的元素，返回 True，否则 False              |
|     s + t      | 连接 s 和 t                                              |
| s * n 或 n * s | 将序列 s 复制 n 次                                       |
|      s[i]      | 索引，返回 s 的第 i 个元素                               |
|    s[i : j]    | 切片，返回包含 s 第 i 到 j 个元素的子序列（不包含 j）    |
|  s[i : j : k]  | 步骤切片，返回包含 s 第 i 到 j 个元素以 k 为步数的子序列 |
|     len(s)     | s 的元素个数（长度）                                     |
|     min(s)     | s 中的最小元素                                           |
|     max(s)     | s 中的最大元素                                           |
|   s.index(x)   | s 中第一次出现元素 x 的位置                              |
|   s.count(x)   | s 中出现 x 的总次数                                      |

#### （3）映射类型

是序列类型的一种扩展，由用户来定义序号，即键，用其去索引具体的值。

### 2.列表类型

#### （1）定义

列表是包含0个或多个元组的有序序列，属于序列类型。

可进行元素的增加、删除、替换、查找。

没有长度限制，元素类型可以不同，不需要预定长度。

列表类型用中括号，也可以通过 list() 函数将集合或字符串类型转换成列表类型。

```python
>>> list('举个栗子')
['举', '个', '栗', '子']
```

#### （2）索引

沿用序列类型的索引方式，即正向递增序号或反负递减序号，用中括号作为索引操作符，不得超过列表的元素范围，否则 IndexError。

```python
>>> ls = [1010, '1010', [1010, '1010'], 1010]
>>> ls = [3]
1010
>>> ls[-2]
[1010, '1010']
```

可以用遍历循环进行操作

```python
for <循环变量> in <列表变量> :
    <语句块>
```

```python
>>> ls = [1010, '1010', [1010, '1010'], 1010]
>>> for i in ls :
    print(i * 2)
2020
10101010
[1010, '1010', 1010, '1010']
2020
```

#### （3）切片

切片后的结果也是列表类型

```python
<列表或列表变量>[N : M]
或
<列表或列表变量>[N : M : K]
```

**在 [ ] 中表示区间需要用冒号（:），表示枚举使用英文逗号**

**一般要求 N 小于 M，当 N 大于 M 时，返回空列表**

### 3.列表类型的操作

#### （1）操作函数

|  函数   | 描述                       |
| :-----: | -------------------------- |
| len(ls) | 列表 ls 的元素个数（长度） |
| min(ls) | ls 中的最小元素            |
| max(ls) | ls 中的最大元素            |
| list(x) | 将 x 转变成列表类型        |

#### （2）列表的操作方法

`<列表变量>.<方法名称>(<方法参数>)`

|      方法       | 描述                                   |
| :-------------: | -------------------------------------- |
|  ls.append(x)   | 在 ls 最后增加 x                       |
| ls.insert(i, x) | 在 ls 第 i 位置增加 x                  |
|   ls.clear()    | 删除 ls 中所有元素                     |
|    ls.pop(i)    | 将 ls 中第 i 项元素取出并从 ls  中删除 |
|  ls.remove(x)   | 将 ls 中出现的第一个 x 删除            |
|  ls.reverse()   | ls 中元素反转                          |
|    ls.copy()    | 生成新列表，复制 ls                    |

*del*

对列表元素或片段进行删除

```python
>>> ls = [1, 2, 3, 4]
>>> del ls[1]
>>> ls
[1, 3, 4]
```



*ls.copy() 生成的新列表不受旧列表影响*

```python
>>> ls = [1, 2, 3, 4]
>>> lsn = ls.copy()
>>> ls.clear()
>>> print(lsn)
[1, 2, 3, 4]

>>> lt = [1, 2, 3, 4]
>>> ls = lt 
>>> lt.clear()
>>> print(ls)
[]
```

### 4.字典的索引

`<值> = <字典变量>[<键>]`

```python
>>> d = {'20101':'小明', '20102':'小红', '20103':'小白'}
>>> print(d['20102'])
小红
```

大括号 { } 可以创建字典，索引和赋值可以增加元素。

```python
>>> t = {}
>>> t['20104':'小新']
>>> print(t)
{'20104':'小新'}
```

字典是存储可变数量键值对的数据结构，键和值可以是任意数据类型。

### 5.字典的操作

#### （1）操作函数

|  函数  | 描述                      |
| :----: | ------------------------- |
| len(d) | 字典 d 的元素个数（长度） |
| min(d) | 字典 d 中键的最小值       |
| max(d) | 字典 d 中键的最大值       |
| dict() | 生成一个空字典            |

#### （2）操作方法

`<字典变量>.<方法名称>(<方法参数>)`

|        方法         | 描述                                                         |
| :-----------------: | ------------------------------------------------------------ |
|      d.keys()       | 返回所有的键信息                                             |
|     d.values()      | 返回所有的值信息                                             |
|      d.items()      | 返回所有的键值对                                             |
| d.get(key, default) | 键存在则返回相应值，否则返回默认值                           |
| d.pop(key, default) | 键存在则返回并删除值对，否则返回默认值                       |
|     d.popitem()     | 随机从字典中去取出一个键值对，以元组(key, value)形式返回，并从字典中删除 |
|      d.clear()      | 删除所有的键值对                                             |

```python
>>> d = {'1':'A', '2':'B', '3':'C'}
>>>d.items()
dict_items([('1','A'), ('2', 'B'), ('3', 'C')])

>>> d.get('4')

>>> d.get('4', '不存在')
'不存在'

>>> del d['1']
>>> print(d)
{'2':'B', '3':'C'}

>>> '1' in d
True

>>> '4' in d
False

>>> for k in d:
    print('The key and value are {} and {}'.format(k, d.get(k)))
The key and value are 1 and A
The key and value are 2 and B
The key and value are 3 and C
```

### 6.实例解析——文本词频统计

```python
#CalHamlet.py
def getText():
    txt = open('hamlet.txt', 'r').read()
    txt = txt.lower()
    for ch in '!"#$&%()*+,-./:;<=>?@[\\]^_{|}~':
        txt = txt.replace(ch, '')
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}

for word in words:
    counts[word] = count.get(word, 0) + 1

items = list(counts.items())
items.sort(key = lambda x:x[1], reverse = True)

for i in range(10):
    word, count = items[i]
    print('{0:<10}{1:>5}'.format(word, count))
```

## 七、文件和数据格式化

### 1.文件的使用

两种类型：文本文件、二进制文件

存储在辅助存储器上的一组数据序列。

#### （1）文件的类型

文本文件：由单一特定编码的字符组成；

二进制文件：直接由比特0和比特1组成，没有统一的字符编码，文件内部数据的组织格式与文件用途有关。

#### （2）打开和关闭

文件的存储状态是默认状态，打开后变成占用状态，关闭后再次回到存储状态。

open() 函数：打开一个文件，并返回一个操作这个文件的变量

`<变量名> = open(<文件路径及文件名>, <打开模式>)

| 打开模式 | 含义                                                     |
| :------: | -------------------------------------------------------- |
|   'r'    | 只读，如果文件不存在返回异常 FileNotFoundError，默认值   |
|   'w'    | 覆盖写，文件不存在则创建，存在则完全覆盖原文件           |
|   'x'    | 创建写，文件不存在则创建，存在则返回异常 FileExistsError |
|   'a'    | 追加写，文件不存在则创建，存在则在源文件最后追加内容     |
|   'b'    | 二进制文件模式                                           |
|   't'    | 文本文件模式，默认值                                     |
|   '+'    | 与 r w x d 一同使用，在原功能上增加读写功能              |

<变量名>.close() 关闭文件，释放文件的使用授权。

**表示路径时，使用 \\\ 或 / 代替  \\ **

#### （3）文件的读写

|        读取方法         | 含义                                                         |
| :---------------------: | ------------------------------------------------------------ |
|    f.read(size = -1)    | 从文件中读入整个文件内容。参数可选，读入前size长度的字符串或字节流 |
|  f.readline(size = -1)  | 从文件中读入一行内容。参数可选，读入该行前size长度的字符串或字节流 |
| f.readlines(hint  = -1) | 从文件中读入所有行，以每行为元素形成一个列表。参数可选，读入 hint 行 |
|     f.seek(offset)      | 改变当前文件操作指针的位置。offset : 0为文件开头；2为文件结尾 |

|    写入方法     | 含义                                 |
| :-------------: | ------------------------------------ |
|   f.write(s)    | 向文件写入一个字符串或字节流         |
| f.writelines(s) | 将一个元素为字符串的列表整体写入文件 |

**f.write(s) 写入字符串 s，每次写入后，将会记录一个写入指针**

```python
f = open('d:/c.txt', 'w')
f.write('123\n')
f.write('456\n')
f.close()
```

**要显式地使用 \n 进行分行**

```python
ls = ['123', '456', '789']
f = open('d:/d.txt', 'w')
f.writelinese(ls)
f.close()
```

### 2.数据组织的维度

#### （1）一维数据

由对等关系的有序或无序数据构成，采用线性方式组织。

任何表现为序列或集合的内容都可以看作是一维数据。

#### （2）二维数据

也称表格数据，由关联系数构成，采用二维表格方式组成。

#### （3）高维数据

由键值对类型的数据组成，采用对象方式组织，可以多层嵌套。

### 3.一维数据处理

#### （1）表示

由于是线性结构，因此主要采用列表形式表示。

#### （2）存储

4种方法：

1. 采用空格分隔元素：A 12 数据
2. 采用逗号分隔元素：A, 12, 数据
3. 采用续行分隔元素：A
                                     12
                                     数据
4. 其他特殊符号分隔，如分号：A; 12; 数据

**逗号分隔的存储格式为 CSV 格式（Comma_Separated Values），它是一种通用的、相对简单的文件格式**

```python
ls = ['北京', '上海', '广州']
f = open('city.csv', 'w')
f.write(','.join(ls) + '\n')
f.close()
```

#### （3）处理

首先需要从 CSV 文件读入一维数据，并将其表示为列表对象。

**默认包含了一个换行符 \n。采用 .strip() 去掉**

```python
f = open('city.csv', 'r')
ls = f.read().strip('\n').split(',')
f.close()
print(ls)
```

### 4.二维数据的处理

#### （1）表示

二维数据可以采用二维列表来表示。

*二维数据一般采用相同的数据类型存储*

#### （2）存储

用 csv 文件存储

```python
# ls 代表二维列表
f = open('cpi.csv', 'w')
for row in ls:
    f.wrtie(','.join(row) + '\n')
f.close()
```

#### （3）处理

```python
f = open('cpi.csv', 'r')
ls = []
for line in f :
    ls.append(line.strip('\n').split(','))
f.close()
print(ls)
```

**与一维列表不同，二维列表一般需要借助循环遍历实现对每个数据的处理**

```python
for row in ls :
    for item in row:
对第 row 行第 item 列元素进行处理
```

对二维数据进行格式化输出，打印成表格形状：

```python
#此出省去从 CSV 获得的 ls
for row in ls:
    line = ''
    for item in row:
        line += '{:10}\t'.format(item) #\t 横行制表符
    print(line)
```

### 5.实例解析——国家财政数据趋势演算

略

#### （1）zip() 函数

用来获取两个组合数据类，并将它的元素交织返回

```python
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> print(zip(x, y))
[(1, 4), (2, 5), (3, 6)]
```

#### （2）线性回归代码

$\hat y$ = b$\hat x$ + a

```python
def means(data):
    return sum(data) / len(data)

def linearRegression(xlist, ylist):
    xmeans, ymeans = means(xlist), means(ylist)
    bNumerator = -len(xlist) * xmeans * ymeans
    bDenominator = -len(xlist) * xmeans ** 2
    for x, y in zip(xlist, ylist):
        bNumerator += x * y
        bDenominator += x ** 2
    b = bNumerator / bDenominator
    a = ymeas - b * xmeans
    return a, b
```

## 八、Python 计算生态

### 1.计算思维

程序设计是实践计算思维的重要手段

本质：抽象和自动化

*算法（Algorithm）：解决问题的清晰指令*

### 2.程序设计方法论

#### （1）自顶向下设计：最重要是顶层设计

是一种开发复杂程序最具价值的设计理念和工具，设计过程自然且简单，自顶向下设计通过封装实现抽象，利用了模块化设计的思想。

见 MatchAnalysis.py

#### （2）自底向上执行

import 开展单元测试：

`import <源文件名称>`

### 3.计算生态

https://pypi.python.org/pypi

函数库并非都采用 Python 编写，很多采用 C 等语言编写的库可以通过简单的接口封装供 Python 程序调用。“胶水语言”。

Python 第三方程序包：

- 库 library；
- 模块 module；
- 类 class；
- 程序包 package

### 4.实例解析——Web 页面元素提取

见 getNGurl.py

## 九、Python 标准库概览

### 1.turtle库概述

turtle 是 Python 重要的标准库之一，它能够进行基本的图形绘制。概念诞生于1969年，成功应用于 LOGO 编程语言。

基本框架：一个龟在坐标系中爬行，其爬行轨迹形成了绘制图形。

刚开始时，位于正中央，前进方向为水平右方。

三种引用方式：

1. ```python
   import turtle
   turtle.<函数名>()
   ```

2. ```python
   from turtle import *
   <函数名>()
   ```

3. ```python
   import turtle as t(也可以是其他别名)
   t.<函数名>()
   ```

### 2.turtle库与基本绘图

#### （1）窗体函数：turtle.setup()

`turtle.setup(width, height, startx, starty)

作用：设置主窗体的大小和位置。

width：窗口宽度。整数：像素值；小数：窗口宽度与屏幕的比例。

height：窗口高度。

startx：窗口左侧与屏幕左侧的像素距离。None：水平中央。

starty：窗口顶部与屏幕顶部的像素距离。None：垂直中央。

#### （2）画笔状态函数

|          函数           | 作用                                        |
| :---------------------: | ------------------------------------------- |
|        pendown()        | 放下画笔                                    |
|         penup()         | 提起画笔，与 pendown() 配对使用             |
|        pensize()        | 设置画笔线条的粗细                          |
|       pencolor()        | 设置颜色                                    |
|      begin_fill()       | 填充前，调用                                |
|       end_fill()        | 填充结束                                    |
|        filling()        | 返回填充的状态，True 为填充，False 为未填充 |
|         clear()         | 清空当前窗口，但不改变当前画笔位置          |
|         reset()         | 清空并重置                                  |
|      screensize()       | 设置画布的长与宽                            |
|      showturtle()       | 显示画笔的 turtle 形状                      |
|      hideturtle()       | 隐藏画笔的 turtle 形状                      |
|       isvisible()       | 如果 turtle 可见，则返回 True               |
| write(str, font = None) | 输出 font 字体的 str                        |

#### （3）画笔运动函数

|       函数        | 作用                               |
| :---------------: | ---------------------------------- |
|     forward()     | 前进指定距离                       |
|    backward()     | 后退指定距离                       |
|   right(angle)    | 向右旋转 angle 角度                |
|    left(angle)    | 向左旋转 angle 角度                |
|    goto(x, y)     | 移动到（x，y）处                   |
|      setx()       | 将当前 x 轴移动到指定位置          |
|      sety()       | 将当前 y 轴移动到指定位置          |
| setheading(angle) | 设置当前朝向为 angle 角度          |
|      home()       | 设置当前位置为原点，朝向东         |
| circle(radius, e) | 绘制一个半径 r 和角度 e 的园或弧形 |
|   dot(r, color)   | 绘制一个半径 r 和颜色的圆点        |
|      undo()       | 撤销画笔最后一个动作               |
|      speed()      | 设置绘制速度，参数为0~10           |

### 3.random 库概述

用于产生各种分布的伪随机数序列。采用梅森旋转算法（Mersenne twiste）生成伪随机数序列，可用于除随机性要求更高的加密算法外大多数工程应用。

最基本函数：random.random()，它生成 [0.0, 1.0] 之间的小数

### 4.random 库与随机数应用

|             函数              | 作用                                                |
| :---------------------------: | --------------------------------------------------- |
|        seed(a = None)         | 初始化随机数种子，默认值为当前系统时间              |
|           random()            | 生成 [0.0, 1.0] 之间的小数                          |
|         randint(a, b)         | 生成一个 [a, b] 之间的整数                          |
|        getrandbits(k)         | 生成一个 k 比特长度的随机整数                       |
| randrange(start, stop [step]) | 生成一个 [start, stop) 之间以 step 为步数的随机整数 |
|         uniform(a, b)         | 生成一个 [a, b] 之间的随机小数                      |
|          choice(seq)          | 从序列类型（如列表）中随机返回一个元素              |
|         shuffle(seq)          | 将序列类型中元素随机排列，返回序列                  |
|        sample(pop, k)         | 从 pop 类型中随机选取 k 个元素，以列表类型返回      |

### 5.time 库概述

Python 提供的处理时间标准库。提供系统级精确计时器的计时功能，可以用来分析程序性能，也可以让程序暂停运行时间。

3方面主要功能：

1. 时间处理：time.time()、time.gmtime()、time.localtime()、time.ctime()
2. 时间格式化：time.mktime()、time.strftime()、time.strptime()
3. 计时：time.sleep()、time.monotonic()、time.perf_counter() 

|       函数       | 作用                                                         |
| :--------------: | ------------------------------------------------------------ |
|   time.time()    | 获取当前的时间戳                                             |
|  time.gmtime()   | 获取当前时间戳对应的 struct_time 对象                        |
| time.localtime() | 获取当前时间戳对应的本地时间的 struct_time 对象              |
|   time.ctime()   | 获取当前时间戳对应的易读字符串表示，内部会调用 time.localtime() |
|  time.mktime()   | 将 srtuct_time 转换为时间戳                                  |
| time.strftime()  | 时间格式化最有效的方法，几乎可以以任何通用格式输出时间       |
| time.strptime()  | 提取字符串中的时间来生成 struct_time                         |

struct_time 元素

| 下标 |   属性   | 值                           |
| :--: | :------: | ---------------------------- |
|  0   | tm_year  | 年份，整数                   |
|  1   |  tm_mon  | 月份 [1, 12]                 |
|  2   | tm_mday  | 日期 [1, 31]                 |
|  3   | tm_hour  | 小时 [0, 23]                 |
|  4   |  tm_min  | 分钟 [0, 59]                 |
|  5   |  tm_sec  | 秒 [0, 61]                   |
|  6   | tm_wday  | 星期 [0, 6] （0 表示星期一） |
|  7   | tm_yday  | 该年第几天 [1, 366]          |
|  8   | tm_isdst | 是否夏令时，0否，1是，-1未知 |

time.strftime():

`time.strftime('<参数>', time)`

| 参数符号 |  日期/时间  |       值范围       |
| :------: | :---------: | :----------------: |
|    %Y    |    年份     |    0001 - 9999     |
|    %m    |    月份     |      01 - 12       |
|    %B    |    月名     | January - December |
|    %b    |  月名缩写   |    Jan. - Dec.     |
|    %d    |    日期     |      01 - 31       |
|    %A    |    星期     |  Monday - Sunday   |
|    %a    |  星期缩写   |    Mon. - Sun.     |
|    %H    | 小时（24h） |      00 - 23       |
|    %I    |     12h     |      01 - 12       |
|    %p    |   上/下午   |       AM, PM       |
|    %M    |    分钟     |       00 -59       |
|    %S    |     秒      |      00 - 59       |

### 6.time 库与程序计时

三要素：

- 程序开始/结束时间
- 程序运行时间
- 程序各核心模块运行时间

time.sleep(t)：推迟 t 秒执行

time.perf_counter()：计时器，每次调用记录当前执行时间

见 Counter.py

### 7.实例解析——雪景艺术绘图

见 SnowView.py

## 十、Python 第三方库概览

### 1.获取和安装

#### （1）pip 工具

是 Python 官方提供并维护的在线第三方库安装工具。

`pip install <库名>`

#### （2）自定义安装

一般适用于在 pip 中尚无登记或安装失败的第三方库

#### （3）文件安装

略

#### （4）pip 工具使用

```powershell
pip uninstall <库名>
pip list #列出当前系统以安装的第三方库
pip show <库名> #列出某个以安装库的详细信息
pip download <库名> #下载第三方库的安装包，但不安装
pip search <关键字> #联网搜索库名或摘要中的关键字
```

### 2.PyInstaller 概述

将 Python 源文件（.py）打包，变成直接可运行的可执行文件。

### 3.PyInstaller 与程序打包

`PyInstaller <程序文件名>`

生成 dist 和 build 文件夹。build 是存储临时文件的目录。

注意问题：

- 文件路径中不能出现空格和英文句号（.）
- 源文件必须是 UTF-8 编码

|    常用参数    | 描述                                 |
| :------------: | ------------------------------------ |
|   -h, --help   | 查看帮助                             |
|    --clean     | 清理打包过程中的临时文件             |
|  -D, --onedir  | 默认值，生成 dist 目录               |
| -F, --onefile  | 在 dist 文件夹中只生成独立的打包文件 |
| -i, <图标.ico> | 指定打包程序使用的图标文件           |

### 4.jieba 库概述

重要的第三方中文分词函数库

原理：中文词库 $\rightarrow$ 内容X分词词库 $\rightarrow$ 图结构和动态规划 $\rightarrow$ 最大概率的词组

三模式：

1. 精确模式：最精确地切开，适合文本分析；
2. 全模式：把句子中所有可以成词的词语都扫描出来，但是不能解歧义；
3. 搜索引擎模式：在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词

### 5.jieba 库使用

|          函数           | 作用               |
| :---------------------: | ------------------ |
|         lcut(s)         | 精确模式，返回列表 |
| lcut(s, cut_all = True) | 全模式             |
|   lcut_for_search(s)    | 搜索模式           |
|       add_word(w)       | 向词典中添加新词 w |

### 6.wordcloud 库概述

“关键词云层”、“关键词渲染”

### 7.wordcloud 库与可视化词云

|       参数       | 功能                                              |
| :--------------: | ------------------------------------------------- |
|    font_path     | 指定字体文件的完整路径，默认 None                 |
|      width       | 生成图片宽度，默认400像素                         |
|      height      | 生成图片高度，默认200像素                         |
|       mask       | 词云形状，默认 None，方形图                       |
|  min_font_size   | 词云中最小的字体字号，默认4号                     |
|    font_step     | 字号步进间隔，默认1                               |
|    stopwords     | 被排除词列表，排除词不再词云中显示                |
| background_color | 背景颜色，默认黑色                                |
|    max_words     | 词云中最大词数，默认200                           |
|  max_font_size   | 词云中最大的字体字号，默认 None，根据高度自动调整 |

|       方法       | 功能     |
| :--------------: | -------- |
|  generate(text)  | 生成词云 |
| tofile(filename) | 保存     |

图像词云：

```python
from scipy.misc import imread
mask = imread('***.png')
```

### 8.实例解析——《红楼梦》人物出场词云

见 CalStoryOfStone.py 与 CalStoryOfStone2.py

## 十一、Python 第三方库纵览

### 1.爬虫方向

自动进行 HTTP 访问并捕获 HTML 页面的程序。

#### （1）requests

简洁且简单

|   函数    | 功能                     |
| :-------: | ------------------------ |
| request() | 构建一个请求             |
|   get()   | 获取 HTML 网页的主要方法 |
|  head()   | 获取 HTML 网页头信息     |
|  post()   | 提交 POST 请求           |
|  patch()  | 提交局部修改请求         |
| delete()  | 提交删除请求             |
|   put()   | 提交 PUT 请求            |

#### （2）scrapy 

快速的、高层次的 web 获取框架

### 2.数据分析方向

#### （1）numpy

开源数值计算扩展第三方库，用于处理数据类型相同的多维数据（ndarray），“数组”。

#### （2）scipy

在 numpy 库的基础沈阳增加了众多的科学、数学以及工程计算中常用的库函数。包括统计、优化、整合、线性代数、傅里叶变换、信号分析、图像处理、常微分方程求解等众多模块。

#### （3）pandas

基于 numpy 扩展。为解决数据分析任务。

### 3.文本处理方向

#### （1）pdfminer

一个可以从 PDF 文档中提取各类信息的第三方库。

#### （2）openpyxl

一个处理 Excel 文档的 Python 第三方库。

#### （3）python_docx

一个处理 Word 文档的第三方库。

#### （4）beautifulsoup4

用于解析和处理 HTML 和 XML。

### 4.数据可视化方向

指根据数据特点将其展示为易于理解的图形的过程。

#### （1）matplotlib

主要进行二维图标数据展示，广泛用于科学计算的数据可视化。

#### （2）TVTK

专业可编程的三维可视化工具。

#### （3）mayavi

基于 VTK 开发，完全用 Python 编写。

### 5.用户图形界面方向

#### （1）PyQt5

最成熟的商业级 GUI 第三方库。

#### （2）wxPython

#### （3）PyGTK

### 6.机器学习方向

#### （1）scikit-learn

一个简单且高效的数据挖掘和数据分析工具。

#### （2）TensorFlow

Google 基于 DistBelief 进行研发的第二代人工智能学习系统。

#### （3）Theano

为执行深度学习中大规模神经网络算法而设计，擅长处理多维数组。

### 7.Web 开发方向

#### （1）Django

最流行的开源 Web 应用框架。

#### （2）Pyramid

相对小巧、快速、灵活的开源 Python Web 框架。

#### （3）Flask

轻量级 Web 应用框架。

### 8.游戏开发方向

#### （1）Pygame

在 SDL 库基础上进行封装的、面向游戏开发入门的 Python 第三方库。

#### （2）Panda3D

一个开源、跨平台的3D渲染和游戏开发库。

#### （3）cocos2d

一个构建2D游戏和图形界面交互式应用的框架。

### 9.更多

#### （1）PIL

在图像处理方面的重要第三方库。

- 图像归档：
  1. 对图像进行批处理；
  2. 生成图像预览；
  3. 图像格式转换等。
- 图像处理：
  1. 基本处理；
  2. 像素处理；
  3. 颜色处理等。

#### （2）SymPY

一个支持符号计算的第三方库。一个全功能的计算机代数系统。

#### （3）NLTK

自然语言处理第三方库。

语料处理、文本统计、内容理解、情感分析等多种应用。

#### （4）WeRoBot

一个微信公众号开发框架，也成为微信机器人框架。

#### （5）MyQR

一个能够产生基本二维码、艺术二维码和动态二维码的第三方库。

## 附录

### 常用 Unicode 编码表

|      名称      |       范围       |
| :------------: | :--------------: |
|    基础汉字    | [0x4e00, 0x9fa5] |
|      数字      | [0x0030, 0x0039] |
|    小写字母    | [0x0061, 0x007a] |
|    大写字母    | [0x0041, 0x005a] |
|      箭头      | [0x2190, 0x21ff] |
|   数字运算符   | [0x2200, 0x22ff] |
| 封闭式字母数字 | [0x2460, 0x24ff] |
|     制表符     | [0x2500, 0x257f] |
|    方块元素    | [0x2580, 0x259f] |
|    几何图形    | [0x25A0, 0x25ff] |
|  一般标点符号  | [0x2000, 0x206f] |
|      韩文      | [0xAC00, 0xD7A3] |
|      货币      | [0x20a0, 0x20cf] |
|      泰文      | [0x0e00, 0x07f]  |
|   中日韩符号   | [0x3000, 0x303f] |
| 中日韩括号数字 | [0x3200, 0x32ff] |

### 转义字符

| 符号 | 作用               |
| :--: | ------------------ |
|  \   | （在行尾时）续行符 |
|  \\  | 反斜杠符号         |
|  \'  | 单引号             |
|  \"  | 双引号             |
|  \a  | 响铃               |
|  \b  | 退格（Backspace）  |
|  \e  | 转义               |
| \000 | 空                 |
|  \n  | 换行               |
|  \v  | 纵向制表符         |
|  \t  | 横向制表符         |
|  \r  | 回车               |
|  \f  | 换页               |

