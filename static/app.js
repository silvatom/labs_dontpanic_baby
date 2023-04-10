baseUrl = "http://127.0.0.1:8000/"

// Get expression from html components (attempt)
function getExpressionAttempt()
{
    let elements = document.getElementsByClassName("elements");
    let expression = []
    for (let i = 0; i < elements.length; i++)
    {
        expression.push(elements[i].value);
    }
    return (expression)
}

function performFetch(all, attempt)
{
    const valuesJSON = JSON.stringify({
        equation: exprAttempt
    });
    return fetch(baseUrl + "getHints", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: valuesJSON
    }).then((res) => {
        return(res.json());
    });
}

function insertHintIntoFront(hints)
{
    let hintContainer = document.getElementsByClassName('hints');
    for (let i = 0; i < hints.length; i++)
    {
        hintContainer[i].value = hints[i].toUpperCase();
    }
}

function eventHandlerKeyPress(next, all)
{
    return (
    async function (event) {
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
                exprAttempt = getExpressionAttempt();

                hints = await performFetch(all, exprAttempt);
                // inserir as hints nos componentes do front
                insertHintIntoFront(hints.hints);
                // colocar expAttempt nos input de cima
            }
        }
    })
    
}

function eventHandlerInput(inputs, i)
{
    return (
        function (event) {
            const validNumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
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

function setEvents()
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

setEvents();






