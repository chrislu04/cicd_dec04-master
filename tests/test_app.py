import sys
from pathlib import Path
import pytest
import math

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import (add, sub, multiply, divide, logarithm, square, 
                 sine, cosine, square_root, percentage)

def test_add():
    assert add(5, 6) == 11

def test_add_negative():
    assert add(-5, -6) == -11
    assert add(-5, 6) == 1

def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5

def test_add_float():
    assert abs(add(5.5, 6.3) - 11.8) < 0.0001

def test_sub():
    assert sub(10, 6) == 4

def test_sub_negative():
    assert sub(-5, -6) == 1
    assert sub(5, -6) == 11

def test_sub_zero():
    assert sub(0, 0) == 0
    assert sub(5, 0) == 5

def test_sub_float():
    assert abs(sub(10.5, 6.3) - 4.2) < 0.0001

def test_multiply():
    assert multiply(5, 6) == 30

def test_multiply_negative():
    assert multiply(-5, 6) == -30
    assert multiply(-5, -6) == 30

def test_multiply_zero():
    assert multiply(5, 0) == 0
    assert multiply(0, 0) == 0

def test_multiply_float():
    assert abs(multiply(2.5, 4) - 10.0) < 0.0001

def test_divide():
    assert divide(10, 2) == 5

def test_divide_negative():
    assert divide(-10, 2) == -5
    assert divide(-10, -2) == 5

def test_divide_float():
    assert abs(divide(10.5, 2) - 5.25) < 0.0001

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_divide_zero_by_number():
    assert divide(0, 5) == 0

def test_logarithm_base_10():
    assert abs(logarithm(100, 10) - 2.0) < 0.0001

def test_logarithm_base_e():
    assert abs(logarithm(math.e, math.e) - 1.0) < 0.0001

def test_logarithm_base_2():
    assert abs(logarithm(8, 2) - 3.0) < 0.0001

def test_logarithm_default_base():
    assert abs(logarithm(1000) - 3.0) < 0.0001

def test_logarithm_negative_number():
    with pytest.raises(ValueError, match="Logarithm undefined for non-positive numbers"):
        logarithm(-5)

def test_logarithm_zero():
    with pytest.raises(ValueError, match="Logarithm undefined for non-positive numbers"):
        logarithm(0)

def test_logarithm_invalid_base_zero():
    with pytest.raises(ValueError, match="Logarithm base must be positive and not equal to 1"):
        logarithm(10, 0)

def test_logarithm_invalid_base_one():
    with pytest.raises(ValueError, match="Logarithm base must be positive and not equal to 1"):
        logarithm(10, 1)

def test_logarithm_invalid_base_negative():
    with pytest.raises(ValueError, match="Logarithm base must be positive and not equal to 1"):
        logarithm(10, -2)

def test_square_positive():
    assert square(5) == 25

def test_square_negative():
    assert square(-5) == 25

def test_square_zero():
    assert square(0) == 0

def test_square_float():
    assert abs(square(2.5) - 6.25) < 0.0001

def test_sine():
    assert abs(sine(0) - 0.0) < 0.0001
    assert abs(sine(math.pi / 2) - 1.0) < 0.0001
    assert abs(sine(math.pi)) < 0.0001

def test_sine_negative():
    assert abs(sine(-math.pi / 2) - (-1.0)) < 0.0001

def test_cosine():
    assert abs(cosine(0) - 1.0) < 0.0001
    assert abs(cosine(math.pi / 2)) < 0.0001
    assert abs(cosine(math.pi) - (-1.0)) < 0.0001

def test_cosine_negative():
    assert abs(cosine(-math.pi) - (-1.0)) < 0.0001

def test_square_root_positive():
    assert square_root(25) == 5
    assert square_root(16) == 4

def test_square_root_zero():
    assert square_root(0) == 0

def test_square_root_float():
    assert abs(square_root(6.25) - 2.5) < 0.0001

def test_square_root_negative():
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
        square_root(-5)

def test_percentage():
    assert percentage(50, 200) == 25.0
    assert percentage(75, 150) == 50.0

def test_percentage_zero_value():
    assert percentage(0, 100) == 0.0

def test_percentage_greater_than_total():
    assert percentage(150, 100) == 150.0

def test_percentage_negative():
    assert percentage(-25, 100) == -25.0

def test_percentage_zero_total():
    with pytest.raises(ValueError, match="Total cannot be zero for percentage calculation"):
        percentage(50, 0)