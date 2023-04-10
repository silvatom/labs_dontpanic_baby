from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from do_calc import main_function

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
async def main():
    return FileResponse("static/index.html")

class Elements(BaseModel):
    equation:list

@app.post("/getHints")
async def post_method(elements: Elements):
    hintsList = main_function(elements.equation)
    return {"hints": hintsList}
