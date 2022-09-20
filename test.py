import  math
def firstDigit(n) :
 digits = (int)(math.log10(n))
 n = (int)(n / pow(10, digits))
 return n;

def lastDigit(n) :
 return (n % 10)

n = int(input("Введіть число: "))
d = firstDigit(n) - lastDigit(n)
print("Різниця першої та останньої цифри вашого числа", d)
