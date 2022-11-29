"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
        if max_discount >= 100:
            raise ValueError #Слишком большая максимальная скидка
        if price <= 0:
            raise ValueError #Неверное значении цены
        if discount <= 0:
            raise ValueError #Неверное значение скидки
        if type(price) is str:
            raise TypeError
        if type(discount) is str:
            raise TypeError
        if type(max_discount) is str:
            raise TypeError
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (ValueError, TypeError):
        print('Неверное значение аргумента')
    


    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
    print(discounted(-100, -22))

    
