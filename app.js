/*
    TO DO:

    VALIDAÇÕES:
        DONE - 1 character por caixa
        DONE - Caracterer deve ser APENAS:
            número
            operadores: *, /, +, -
        DONE - OPERADOR:
            Não pode estar no início ou no fim
            Devem sempre estar entre números
        
*/

function eventHandlerKeyPress(next, all)
{
    return (
    function (event) {
        if (event.keyCode === 13 && event.target.value === "") {
            document.getElementById("spnError").innerHTML = "Digite alguma coisas na caixinha!"
        }
        else if (event.keyCode === 13) {
            document.getElementById("spnError").innerHTML = ""
            if (next !== undefined)
            {
                document.getElementById(next).focus();
            }
            else {
                for (let i = 0; i < all.length; i++)
                {
                    if (all[i].value === "")
                    {
                        document.getElementById("spnError").innerHTML = "Missing Value";
                        return(1);
                    }
                }
                document.getElementById("spnError").innerHTML = "OK";
            }
        }
    })
}

function eventHandlerInput(inputs, i)
{
    return (
        function (event) {
            const validNumbers = ["0", "1", "2", "3", "4", "5", "7", "8", "9"]
            const validOperators = ["*", "/", "-", "+"]
            if (!validNumbers.includes(inputs[i].value) && !validOperators.includes(inputs[i].value))
            {
                inputs[i].value = "";
                return(1);
            }
            if (((i === 0 || i === 5) && validOperators.includes(inputs[i].value)))
            {
                inputs[i].value = "";
                return(1);
            }
            if (i !== 0 && i !== 5)
            {
                if (validOperators.includes(event.target.value) &&
                    (validOperators.includes(inputs[i-1].value) || validOperators.includes(inputs[i+1].value)))
                {
                    inputs[i].value = "";
                }
            }
        }
    )
}

function hello()
{
    const ids = ["inpPrimeiro", "inpSegundo", "inpTerceiro", "inpQuarto", "inpQuinto", "inpSexto"]
    const inputs = []

    for (let i = 0; i < ids.length; i++)
    {
        inputs.push(document.getElementById(ids[i]))
        inputs[i].addEventListener("input", eventHandlerInput(inputs, i))
        inputs[i].addEventListener("keydown", eventHandlerKeyPress(ids[i + 1], inputs))
    }
}

hello()







