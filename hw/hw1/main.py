import math


class Calculator:
    def basic(self, a: float, b: float, op: str) -> float:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                return "Ошибка: деление на ноль"
            return a / b
        else:
            return "Ошибка: неизвестная операция"

    def trig(self, func: str, x: float) -> float:
        if func == "sin":
            return math.sin(x)
        elif func == "cos":
            return math.cos(x)
        elif func == "tg":
            return math.tan(x)
        else:
            return "Ошибка: неизвестная функция"


calc = Calculator()
mode = input("Выберите режим (basic/trig): ")
if mode == "basic":
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    op = input("Введите операцию (+, -, *, /): ")
    result = calc.basic(a, b, op)
    print(f"{a} {op} {b} = {result}")
elif mode == "trig":
    func = input("Введите функцию (sin, cos, tg): ")
    x = float(input("Введите значение (в радианах): "))
    result = calc.trig(func, x)
    print(f"{func}({x}) = {result}")
else:
    print("Ошибка: неизвестный режим")
