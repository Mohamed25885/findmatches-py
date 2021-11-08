from fastapi import FastAPI, Request, Response
import DB.dbAccessLayer as dbAccessLayer

app = FastAPI()


@app.get("/{level}")
async def root(level:int,req:Request, res:Response):
    if level is not int:
        res.status_code = 404
        res.body = "level must be an integer value"
        return res
    else:
        return dbAccessLayer.getLevel(level)