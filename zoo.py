class Zoo():
    def __init__(self, capacity, budget):
        self.capacity = capacity
        self.budget = budget
        self.animals = []

    def incomes_per_day(self):
        return len(self.animals) * 60

    def outcomes_per_day(self):
        pass
