from fastapi import FastAPI, Request, Response

app = FastAPI()


@app.post("/")
async def root(req:Request, res:Response):
    pass