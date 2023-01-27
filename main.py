from db_entry import db_entry
from reading_db import reading_db
from get_number import get_number


def main():
    data_base = 'cars_num.db'
    address_list = ['images/car_1.jpeg', 'images/car_2.jpg', 'images/car_3.jpg', 'images/car_4.jpg', 'images/car_5.jpg']
    num_list = map(get_number, address_list)
    addresses_and_nums = dict(zip(address_list, num_list))
    db_entry(data_base, addresses_and_nums)
    reading_db(data_base)


if __name__ == '__main__':
    main()

