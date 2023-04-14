import pytest
import sys
sys.path.append("../")
from calculator import checkElems

def test_exist_x():
    #arrange
    expected_result = ["X", "X", "X"]
    inp_equation = ["4", "+", "2"]
    right_equation = ["7", "*", "8"]
    #action
    result = checkElems(inp_equation, right_equation)

    #assert
    assert expected_result == result

def test_exist_x_c():
    #arrange
    expected_result = ["X", "X", "C"]
    inp_equation = ["2", "+", "8"]
    right_equation = ["7", "*", "8"]
    #action
    result = checkElems(inp_equation, right_equation)

    #assert
    assert expected_result == result

def test_exist_c_in_the_middle():
    #arrange
    expected_result = ["X", "C", "X"]
    inp_equation = ["2", "+", "10"]
    right_equation = ["7", "+", "8"]
    #action
    result = checkElems(inp_equation, right_equation)

    #assert
    assert expected_result == result
    
def test_exist_c_first():
    #arrange
    expected_result = ["C", "X", "X"]
    inp_equation = ["7", "*", "10"]
    right_equation = ["7", "+", "8"]
    #action
    result = checkElems(inp_equation, right_equation)

    #assert
    assert expected_result == result
    
def test_exist_c_first():
    #arrange
    expected_result = ["C", "C", "C"]
    inp_equation = ["7", "*", "10"]
    right_equation = ["7", "*", "10"]
    #action
    result = checkElems(inp_equation, right_equation)

    #assert
    assert expected_result == result
    
def test_exist_t_first():
    #arrange
    expected_result = ["T", "X", "X"]
    inp_equation = ["10", "+", "9"]
    right_equation = ["7", "*", "10"]
    #action
    result = checkElems(inp_equation, right_equation)

    #assert
    assert expected_result == result
    
def test_exist_t_last():
    #arrange
    expected_result = ["X", "X", "T"]
    inp_equation = ["8", "+", "7"]
    right_equation = ["7", "*", "10"]
    #action
    result = checkElems(inp_equation, right_equation)

    #assert
    assert expected_result == result
    
def test_exist_t_last():
    #arrange
    expected_result = ["X", "T", "X", "T", "X"]
    inp_equation = ["8", "+", "9", "*", "1"]
    right_equation = ["7", "*", "10", "+", "2"]
    #action
    result = checkElems(inp_equation, right_equation)

    #assert
    assert expected_result == result