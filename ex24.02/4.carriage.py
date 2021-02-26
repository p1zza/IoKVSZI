import math

def program():
	
    print('4. Дан номер места в плацкартном вагоне. '
    'Определить, какое это место - верхнее или нижнее,'
    ' в купе или боковое. Номер вводится пользователем. '
    'Выполнение программы зациклить.\n')

    place = int(input("Введите номер места: "))
    if(place <=54):
        if(place%2 == 1) : print('Место ',place,'находится на нижней полке ')
        if(place%2 == 0) : print('Место ',place,'находится на верхней полке ')
        if (place>=1)and(place<=36): print('в купе.')
        if (place>=37)and(place<=54): print('сбоку.')
    else: print("Такого места нет")
    return
    
flag = True

while flag:
    program()
    flag = input('Запустить программу ещё раз? [y/n]') == 'y'

print ("Конец программы.")


