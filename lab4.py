import math

def f(x):
    try:
        numerator = x + math.sin(x)
        denominator = math.log10(abs(x - x**4))
        term1 = numerator / denominator
        term2 = math.log(x, 4)
        return term1 + term2
    except ValueError as e:
        return f"Помилка в обчисленнях: {e}"

x = float(input("Введіть значення x: "))
result = f(x)
print("Значення функції f(x):", result)
