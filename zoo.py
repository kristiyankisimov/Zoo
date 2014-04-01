from animal import Animal
from species import Species


class Zoo():
    def __init__(self, capacity, budget, info):
        self.__animals = []
        self.__capacity = capacity
        self.__budget = budget
        self.__info = info

    def calculate_incomes(self):
        self.__incomes += 60 * len(self.__animals)

    def calculate_outcomes(self, food_ratios):
        pass

    def get_animals(self):
        return self.__animals

    def add_animal(self, species, age, name, gender, weight):
        if len(self.__animals) < self.__capacity:
            animal = Animal(species, age, name, gender, weight)
            self.__animals.append(animal)
        else:
            print("Not enough space in zoo!")

    def eat(self):
        pass

    def grow(self):
        pass

    def die(self):
        pass
