'''
#0001
print ('Давай "Знакомиться"?')
name = input('Как тебя зовут? \n')
print('Привет,', name, '! \n')
#0002
print(dir())
# dir - список доступных переменных в программе
# !! не начинать и не заканчивать свои переменные со знака подчеркивания
import builtins #подключение новых модулей и библиотек
print(dir(builtins)) #выведет список ключевых слов из builtins
'''
'''
#0003
name = 'Vladimir'
print ('Переменные ссылаются на данные.')
print ('Тип переменной name:', type(name))
del name
'''
'''
#0004
print(2+3)
print(2-3)
print(2*3)
print(2/3)
print(2//3)
print(2%3)
print(2**3) #степень
print('2aaaaaaaa a' * 3) #вывести любое значение несколько раз
a = '4**5 + 2'
print(eval(a)) #eval парсит строку и выполняет её 
'''
'''
#0005
print(bin(25))
print(oct(25))
print(hex(25))
print(bin(5))
print(bin(~5))
'''
'''
#0006
print(' ' + bin(250))
print(bin(~250))
print('x + (-x)=0')
print('x + (~x) = 1111...111 + 1')
print('x + (~x) + 1 = 1111...111 + 1')
print('x + (~x) + 1 = 0')
print('~x = -x - 1')
print('~x = ~x + 1')
print('x = -(~x = 1)')
print('x = -(~x + 1)')
print(bin(~(-250)))
print('~a == -a -1')


#0007
print(bin(50) + '\n' + bin(30))
print(' ' + bin(50&30))
print(bin(50&30))
print(bin(50|30))
print(bin(50^30))
print(bin(50<<3))
print(bin(50>>3))


#0008
print(True or False)
print(True and False)
print(not False)
print(5 > 3)
print(5 < 3)
print(5 >= 3)
print(5 <= 3)
print(5 == 3)
print(5 != 3)

#0009
a = 3
b = 5
c = 5
print(a is b)
print(a is not b)
a = 5
print(a is b)

#0010
a = 3
b = 5
c = 5
a += b # a = a + b
print(a)
a -= c
print(a)
a /= b
print(a)
a *= b
print(a)

#0011
a = b = c = 3
a, b = 3, 4
del a, b, c

#0012
#Приоритет операций:
# ~ ** -
# * / // %
# + -
# << >>
# &
# ^
# |
# =

#0013
print(int, float, complex)
a = 3 + 2j
print(a)
print(complex(3, 2))
print(complex('3+2j'))

#0014
print('Мантиса и показатель степени.')
a = 1.5e5 #1.5 * 10^5
print(a)
a = 1.5e-3 #1.5 * 10^-3
print(a)

#0015
print(abs(-5)) #Модуль числа
print(float('5')) #к типу float
print(int(15.9987)) #к типу int
print(str(15.9987 * 3)) #к типу str
print('И снова конкатенация' + str(15.9987 * 3))
print(max(5,8))
print(min(5.8976, 5.8975))
print(pow(2,3)) #возведение в степень
print(pow(2,3,3))
print(round(8.4)) #округление до ближайшего чётного числа
print(round(8.6))
print(round(8.5))
print(round(7.5))
print(round(5.897363, 4)) #округление с точностью

#0016
import builtins, math
print(math.pi)
print(math.e)
import math as m
print(m.pi)
print(m.e)
from math import pi
print(pi)
from math import * # * - импортировать всё из модуля
print(e)

#0017
print('Тернарный оператор.')
a = float(input('Введите а:\n'))
b = float(input('Введите b:\n'))
print('a > b' if a > b else 'a <= b')

#0018
print('Условный оператор.')
#true True false 'False' 10 -15.6 0 () ' ' '' 5 < 3 5 < 3 or 5 < 8
if True:
    print('Условие истино.')
    print('В блоке условия может быть несколько строк.')
else:
    print('Условие ложно.')
    print('В блоке условия может быть несколько строк.')

#0019
a = float(input('Введите а:\n'))
b = float(input('Введите b:\n'))
if a > b:
    print('a > b')
elif a < b:
    print('a < b')
else:
    print('a == b')

#0020
while True:
    print('Досчитай!')
print('До ста!')

while False:
    print('Условие цикла истинно.')
else:
    print('Условие ложно.')

i = 1
a = 1
while i < 100:
    i += 1
    a *= i
    print(a)
else:
    print(a)
'''