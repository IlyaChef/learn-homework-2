"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
age = int(input())

def main():
    
    if 0 < age < 7:
        print('Вы должны учиться в детском саду')
    elif 7 <= age <= 17:
        print('Вы должны учиться в школе')
    elif 17 < age <= 23:
        print('Вы должны учиться в ВУЗе')
    else:
        print('Вы должны работать')
main()
print()
    