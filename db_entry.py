import sqlite3


# Функция для создания и записи данных в базу
def db_entry(data_base, data_dict):
    db = sqlite3.connect(data_base)
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
        path TEXT,
        number TEXT
    )''')
    db.commit()
    for key, value in data_dict.items():
        cursor.execute(f'SELECT path FROM  cars WHERE path = "{key}"')
        val = cursor.fetchone()
        if val is None:
            cursor.execute(f'INSERT INTO cars VALUES ("{key}", "{value}")')
            db.commit()
        else:
            cursor.execute(f'UPDATE cars SET number = "{value}" WHERE path = "{key}"')
            db.commit()
