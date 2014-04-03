from random import randint


class Animal():
    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight

    def grow(self, average_weight, weight_age_ratio):
        if self.weight < average_weight:
            self.weight += weight_age_ratio
        self.age += 1

    def eat(self, food_weight_ratio):
        return self.weight * food_weight_ratio

    def die(self, life_expectancy):
        in_months = life_expectancy * 12
        return randint(1, in_months) < self.age
