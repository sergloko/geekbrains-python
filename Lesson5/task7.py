# -*- coding: cp1251 -*-
'''������� ������� � ��������� ����������� �������� ��������� ����, � ������� ������ ������ ������ ��������� ������ � �����:
��������, ����� �������������, �������, ��������.
������ ������ �����: firm_1 ��� 10000 5000.

���������� ��������� ��������� ����, ��������� ������� ������ ��������, � ����� ������� �������.
���� ����� �������� ������, � ������ ������� ������� �� �� ��������.
����� ����������� ������. �� ������ ��������� ������� � ������� � �� ���������,
� ����� ������� �� ������� ��������. ���� ����� �������� ������, ����� �������� �� � ������� (�� ��������� �������).
������ ������: [{�firm_1�: 5000, �firm_2�: 3000, �firm_3�: 1000}, {�average_profit�: 2000}].

�������� ������ ��������� � ���� json-������� � ��������������� ����.
������ json-�������:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

���������: ������������ �������� ���������.
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
            print(f"����� {firm} � ��������: {profit} ������")
            firm_dict[firm] = profit
            if profit >= 0:
                av_profit += profit
                i+=1
        average_profit = av_profit / i
        average_dict['average_profit'] = average_profit
        print(f"\n������� ������� ����������� �������� ���������: {average_profit} ������")
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
    print("��������� ������ �����-������!")
