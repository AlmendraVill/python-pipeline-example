import pytest
from app import GeometryCalculator

@pytest.fixture
def calculator():
    return GeometryCalculator()

def test_rectangle_area(calculator):
    assert calculator.rectangle_area(5, 10) == 50
    assert calculator.rectangle_area(1, 1) == 1
    with pytest.raises(ValueError):
        calculator.rectangle_area(-5, 10)
    with pytest.raises(ValueError):
        calculator.rectangle_area(5, -10)
    with pytest.raises(ValueError):
        calculator.rectangle_area(0, 10)

def test_rectangle_perimeter(calculator):
    assert calculator.rectangle_perimeter(5, 10) == 30
    assert calculator.rectangle_perimeter(1, 1) == 4
    with pytest.raises(ValueError):
        calculator.rectangle_perimeter(-5, 10)
    with pytest.raises(ValueError):
        calculator.rectangle_perimeter(5, -10)
    with pytest.raises(ValueError):
        calculator.rectangle_perimeter(0, 10)

def test_circle_area(calculator):
    assert pytest.approx(calculator.circle_area(7), 0.01) == 153.938
    assert pytest.approx(calculator.circle_area(1), 0.01) == 3.14159
    with pytest.raises(ValueError):
        calculator.circle_area(-7)
    with pytest.raises(ValueError):
        calculator.circle_area(0)

def test_circle_circumference(calculator):
    assert pytest.approx(calculator.circle_circumference(7), 0.01) == 43.9823
    assert pytest.approx(calculator.circle_circumference(1), 0.01) == 6.28318
    with pytest.raises(ValueError):
        calculator.circle_circumference(-7)
    with pytest.raises(ValueError):
        calculator.circle_circumference(0)