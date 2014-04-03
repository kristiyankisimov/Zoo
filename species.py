class Species():
    """docstring for Species"""
    def __init__(self, life_exp, food, gest, nw, aw, wa_ratio, fw_ratio):
        self.__life_expectancy = life_exp
        self.__food = food
        self.__gestation = gest
        self.__newborn_weight = nw
        self.__average_weight = aw
        self.__weight_age_ratio = wa_ratio
        self.__food_weight_ratio = fw_ratio

    def life_expectancy(self):
        return self.__life_exp

    def food(self):
        return self.__food

    def gestation_period(self):
        return self.__gestation

    def newborn_weight(self):
        return self.__newborn_weight

    def average_weight(self):
        return self.__average_weight

    def weight_age_ratio(self):
        return self.__weight_age_ratio

    def food_weight_ratio(self):
        return self.__food_weight_ratio
