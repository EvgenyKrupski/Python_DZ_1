# 4. Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y).

quart = int(input('Введите четверть: '))

if кварт==1:
    mes='x>0, y>0'
elif quart==2:
    mes='x<0, y>0'
elif quart==3:
    mes='x<0, y<0'
elif quart==4:
    mes='x>0, y<0'
else:
    mes='Такой четверти нет'
print(mes)