import sqlite3


# Функция для создания и записи данных в базу
def db_entry(function, data_base):
    address_lst = ['images/car_1.jpeg', 'images/car_2.jpg', 'images/car_3.jpg', 'images/car_4.jpg', 'images/car_5.jpg']

    num_lst = map(function, address_lst)

    addresses_and_nums = dict(zip(address_lst, num_lst))

    db = sqlite3.connect(data_base)
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
        path TEXT,
        number TEXT
    )''')
    db.commit()
    for key, value in addresses_and_nums.items():
        cursor.execute(f'SELECT path FROM  cars WHERE path = "{key}"')
        val = cursor.fetchone()
        if val is None:
            cursor.execute(f'INSERT INTO cars VALUES ("{key}", "{value}")')
            db.commit()
