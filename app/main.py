import dotenv

dotenv.load_dotenv()

import uvicorn
import logging
from fastapi import FastAPI
from app.routers import wildberries, users
from app.routers.wildberries import router as wildberries_router
from app.core.config import settings
from contextlib import asynccontextmanager
from app.database.engine import create_db_and_tables


@asynccontextmanager
async def lifespan(_: FastAPI):
    logging.warning("On startup")
    create_db_and_tables()
    yield
    logging.warning("On shutdown")


app = FastAPI(title=settings.app_name, lifespan=lifespan)

app.include_router(wildberries.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.host, port=settings.port)
