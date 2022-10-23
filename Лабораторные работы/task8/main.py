
money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить


def i(a, b, c, d, e):
    while a > b:
        a = c + a - b
        e += 1
        b *= (1+d)
    return e


month = i(money_capital, spend, salary, increase, month)

print(month)
