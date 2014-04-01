from animal import Animal


class Zoo():
    def __init__(self, capacity, budget):
        self.__animals = []
        self.__capacity = capacity
        self.__budget = budget
        self.__incomes =
        self.__outcomes = 0
        self.__reproduce = False

    def calculate_incomes(self):
        self.__incomes += 60*len(self.__animals)

    def calculate_outcomes(self, food_ratios):
        pass

    def get_animals(self):
        return self.__animals

    def add_animal(self, species, age, name, gender, weight):
        animal = Animal(species, age, name, gender, weight)
        self.__animals.append(animal)
