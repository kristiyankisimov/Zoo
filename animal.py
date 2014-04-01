from ramdom import randint


class Animal():
    def __init__(self, specie, age, name, gender, weight):
        self.__specie = specie
        self.__age = age
        self.__name = name
        self.__gender = gender
        self.__weight = weight

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_weight(self):
        return self.__weight

    def set_species(self, specie):
        self.__specie = specie

    def update_age(self, age):
        self.__age += age
        if self.chance_of_dying() > randint(0, 100):
            return False
        return True

    def chance_of_dying(self):
        return self.__age / self.specie.life_expectancy

    def update_weight(self, weight):
        self.__weight = weight
