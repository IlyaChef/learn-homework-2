"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
stock = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
  
def count_sum(sales):
    sales_sum = 0
    for sale in sales:
        sales_sum += sale
    return sales_sum

def count_avg(sales):
    sales_avg = 0
    for sale in sales:
        sales_avg += sale
    return round(sales_avg / len(sales))

stock_sum_sales = 0
for phone in stock:
    sales_qty = count_sum(phone['items_sold'])
    print(f'Суммарное количество продаж {phone["product"]}: {sales_qty}')
    stock_sum_sales += sales_qty

stock_avg_sales = 0
for phone in stock:
    sales_avg = count_avg(phone['items_sold'])
    print(f'Среднее количество продаж {phone["product"]}: {sales_avg}')
    stock_avg_sales += sales_avg

stock_avg_total = round(stock_avg_sales/len(stock))

print(f'Cуммарное количество продаж всех товаров: {stock_sum_sales}')
print(f'Cреднее количество продаж всех товаров: {stock_avg_total}')


        
          
    
    
    
