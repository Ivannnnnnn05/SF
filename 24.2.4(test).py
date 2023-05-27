import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 4, 5) == 9

    def test_division_success(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_multiply_success(self):
        assert self.calc.multiply(self, 8, 5) == 40

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 5, 1) == 4

    def test_zero_division(self):      #тоже проверил на всякий случай)
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 3, 0)

    def teardown(self):
        print('Выполнение метода Teardown')
