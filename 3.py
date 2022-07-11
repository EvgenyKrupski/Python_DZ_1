'''3. Напишите программу, которая принимает на вход координаты точки (X и 
Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой 
находится эта точка (или на какой оси она находится).'''

coordinatX = input('Введите координату X = ')
try:
    coordinatX = int(coordinatX)
except:
    print('Вы ввели не то, повторите')

coordinatY = input('Введите координату Y = ')
try:
    coordinatY = int(coordinatY)
except:
    print('Вы ввели не то, повторите')


def Quarter(a,b):
    if a == 0 or b == 0:
        print('Число не находится в какой-либо плоскости!')
    elif a > 0 and b > 0:
        print('Число находится в четверти 1')
    elif a < 0 and b > 0:
        print('Число находится в четверти 2')
    elif a < 0 and b < 0:
        print('Число находится в четверти 3')
    else:
        print('Число находится в четверти 4')

Quarter(coordinatX,coordinatY)