import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_zero1_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_zero2_mul(self):
        res = area(0, 66)
        self.assertEqual(res, 0)

    def test_number1_mul(self):
        res = area(5, 7)
        self.assertEqual(res, 17.5)

    def test_number2_mul(self):
        res = area(4, 8)
        self.assertEqual(res, 16)

    def test_zero_add(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_cube_add(self):
        res = perimeter(4, 4, 4)
        self.assertEqual(res, 12)

    def test_number_add(self):
        res = perimeter(6, 7, 8)
        self.assertEqual(res, 21)


if __name__ == '__main__':
    unittest.main()
