import cv2
import pytesseract


# Функция для получения изображения автомобиля
def get_img(img_address):
    car_img = cv2.imread(img_address)
    car_img = cv2.cvtColor(car_img, cv2.COLOR_BGR2RGB)
    return car_img


# Функция для нахождения изображения номера автомобиля
def car_num_img(img, haar_cascade):
    number_coordinates = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=6)

    for x, y, w, h in number_coordinates:
        number_img = img[y + 10: y + h - 5, x + 15: x + w - 15]

    return number_img


# Функция для увеличения изображения номера автомобиля по заданному масштабу
def image_enlargement(image, scale):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    size = (width, height)
    resized_img = cv2.resize(image, size, interpolation=cv2.INTER_LINEAR)

    return resized_img


# Основная функция для преобразования изображения номера в текст
def get_number(address):
    try:
        car_1 = get_img(address)
    except:
        print('Не удалось открыть изображение')
        quit()
    haar_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

    car_num = car_num_img(car_1, haar_cascade)
    car_num = image_enlargement(car_num, 2)

    car_num_bw = cv2.cvtColor(car_num, cv2.COLOR_RGB2GRAY)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    result = pytesseract.image_to_string(
        car_num_bw,
        config='--psm 6 --oem 3 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789')

    return result.strip()
