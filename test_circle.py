import math
import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_number_mul(self):
        res = area(7)
        self.assertEqual(res, 49 * math.pi)

    def test_perimetr_mul(self):
        res = perimeter(12)
        self.assertEqual(res, 24 * math.pi)

    def test_zero_perimetr_mul(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
