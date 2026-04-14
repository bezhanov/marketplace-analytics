import uvicorn
from fastapi import FastAPI

from app.routers.wildberries import router as wildberries_router
from app.core.config import settings

app = FastAPI(title=settings.app_name)

app.include_router(wildberries_router)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.host, port=settings.port)
