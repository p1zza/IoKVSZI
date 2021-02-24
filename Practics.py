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
'''

#0007
print(bin(50) + '\n' + bin(30))
print(' ' + bin(50&30))
print(bin(50&30))
print(bin(50|30))
print(bin(50^30))
print(bin(50<<3))
print(bin(50>>3))
