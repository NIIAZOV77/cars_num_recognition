from db_entry import db_entry
from reading_db import reading_db
from get_number import get_number


def main():
    data_base = 'cars_num.db'
    db_entry(get_number, data_base)
    reading_db(data_base)


if __name__ == '__main__':
    main()

