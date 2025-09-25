import pytest

class Test_Math:


    def test_divide_number(self):
        pytest.xfail("Need to investigate")
        num = 10
        result = num + num
        assert result == num/num

    @pytest.mark.xfail(reason="Result adds not multiply")
    def test_square_false(self):
        num = 10
        result = num + num
        assert result == num**2

    @pytest.mark.xfail(reason="Assert is correct")
    def test_cube(self):
        num = 10
        result = num * num * num
        assert result == num ** 3

    @pytest.mark.xfail(run=False)
    def test_square_true(self):
        num = 10
        result = num * num
        assert result == num ** 2