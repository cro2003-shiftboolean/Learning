from fastapi import FastAPI # Importing FastAPI class from fastapi module
import uvicorn
from models import IndianStates, states

app = FastAPI() #Instance Creation

@app.get('/') #Defining Method Type (GET, POTS, PUT DELETE) & url path
async def home():
    return {"msg": "Hello World"}

@app.get('/availaibility/{state}') # An Example where User can select the particular states from enum and then we can return list of cities in that State
async def available_cities(state: IndianStates):
    print(state.value) # It can show value in String
    return {"cities": states[state]}

uvicorn.run(app) #Running Application using uvicorn