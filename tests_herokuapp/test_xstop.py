import pytest

class Test_Math:


    def test_divide_number(self):
        num = 10
        result = num + num
        assert result == num/num


    def test_square_false(self):
        num = 10
        result = num + num
        assert result == num**2


    def test_cube(self):
        num = 10
        result = num * num * num
        assert result == num ** 3


    def test_square_true(self):
        num = 10
        result = num * num
        assert result == num ** 2


         