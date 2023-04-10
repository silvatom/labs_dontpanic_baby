from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
async def main():
    return FileResponse("static/index.html")

class Elements(BaseModel):
    equation:list

@app.post("/hahaha")
async def post_method(elements: Elements):
    print(elements)
    return {"Hello":"ola"}
