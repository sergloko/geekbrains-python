# -*- coding: cp1251 -*-
'''Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
'''
import json
try:
    with open('task7.txt') as f_seven, open('task7.json', 'w') as f_json:
        lines = f_seven.readlines()
        i=0
        av_profit = 0
        firm_list = []
        firm_dict = dict()
        average_dict = dict()
        for line in lines:
            firm, form, proceeds, costs = line.split()
            profit = float(proceeds)-float(costs)
            print(f"Фирма {firm} с прибылью: {profit} рублей")
            firm_dict[firm] = profit
            if profit >= 0:
                av_profit += profit
                i+=1
        average_profit = av_profit / i
        average_dict['average_profit'] = average_profit
        print(f"\nСредняя прибыль неубыточных компаний составила: {average_profit} рублей")
        firm_list.append(firm_dict)
        firm_list.append(average_dict)
        print(firm_list)
        json.dump(firm_list, f_json)

    # for sub in lines:
    #     subject = sub.replace('(',' ').split()
    #     school[subject[0][:-1]] = sum(
    #         int(i) for i in subject if i.isdigit()
    #     )
except IOError:
    print("Произошла ошибка ввода-вывода!")
