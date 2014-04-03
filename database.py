import sqlite3


class Database():
    def __init__(self, database_name="animals.db"):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def life_expectancy(self, species):
        quiry = "SELECT life_expectancy FROM animals WHERE species\
         = '%s'" % (species)
        result = self.cursor.execute(quiry)
        result = list(map(lambda x: x[0], result))
        return result[0]

    def food_type(self, species):
        quiry = "SELECT food_type FROM animals WHERE species\
         = '%s'" % (species)
        result = self.cursor.execute(quiry)
        result = list(map(lambda x: x[0], result))
        return result[0]

    def gestation_period(self, species):
        pass
