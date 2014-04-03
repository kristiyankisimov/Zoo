from zoo import Zoo
import unittest


class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo(50, 1500)

    def test_properties(self):
        self.assertEqual(self.zoo.capacity, 50)
        self.assertEqual(self.zoo.budget, 1500)
        self.assertEqual(self.zoo.animals, [])


if __name__ == '__main__':
    unittest.main()
