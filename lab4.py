import math
def countS(n, t, k) :
 PI = math.pi
 return 4.17 * (math.sqrt(t)) - math.sin(PI * n + PI/7) + (math.e ** (k/t + n));

n = float(input("Enter n:"))
t = float(input("Enter t:"))
k  = float(input("Enter k:"))

print("Значення виразу: ", countS(n, t, k))