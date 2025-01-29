from fastapi import FastAPI
import models
import database
import uvicorn

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)