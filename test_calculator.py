
import math
import pytest

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    square_root,
    factorial,
    sin,
    cos,
    tan,
    log10,
    natural_log,
)


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(2, 3) == -1


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5

    with pytest.raises(ValueError):
        divide(10, 0)


def test_power_and_square_root():
    assert power(2, 3) == 8
    assert square_root(25) == 5

    with pytest.raises(ValueError):
        square_root(-1)


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1

    with pytest.raises(ValueError):
        factorial(-1)

    with pytest.raises(ValueError):
        factorial(2.5)


def test_trigonometry():
    assert math.isclose(sin(30), 0.5)
    assert math.isclose(cos(60), 0.5)
    assert math.isclose(tan(45), 1.0)

    with pytest.raises(ValueError):
        tan(90)


def test_logarithms():
    assert log10(100) == 2
    assert math.isclose(natural_log(math.e), 1)

    with pytest.raises(ValueError):
        log10(0)

    with pytest.raises(ValueError):
        natural_log(-1)
 
