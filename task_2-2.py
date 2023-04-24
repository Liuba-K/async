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

    with open('orders.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders-1.json', 'w', encoding='utf-8') as f_n:
            list_orders = data["orders"]
            Dict_ex = {
                "item": item,
                "quantity": quantity,
                "price": price,
                "buyer": buyer,
                "date": date
            }
            list_orders.append(Dict_ex)
            json.dump(data, f_n, indent=4, ensure_ascii=False)
        #отступ indent
        #ensure_ascii = False, строки запишутся как есть
    #w-перезаписываем только последние данные


write_order_to_json("book", 2, 10.50, "Lisa", "22-10-2022")
write_order_to_json("компьютер", 5, 25, "Sidorov", "02-05-2022")


