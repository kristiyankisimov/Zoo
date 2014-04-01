import sqlite3
from animal import Animal
from zoo import Zoo


def load():
    conn = sqlite3.connect('animals.db')
    cursor = conn.cursor()
    query = "SELECT * FROM %s" % ('animals')
    result = cursor.execute(query)
    conn.commit()
    conn.close()
    return t


def see_animals(zoo):
    animals = zoo.get_animals()
    for animal in animals:
        weight = animal.get_weight()
        print("%s : %s, %d, %d" % (
            animal.get_name(), animal.get_species(), animal.get_age(), weight))
