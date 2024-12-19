import math

def F(x, a, b):
    try:
        term1 = x * math.tan(x) * math.exp(a - b)
        term2 = math.log(abs(x**2 + 0.7), 4)
        return term1 + term2
    except ValueError as e:
        return f"Помилка в обчисленнях: {e}"

x = float(input("Введіть значення x: "))
a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
result = F(x, a, b)
print("Значення виразу F:", result)
