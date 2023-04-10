baseUrl = "http://127.0.0.1:8000/"
var watcher = 0;

function anyThing(all)
{
    let elements = document.getElementsByClassName("elements");
    let values = []
    for (let i = 0; i < elements.length; i++)
    {
        values.push(elements[i].value);
    }

    const valuesJSON = JSON.stringify({
        equation: values
    });
    //console.log(valuesJSON);
    return fetch(baseUrl + "hahaha", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: valuesJSON
    }).then((res) => {
        console.log(res.json())
        console.log(res)
        // return (res.json());
    });
} 

function eventHandlerKeyPress(next, all)
{
    ++watcher;
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
                anyThing(all);
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
    //TODO:
        // construir a lista com a "tentativa"
        // loop dos componentes
}

hello();
/**
function setHints(hints) {
  const tiles = document.getElementsByClassName("hint");
  for (let i = 0; i < tiles.length; i++) {
    const tile = tiles[i];
    tile.textContent = hints[i];
    setHintColor(tile);
  }
}
*/








