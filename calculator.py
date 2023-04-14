right_expression = ["8","*","9","-","3","0"]

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

def isRightExpression(inp_equation: list, exp_equation: list) -> bool:
    elements_str = ''.join(inp_equation)
    equation_str = ''.join(exp_equation)

    return elements_str == equation_str

def checkElems(inp_equation: list, exp_equation: list) -> list:
    result = []
    loop_size = len(inp_equation)
    
    for i in range(loop_size):
        if (inp_equation[i] == exp_equation[i]):
            result.append("C")
        else:
            if inp_equation[i] in exp_equation:
                result.append("T")
            else:
                result.append("X")
    return (result)

def main_function(expr_list_guess: list) -> list:
    result = getExprResult(expr_list_guess)
    if (result != 42):
        return ([]) #só retorna tentativa anterior
    if (isRightExpression(expr_list_guess, right_expression) == True):
        return (["C","C","C","C","C","C"]) # você venceu!
    hints_list = checkElems(expr_list_guess, right_expression)
    return (hints_list)
