# cars_num_recognition
Основаная функция для запуска программы main.py

В файле db_entry.py описана функция добавления записей в базу данных 

В файле reading_db.py описана функция просмотра записей из базы данных 

В файле get_number.py описаны функции для нахождений номера автомобиля и конвертирования в текст


Поиск номера автомобиля производиться с помощью встроенного в библиотеку opencv каскада Хаара (haarcascade_russian_plate_number.xml),
далее происходит увеличение изображения и преобразование в черно-белый цвет, текст извлекается при помощи библиотеки pytesseract (tesseract-ocr-w64-setup-5.3.0.20221222.exe)