#Задача 5 Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x = [0, 0, 0, 0, 1, 1, 1, 1]
y = [0, 0, 1, 1, 0, 0, 1, 1]
z = [0, 1, 0, 1, 0, 1, 0, 1]

for i in range(8):
    print(int(not(x[i] or y[i] or z[i]) == (not x[i] and not y[i] and not z[i])))

