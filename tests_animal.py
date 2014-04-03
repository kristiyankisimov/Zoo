from animal import Animal
import unittest


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.animal = Animal("tiger", 10, "Tig", "male", 175)

    def test_properties(self):
        self.assertEqual(self.animal.species, "tiger")
        self.assertEqual(self.animal.age, 10)
        self.assertEqual(self.animal.name, "Tig")
        self.assertEqual(self.animal.gender, "male")
        self.assertEqual(self.animal.weight, 175)

    def test_grow(self):
        self.animal.grow(250, 15.1)
        self.assertEqual(11, self.animal.age)
        self.assertEqual(190.1, self.animal.weight)

    def test_grow_again(self):
        self.animal.grow(175, 2)
        self.assertEqual(11, self.animal.age)
        self.assertEqual(175, self.animal.weight)

    def test_eat(self):
        self.assertEqual(17.5, self.animal.eat(0.1))

    def test_die(self):
        is_dead = self.animal.die(3)
        self.assertEqual(False, is_dead)


if __name__ == '__main__':
    unittest.main()
