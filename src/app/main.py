from fastapi import FastAPI
import uvicorn

from database.access_control import db_access_control

from core.config import settings

from objects.routes import router as routes
from objects.agency import router as agencies
from objects.shapes import router as shapes

app = FastAPI(
    title=settings.PROJECT_NAME
)

app = db_access_control(app) # Adiciona enventos de inicialização e fechamento do banco

app.include_router(routes.router, prefix="/routes", tags=["routes"])
app.include_router(agencies.router, prefix="/agency", tags=["agency"])
app.include_router(shapes.router, prefix="/shapes", tags=["shapes"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)