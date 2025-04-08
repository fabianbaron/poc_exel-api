from fastapi import FastAPI
from fastapi.responses import JSONResponse
from processes import some_logic
import uvicorn
    
app = FastAPI()

@app.get("/")
def root():
    return JSONResponse(content={"resultado": "Hola mundo"})

@app.post("/some_operation")
def sumar(data: dict):
    resultado = some_logic(data)
    return JSONResponse(content={"resultado": resultado})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
