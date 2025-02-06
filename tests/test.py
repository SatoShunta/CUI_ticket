import unittest
from source import simulator

class TestSimulator(unittest.TestCase):

    def test_calculate_total(self):
        items = [
            {"name": "特製ラーメン", "price": 1000},
            {"name": "しおラーメン", "price": 880}
        ]
        total = simulator(items)
        self.assertEqual(total, 1880)

if __name__ == '__main__':
    unittest.main()
