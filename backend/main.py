import uvicorn
from fastapi import FastAPI

from backend.controllers import car, driver, ticket, login

app = FastAPI()
app.include_router(car.router)
app.include_router(driver.router)
app.include_router(ticket.router)
app.include_router(login.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
