from fastapi import FastAPI

from .helpers import get_value_from_db

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/db_test")
async def db_test():
    result = get_value_from_db()

    return {"result": result}
