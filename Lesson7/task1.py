# -*- coding: cp1251 -*-
'''����������� ����� Matrix (�������). ���������� ���������� ������������ ������ (����� init()),
������� ������ ��������� ������ (������ �������) ��� ������������ �������.
���������: ������� � ������� ��������� �������������� �������, ������������� � ���� ������������� �����.
������� ������: ��. � ���������.

��������� ��� � ����������� ���������� ������ str() ��� ������ ������� � ��������� ����.
����� ����������� ���������� ������ add() ��� ���������� �������� �������� ���� �������� ������ Matrix (���� ������).
����������� �������� ������ ���� ����� �������.
���������: �������� ��������� ������ ��������� ����������� � ������ ������� ������ ������ ������ ������� ���������� �
������ ��������� ������ ������ ������ ������� � �.�.
'''
from random import randint
class Matrix:
    def __init__(self,row=3,col=2):
        self.row = row
        self.col = col
        i=0
        matrix = []
        while i < self.row:
            list = []
            j=0
            while j< self.col:
                list.append(randint(1,100))
                j+=1
            matrix.append(list)
            i+=1
        self.matrix = matrix

    def __add__(self, other):
        matr =[]
        i=0
        while i < self.row:
            addmatr = []
            rows = self.matrix[i]
            rowsoth = other.matrix[i]
            j = 0
            while j < self.col:
                cols = rows[j]
                colsoth = rowsoth[j]
                addmatr.append(colsoth+cols)
                j += 1
            matr.append(addmatr)
            i += 1
        self.matrix = matr
        return '\n'.join(' '.join(map(str,i)) for i in self.matrix)

    def __str__(self):
        return '\n'.join(' '.join(map(str,i)) for i in self.matrix)

matrix1 = Matrix()
matrix2 = Matrix()
print(f'{matrix1}\n\n{matrix2}\n\n{matrix1+matrix2}')
