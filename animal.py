class Animal():
    def __init__(self, species, age, name, gender, weight):
        self.__species = species
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

    def get_gender():
        return self.__gender

    def get_weight():
        return self.__weight

    def set_species(self, species):
        self.__species = species

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_gender(self, gender):
        self.__gender = gender

    def set_weight(self, weight):
        self.__weight = weight

    def grow(self):
        self.__age += 1

    def eat(self):
        pass

    def die():
        pass
