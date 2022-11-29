"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def main(string_1, string_2):
    
    if type(string_1) != str or type(string_2) != str:
        return 0
    elif string_1 == string_2:
        return 1
    elif string_1 != string_2 and int(len(string_1)) > int(len(string_2)):
        return 2
    elif string_1 != string_2 and string_2 == 'learn':
        return 3

print(main(2,3))
print(main('python', 'python'))
print(main('learning', 'python'))
print(main('happy', 'learn'))



    

