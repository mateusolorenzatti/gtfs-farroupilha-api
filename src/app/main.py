from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from database.access_control import db_access_control

from core.config import settings
from core.home import home

from objects.agency.router import agencies
from objects.routes.router import routes
from objects.shapes.router import shapes
from objects.stops.router import stops
from objects.trips.router import trips
from objects.stop_times.router import stop_times

#  Cria a API e atribuoi o nome (Será exibido em /docs)
app = FastAPI(
    title=settings.PROJECT_NAME
)

# Adiciona configurações de acesso pelo CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Adiciona enventos de inicialização e fechamento do banco
app = db_access_control(app) 

# Configura oara que a rota raiz seja direcionada para /docs
app.include_router(home, tags=["Home"])

#  Adiciona as rotas dos objects
app.include_router(routes, prefix="/routes", tags=["Routes"])
app.include_router(agencies, prefix="/agency", tags=["Agency"])
app.include_router(shapes, prefix="/shapes", tags=["Shapes"])
app.include_router(stops, prefix="/stops", tags=["Stops"])
app.include_router(trips, prefix="/trips", tags=["Trips"])
app.include_router(stop_times, prefix="/stop_times", tags=["StopTimes"])

#  Opção para rodar automaticamente o servidor local
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)