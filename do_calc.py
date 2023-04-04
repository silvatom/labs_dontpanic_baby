import re

def verify_precedence(operators: list):
	if (operators[0] == '-' or operators[0] == '+'):
		if (operators[1] == '*' or operators[1] == '/'):
			operators[0], operators[1] = operators[1], operators[0]

# USAR O EXEMPLO ABAIXO PARA O TESTE BASICO
# (8, "*", 9, "-", 3, 0)
# "8*9-30"
# "8, 9, 30"
# "*, -"
def do_calc(elementos_equacao: str) -> bool:
	# return True
	list_numb = re.split('(\*|-|\+|/)', elementos_equacao)
	list_size = len(list_numb)
	if (list_size == 5):
		operators = [list_numb[1], list_numb[3]]
		verify_precedence(operators)
		# pro caso de inverter os operadores, precisamos
		# inverter os numeros (caso o verify retorne 1)		

do_calc('8-9*30')
# arr = [1, 2, 3, 4, 5, 10, 200]
# arr[2:5]

# op1 = -
# op = *

# --> qual dos dois tem precedencia?
