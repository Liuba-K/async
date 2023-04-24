"""
2. Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными.
Для этого: Создать функцию write_order_to_json(), в которую передается 5 параметров —
товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json

def write_order_to_json(item, quantity, price, buyer, date):
    Dict_ex = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }
    with open('orders.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

        with open('orders-1.json', 'w', encoding='utf-8') as f_n:
            data['orders'].append(Dict_ex)
            json.dump(data, f_n)



write_order_to_json('book', 2, 10.50, 'Lisa', "22-10-2022")

