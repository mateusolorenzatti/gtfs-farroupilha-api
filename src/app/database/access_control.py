from database.db import database, engine, metadata
from core.config import settings

def db_access_control(app):

    @app.on_event("startup")
    async def startup():
        await database.connect()

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()

    return app