import sqlite3


# Функция для чтения данных из базы данных
def reading_db(data_base):
    db = sqlite3.connect(data_base)
    cursor = db.cursor()

    for value in cursor.execute('SELECT * FROM cars'):
        print(value)
