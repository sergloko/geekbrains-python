'''Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке
'''
try:
    with open('task2.txt') as second_file:
        i=0
        for line in second_file:
            i+=1
            words = line.split()
            print('В',i, 'строке. Слов: ', len(words))
        print('Всего', i, 'строк')

except IOError:
    print("Произошла ошибка ввода-вывода!")