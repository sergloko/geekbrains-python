'''Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников
'''
staff = dict()
try:
    with open("task3.txt") as f_third:
        for line in f_third:
            key, value = line.split()
            staff[key] = value
except IOError:
    print("Произошла ошибка ввода-вывода!")
print(staff)
print('Список сотрудников с окладом менее 20000')
i = 0
sum_salary = 0
for x, y in staff.items():
    if float(y) < 20000:
        print(x)
    sum_salary += float(y)
    i +=1
print('Средний оклад составляет:', "%.2f"%(sum_salary / i))
