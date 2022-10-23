salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев


def total_minus(m, sp, inc, sa):
    current_month = 1
    sum_spend = 0
    while current_month <= m:
        sum_spend += sp
        sp = sp * (1 + inc)
        sum_salary = sa * current_month
        current_month += 1
    return sum_spend - sum_salary


need_money = total_minus(months, spend, increase, salary)

print(round(need_money))
