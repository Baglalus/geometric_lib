import circle
import square
import triangle
import calculate
# import pytest


class TestCircle:
    def test_area(self):
        r = 5
        area = circle.area(r)
        assert area == 78.53981633974483

    def test_perimeter(self):
        r = 5
        perimeter = circle.perimeter(r)
        assert perimeter == 31.41592653589793


class TestSquare:
    def test_area(self):
        r = 5
        area = square.area(r)
        assert area == 25

    def test_perimeter(self):
        r = 5
        perimeter = square.perimeter(r)
        assert perimeter == 20


class TestTriangle:
    def test_area(self):
        a, b, c = 3, 3, 3
        area = triangle.area(a, b, c)
        assert area == 3.897114317029974

    def test_perimeter(self):
        a, b, c = 3, 3, 3
        perimeter = triangle.perimeter(a, b, c)
        assert perimeter == 9


class TestCalc:
    def test_valid(self):
        figure = "circle"
        function = "area"
        size = [3]
        try:
            calculate.calc(figure, function, size)
        except AssertionError:
            assert False

    def test_invalid(self):
        figure = "Bebr"
        function = "c++"
        size = 'a'
        try:
            calculate.calc(figure, function, size)
        except AssertionError:
            assert True
