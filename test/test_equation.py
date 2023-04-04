import pytest

# no maximo: 2 operadores 4 inteiros
# minimo: 1 operador e 5 inteiros 
def test_is_equation_42():
	# arrange
	expected_result = True

	# action
	result = do_calc('8-9*30')

	# assert
	assert result == expected_result


# Preparar o teste
# Rodar as asserções
# Verificar o teste
# Fazer novo teste