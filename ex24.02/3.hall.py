import math

def program():
	
    print('3. Можно ли в квадратном зале площадью S '
    'поместить круглую сцену радиусом R так,'
    ' чтобы от стены до сцены был проход менее К? '
    'Все параметры вводятся пользователем. '
    'Выполнение программы зациклить.\n')

    S=int(input('Введите S: '))
    print("S="+str(S))

    R=int(input('Введите R: '))
    print("R=" + str(R))

    K=int(input('Введите K: '))
    print("K="+ str(K))

    if (S-K)>R : 
        print("Вы можете поставить сцену")

    if S-K<=R: 
        print('Вы не можете поставить сцену')
    return
    
flag = True

while flag:
    program()
    flag = input('Запустить программу ещё раз? [y/n]') == 'y'

print ("Конец программы.")


