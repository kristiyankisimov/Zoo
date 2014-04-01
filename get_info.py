import sqlite3
from animal import Animal


def load():
    conn = sqlite3.connect('animals.db')
    cursor = conn.cursor()
    query = "SELECT * FROM %s" % ('animals')
    result = cursor.execute(query)
    for t in result:
        print(t)
    conn.commit()
    conn.close()


def main():
    load()


if __name__ == '__main__':
    main()
