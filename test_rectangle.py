import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_number_mul(self):
        res = area(123, 321)
        self.assertEqual(res, 39483)

    def test_number_add(self):
        res = perimeter(12, 34)
        self.assertEqual(res, 92)

    def test_zero_add(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_square_add(self):
        res = perimeter(12, 12)
        self.assertEqual(res, 48)


if __name__ == '__main__':
    unittest.main()
