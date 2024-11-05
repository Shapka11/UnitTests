import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(11)
        self.assertEqual(res, 121)

    def test_zero_add(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_add(self):
        res = perimeter(6)
        self.assertEqual(res, 24)


if __name__ == '__main__':
    unittest.main()
