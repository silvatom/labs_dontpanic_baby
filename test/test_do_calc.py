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


# Preparar o teste
# Rodar as asserções
# Verificar o teste
# Fazer novo teste