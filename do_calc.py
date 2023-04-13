rightExpression = ["8","*","9","-","3","0"]

def getExprResult(equation_elements: list) -> int:
    result_str = ''
    aux = ''
    for elem in equation_elements:
        if elem.isdigit():
            aux += elem
        else:
            result_str += str(int(aux))
            result_str += elem
            aux = ''
    result_str += str(int(aux))
    return (eval(result_str))

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
