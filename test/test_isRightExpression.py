import pytest
import sys
sys.path.append("../")
from calculator import isRightExpression

def test_is_expected_1():
    equation = ["1", "+", "41"]
    expected_equation = ["32", "+", "10"]
    expected_result = False

    result = isRightExpression(equation, expected_equation)
    assert expected_result == result
    
def test_is_expected_2():
    equation = ["1", "+", "41"]
    expected_equation = ["1", "+", "41"]
    expected_result = True

    result = isRightExpression(equation, expected_equation)
    assert expected_result == result

def test_is_expected_3():
    equation = ["1", "+", "1"]
    expected_equation = ["1", "+", "1"]
    expected_result = True

    result = isRightExpression(equation, expected_equation)
    assert expected_result == result