# -*- coding: cp1251 -*-
#������� (����������) ��������� ����, �������� � ���� ���������� ����� �����, ����������� ���������.
#��������� ������ ������������ ����� ����� � ����� � �������� �� �� �����
try:
    with open('task5.txt', 'w') as f_five:
        user_data = input('������� ����� ����� ������: ')
        f_five.writelines(user_data)
        user_num = user_data.split()
        print(sum(map(int,user_num)))
except IOError:
    print("��������� ������ �����-������!")