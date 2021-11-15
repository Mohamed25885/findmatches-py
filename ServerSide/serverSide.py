from typing import Any, Dict
from fastapi import FastAPI, Request, Response
from Score import Score

app = FastAPI()


@app.get("/{level}")
async def root(level:int,req:Request, res:Response):    
    return Score.getLevel(level)

@app.post("/")
async def store(data: Dict[str, Any],req:Request, res:Response):
    try:
        Score.storeScore(data)
        return "Score Stored Succesfully"
    except Exception as e:
        res.status_code = 404
        return e
    