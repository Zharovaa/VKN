import math
a = float(input("Введіть довжину ребра:"))
x = float(input("Введіть x:"))
y = float(input("Введіть y:"))
z = float(input("Введіть z:"))
if x <= a//2 and y <= a//2 and z <= a//2:
    print("Точка належить кубу")
elif x >= a//2 or x < a//2 and y >= a//2 or y < a//2 and z >= a//2 or z < a//2:
    print("Точка не належить кубу")
