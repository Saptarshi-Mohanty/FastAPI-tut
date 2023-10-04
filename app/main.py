from fastapi import FastAPI

app = FastAPI()

@app.get("/", description="first get route", deprecated=True)
async def root():
    return {"message": "hello world"}

@app.post("/")
async def post():
    return {"message": "hello world from post request"}
