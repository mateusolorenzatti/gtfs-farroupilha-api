from fastapi import FastAPI
import uvicorn

from database.db import database, engine, metadata

from objects.routes import router as routes

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(routes.router, prefix="/routes", tags=["routes"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)