def program():

    print('1. Имеется коробка со сторонами: AxBxC. '
     'Определить, пройдёт ли она в дверь с размерами MxK. ' 
     'Все параметры вводятся пользователем. '
     'Выполнение программы зациклить. \n')
    
    boxLength = int(input("Длина коробки : "))
    boxWidth = int(input("Ширина коробки : "))
    boxHeigh = int(input("Высота коробки : "))
    doorHeigh = int(input("Длина двери : "))
    doorWidth = int(input("Ширина двери : "))
    if ((boxLength<doorHeigh and boxLength<doorWidth and boxWidth<doorWidth and boxWidth<doorHeigh) or
        (boxLength<doorHeigh and boxLength<doorWidth and boxHeigh<doorHeigh and boxHeigh<doorWidth) or
        (boxHeigh<doorWidth and boxHeigh<doorHeigh and boxWidth<doorWidth and boxWidth<doorHeigh) or
        (boxLength<doorHeigh and boxLength<=doorWidth and boxWidth<doorWidth and boxWidth<=doorHeigh ) or
        (boxLength<=doorHeigh and boxLength<doorWidth and boxWidth<=doorWidth and boxWidth<doorHeigh) or
        (boxLength<=doorHeigh and boxLength<doorWidth and boxHeigh<=doorWidth and boxHeigh<doorHeigh) or
        (boxLength<doorHeigh and boxLength<=doorWidth and boxHeigh<doorWidth and boxHeigh<=doorHeigh) or
        (boxHeigh<doorHeigh and boxHeigh<=doorWidth and boxWidth<doorWidth and boxWidth<=doorHeigh) or
        (boxHeigh<=doorHeigh and boxHeigh<doorWidth and boxWidth<=doorWidth and boxWidth<doorHeigh)):
        print("Коробка пролезет")
    else:
        print("Коробка не пролезет")
    return

flag = True

while flag:
    program()
    flag = input('Запустить программу ещё раз? [y/n]') == 'y'

print ("Конец программы.")


