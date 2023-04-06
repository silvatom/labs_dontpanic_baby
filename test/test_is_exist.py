import pytest
import sys
sys.path.append("../")
from do_calc import check_elems

def test_exist_x():
    #arrange
    expected_result = ["x", "x", "x"]
    inp_equation = ["4", "+", "2"]
    right_equation = ["7", "*", "8"]
    #action
    result = check_elems(inp_equation, right_equation)

    #assert
    assert expected_result == result

def test_exist_x_c():
    #arrange
    expected_result = ["x", "x", "c"]
    inp_equation = ["2", "+", "8"]
    right_equation = ["7", "*", "8"]
    #action
    result = check_elems(inp_equation, right_equation)

    #assert
    assert expected_result == result

def test_exist_c_in_the_middle():
    #arrange
    expected_result = ["x", "c", "x"]
    inp_equation = ["2", "+", "10"]
    right_equation = ["7", "+", "8"]
    #action
    result = check_elems(inp_equation, right_equation)

    #assert
    assert expected_result == result
    
def test_exist_c_first():
    #arrange
    expected_result = ["c", "x", "x"]
    inp_equation = ["7", "*", "10"]
    right_equation = ["7", "+", "8"]
    #action
    result = check_elems(inp_equation, right_equation)

    #assert
    assert expected_result == result
    
def test_exist_c_first():
    #arrange
    expected_result = ["c", "c", "c"]
    inp_equation = ["7", "*", "10"]
    right_equation = ["7", "*", "10"]
    #action
    result = check_elems(inp_equation, right_equation)

    #assert
    assert expected_result == result
    
def test_exist_t_first():
    #arrange
    expected_result = ["t", "x", "x"]
    inp_equation = ["10", "+", "9"]
    right_equation = ["7", "*", "10"]
    #action
    result = check_elems(inp_equation, right_equation)

    #assert
    assert expected_result == result
    
def test_exist_t_last():
    #arrange
    expected_result = ["x", "x", "t"]
    inp_equation = ["8", "+", "7"]
    right_equation = ["7", "*", "10"]
    #action
    result = check_elems(inp_equation, right_equation)

    #assert
    assert expected_result == result
    
def test_exist_t_last():
    #arrange
    expected_result = ["x", "t", "x", "t", "x"]
    inp_equation = ["8", "+", "9", "*", "1"]
    right_equation = ["7", "*", "10", "+", "2"]
    #action
    result = check_elems(inp_equation, right_equation)

    #assert
    assert expected_result == result