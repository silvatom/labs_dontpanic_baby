# FUNÇÃO(expr.) -> retorna TRUE_FALSE 
# 	calcular espressão (parametro) -> resultado
# 		performa calculo******************
# 		    verifica precedencia

rightExpression = ["1","*","2","+","4","0"]

def getExprResult(equation_elements: list) -> int:
    inp_str = ''.join(equation_elements)
    return (eval(inp_str))

def is_42(number: int) -> bool:
	return (number == 42)

def isRightExpression(inp_equation: list, exp_equation: list) -> bool:
    elements_str = ''.join(inp_equation)
    equation_str = ''.join(exp_equation)

    return elements_str == equation_str
    

def check_elems(inp_equation: list, exp_equation: list) -> list:
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

def main_function(exprListGuess: list) -> list:
    result = getExprResult(exprListGuess)
    if (is_42(result) != True):
        return ([]) #só retorna tentativa anterior
    if (isRightExpression(exprListGuess, rightExpression) == True):
        return (["C","C","C","C","C","C"]) # você venceu!
    hintsList = check_elems(exprListGuess, rightExpression)
    return (hintsList)
