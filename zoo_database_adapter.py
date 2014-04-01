from zoo import Zoo
from animal import Animal
import sqlite3


class ZooDatabaseAdapter():
    def __init__(self, database, zoo=None):
        self.__zoo = zoo
        self.__database = database
        self.__conn = sqlite3.connect("zoo.db")
        self.__cursor = self.__conn.cursor()


    def connect(self):
        conn = sqlite3.connect(database)
        return conn

    def add_animal(self,conn ,species, age, name, gender, weight):
        cursor = conn.cursor()
        query = "INSERT INTO "