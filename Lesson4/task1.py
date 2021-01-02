'''Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами'''
from sys import argv
script_name, work_hours, rate_hour, bonus = argv
new_work_hours = int(work_hours)
new_rate_hour = int(rate_hour)
new_bonus = int(bonus)
salary = (new_work_hours * new_rate_hour) + new_bonus
print("Зарплата составит: ", salary)