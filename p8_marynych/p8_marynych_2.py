try:
    a = float(input("Введіть коефіціент a: "))
    b = float(input("Введіть коефіціент b: "))
    c = float(input("Введіть коефіціент c: "))
    d = ((b**2) - 4 *(a*c))**0.5
    x1 = (-b+d)/(2*a)
    x2 = (-b-d)/(2*a)
    print("x1 =",x1,'x2 =',x2)
except ZeroDivisionError:
    print("ZeroDivisionError Я вам забороняю ділити на 0")
except ValueError:
    print("ValueError недопустиме значення ")
except Exception :
    print("Невідома помилка")