from fastapi import FastAPI # Importing FastAPI class from fastapi module
import uvicorn
from models import IndianStates, states

app = FastAPI() #Instance Creation

@app.get('/') #Defining Method Type (GET, POTS, PUT DELETE) & url path
async def home():
    return {"msg": "Hello World"}

@app.get('/availaibility/{state}') # An Example where User can select the particular states from enum and then we can return list of cities in that State
async def available_cities(state: IndianStates, offset: int = 0, limit: int = 100): #Tried mimic Pagination where the cities will be shown from offset to next limit values
    """
        Retrieves available cities for a given state with optional pagination.

        Args:
            state: The Indian state to retrieve cities for.
            offset: The starting index for the list of cities. Defaults to 0.
            limit: The maximum number of cities to return. Defaults to 100.

        Returns:
            A dictionary containing the list of cities.
    """
    print(state.value) # It can show value in String
    if offset < 0:
        return {"error": "offset cannot be negative", "success": True}, 400
    if offset < 0:
        return {"error": "offset limit exceeded", "success": True}, 400

    elif offset + limit > len(states[state]):
        return {"cities": states[state][offset:]}
    return {"cities": states[state][offset: offset + limit], "success": True}, 200

uvicorn.run(app) #Running Application using uvicorn