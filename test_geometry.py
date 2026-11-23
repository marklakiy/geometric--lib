import unittest

from circle_area import circle_area
from circle_perimeter import circle_perimeter
from rectangle_area import rectangle_area
from rectangle_perimeter import rectangle_perimeter
from square_area import square_area
from square_perimeter import square_perimeter


class CircleTests(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(3), 28.2743338823)

    def test_area_zero_radius(self):
        self.assertEqual(circle_area(0), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(3), 18.8495559215)

    def test_perimeter_zero_radius(self):
        self.assertEqual(circle_perimeter(0), 0)


class RectangleTests(unittest.TestCase):
    def test_area_different_sides(self):
        self.assertEqual(rectangle_area(4, 5), 20)

    def test_area_zero_sides(self):
        self.assertEqual(rectangle_area(4, 0), 0)

    def test_perimeter_different_sides(self):
        self.assertEqual(rectangle_perimeter(4, 5), 18)

    def test_perimeter_zero_side(self):
        self.assertEqual(rectangle_perimeter(4, 0), 8)


class SquareTests(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(5), 25)

    def test_area_zero_side(self):
        self.assertEqual(square_area(0), 0)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_perimeter_zero_side(self):
        self.assertEqual(square_perimeter(0), 0)
