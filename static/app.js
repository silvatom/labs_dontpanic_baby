baseUrl = "http://labs-cidadao-do-mundo.42sp.org.br:5015/"

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

function performFetch(attempt)
{
    const values_JSON = JSON.stringify({
        equation: attempt
    });
    return fetch(baseUrl + "getHints", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: values_JSON
    }).then((res) => {
        return(res.json());
    });
}

function insertHintIntoFront(hints)
{
    let hint_container = document.getElementsByClassName('hints');
    if (hints.length === 0)
        document.getElementById("spnError").innerHTML = "Expressão inválida!";
    for (let i = 0; i < hint_container.length; i++)
    {
        if (hints.length === 0)
            hint_container[i].value = ""
        else
            hint_container[i].value = hints[i].toUpperCase();
    }
}

function insertLastAttempIntoFront(attempt)
{   
    let attempt_box = document.getElementsByClassName('last-expr')
    for (let i = 0; i < attempt_box.length; i++)
    {
        attempt_box[i].value = attempt[i];
    }
}

function cleanInputs(all)
{
    for (let i = 0; i < all.length; i++)
    {
        all[i].value = "";
    }
    all[0].focus();
}

function eventHandlerKeyPress(all, index, next)
{
    return (
    async function (event) {
        if (event.keyCode === 8 && index > 0) {
            if (all[index].value === ""){
                all[index - 1].value = "";
                all[index - 1].focus();
            }
            all[index].value = "";
        }
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
                        document.getElementById("spnError").innerHTML = "Digite alguma coisas na caixinha!";
                        return(1);
                    }
                }
                expr_attempt = getExpressionAttempt();
                hints = await performFetch(expr_attempt);
                insertHintIntoFront(hints.hints);
                insertLastAttempIntoFront(expr_attempt);
                cleanInputs(all);
                count = 0;
                for (i = 0; i < hints.hints.length; i++)
                {
                    if (hints.hints[i].toUpperCase() === "C")
                        count++;
                }
                if (count === 6)
                {
                    alert("Parabéns!!!")
                }
            }
        }
    })
}

function eventHandlerInput(inputs, i, all)
{
    return (
        function (event) {
            const valid_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            const valid_operators = ["*", "/", "-", "+"]
            if (!valid_numbers.includes(inputs[i].value) && !valid_operators.includes(inputs[i].value))
            {
                inputs[i].value = "";
                return(1);
            }
            if (((i === 0 || i === 5) && valid_operators.includes(inputs[i].value)))
            {
                inputs[i].value = "";
                return(1);
            }
            if (i !== 0 && i !== 5)
            {
                if (valid_operators.includes(event.target.value) &&
                    (valid_operators.includes(inputs[i-1].value) || valid_operators.includes(inputs[i+1].value)))
                {
                    inputs[i].value = "";
                    return(1);
                }
            }
            if (inputs[i + 1] !== undefined)
                inputs[i + 1].focus();
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
        inputs[i].addEventListener("input", eventHandlerInput(inputs, i, ids))
        inputs[i].addEventListener("keydown", eventHandlerKeyPress(inputs, i, ids[i + 1]))
    }
}

setEvents();