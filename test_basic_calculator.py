import pytest
from basic_mode_calculator import BasicCalculator


# Unit Tests for a Basic Mode Calculator
class TestsCalc:
    # one instance of the calculator that can be used in all test cases
    calc = BasicCalculator()

    def test_add(self):
        result, expected = self.calc.add(5, 9), 14
        assert result == expected

    def test_sub(self):
        result, expected = self.calc.sub(5, 9), -4
        assert result == expected

    def test_mul(self):
        result, expected = self.calc.mul(5, 9), 45
        assert result == expected

    def test_div(self):
        result, expected = self.calc.div(9, 3), 3
        assert result == expected

    # checking if an exception will be thrown if the divisor = 0
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError) as ex:
            self.calc.div(8, 0)
        assert "division by zero" in str(ex.value)

    def test_power(self):
        result, expected = self.calc.power(9, 3), 729
        assert result == expected

    def test_sqr_root(self):
        result, expected = self.calc.square_root(16), 4
        assert result == expected

    # checking if an exception will be thrown when taking the square root to a negative number
    def test_negative_sqr_root(self):
        with pytest.raises(ValueError) as ex:
            self.calc.square_root(-6)
        assert "math domain error" in str(ex.value)

    def test_nth_root(self):
        result, expected = round(self.calc.nth_root(8, 5), 9), 1.515716567
        assert result == expected

    # Test case functions for the "STRING OF OPERATIONS" function
    def test_string_of_operations(self):
        result, expected = self.calc.string_of_operations("900/(6*12)+(85*96)"), 8172.5
        assert result == expected

    # checking if an exception will be thrown when entering invalid operations
    def test_additional_parenthesis(self):
        with pytest.raises(IndexError) as ex:
            self.calc.string_of_operations("((6+1)")
        assert "pop from empty list" in str(ex.value)

    def test_missed_parenthesis(self):
        with pytest.raises(IndexError) as ex:
            self.calc.string_of_operations("6+1)")
        assert "list index out of range" in str(ex.value)

    def test_invalid_operator(self):
        with pytest.raises(IndexError) as ex:
            self.calc.string_of_operations("6+1+")
        assert "pop from empty list" in str(ex.value)

