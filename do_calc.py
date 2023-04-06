# FUNÇÃO(expr.) -> retorna TRUE_FALSE 
# 	calcular espressão (parametro) -> resultado
# 		performa calculo******************
# 		    verifica precedencia

def do_calc(equation_elements: list) -> int:
    inp_str = ''.join(equation_elements)
    return (eval(inp_str))

def is_42(number: int) -> bool:
	return (number == 42)

def is_expected_equation(inp_equation: list, exp_equation: list) -> bool:
    elements_str = ''.join(inp_equation)
    equation_str = ''.join(exp_equation)

    return elements_str == equation_str
    

def check_elems(inp_equation: list, exp_equation: list) -> list:
    # if (len(inp_equation) != len(exp_equation)):
    #     return []
    result = []
    loop_size = len(inp_equation)
    
    for i in range(loop_size):
        if (inp_equation[i] == exp_equation[i]):
            result.append("c")
        else:
            if inp_equation[i] in exp_equation:
                result.append("t")
            else:
                result.append("x")
    return (result)
