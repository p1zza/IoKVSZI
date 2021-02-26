import math

def program():
	
    print('6. Имеются две ёмкости: кубическая с ребром А,'
    'цилиндрическая с высотой H и радиусом основания R.'
    'Определить, поместится ли жидкость объёма М в первую'
    'ёмкость, во вторую, в обе. Все параметры вводятся пользователем.'
    ' Выполнение программы зациклить.\n')

    import math

    A=int(input('Введите длину ребра куба: '))
    CubeVolume=A**3
    print("Объём куба = " + str(CubeVolume))

    H=int(input('Введите высоту цилиндра: '))
    R=int(input('Введите радиус основания цилиндра: '))
    pi=math.pi
    CylinderVolume=pi*R**2*H
    print("Полученный объём цилиндра: " + str(CylinderVolume))

    LiquidVolume=int(input('Введите объём жидкости: ')) 
    print("Объём жидкости: " + str(LiquidVolume))

    if CubeVolume >= LiquidVolume: print("Жидкость поместится в куб. ")
    else : print("Жидкость не поместится в куб. ")
    
    if CylinderVolume >= LiquidVolume: print("Жидкость поместится в цилиндр. ")
    else : print("Жидкость не поместится в цилиндр. ")

    if LiquidVolume >= CylinderVolume + CubeVolume : print("Жидкость не поместится в куб и цилиндр.")
    else : print("Жидкость поместится в куб и цилиндр.")  
    
    return
    
flag = True

while flag:
    program()
    flag = input('Запустить программу ещё раз? [y/n]') == 'y'

print ("Конец программы.")


