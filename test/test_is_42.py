import pytest
import sys
sys.path.append("../")
from do_calc import is_42

def test_is_42_with_1():
    # arrange
    number = 1
    expected_result = False

    # action
    result = is_42(number)
    # assert
    assert result == expected_result

def test_is_42_with_42():
    # arrange
    number = 42
    expected_result = True

    # action
    result = is_42(number)
    # assert
    assert result == expected_result