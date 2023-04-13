import pytest
import sys
sys.path.append("../")
from do_calc import getExprResult

# no maximo: 2 operadores 4 inteiros
# minimo: 1 operador e 5 inteiros 
def test_result_2():
    # arrange
    expected_result = 2
    inp_front = ['1', '+', '1']

    # action
    result = getExprResult(inp_front)
    # assert
    assert result == expected_result

def test_result_42():
    # arrange
    expected_result = 42
    inp_front = ['8', '*', '9', '-', '3', '0']

    # action
    result = getExprResult(inp_front)
    # assert
    assert result == expected_result

def test_result_42_precedence():
    # arrange
    expected_result = -42
    inp_front = ['3', '0', '-', '8', '*', '9']

    # action
    result = getExprResult(inp_front)
    # assert
    assert result == expected_result

# ['0', '1', '6', '4', '/', '0', '4']
def test_leading_zero():
    expect_result = 42
    input_front = ['1', '6', '8', '/', '0', '4']

    result = getExprResult(input_front)

    assert result == expect_result

def test_leading_zero_starts_with_zero():
    expect_result = 42
    input_front = ['0', '1', '6', '8', '/', '0', '4']

    result = getExprResult(input_front)

    assert result == expect_result

def test_leading_zero_more_operetors():
    expect_result = 217
    input_front = ['0', '1', '2', '+', '2', '+', '0', '-', '0', '1', '+', '2', '0', '4', '-','0']

    result = getExprResult(input_front)

    assert result == expect_result
# Preparar o teste
# Rodar as asserções
# Verificar o teste
# Fazer novo teste