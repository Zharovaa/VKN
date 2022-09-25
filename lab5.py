import math

x = float(input('Введіть значення аргументу функції x: '))

if x >= 5:
    y = - 9 + math.log(x) + math.sqrt(x)
elif - 0.5 < x < 5:
    y = math.cos(x) + math.sin(2 * x)
elif x <= - 0.5:
    y = math.fabs(- x ** 2 + 2 * x ** -x)

print('x =', x, '\ny =', y)




