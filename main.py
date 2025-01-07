from fastapi import FastAPI # Importing FastAPI class from fastapi module
import uvicorn

app = FastAPI() #Instance Creation

@app.get('/') #Defining Method Type (GET, POTS, PUT DELETE) & url path
async def home():
    return {"msg": "Hello World"}

uvicorn.run(app) #Running Application using uvicorn