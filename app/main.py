from fastapi import FastAPI

from app.api.routes import router as api_router
from app.views.routes import router as view_router
from app.infra.database import init_db

app = FastAPI()
app.include_router(api_router, prefix="/api")
app.include_router(view_router)


@app.on_event("startup")
def on_startup() -> None:
    init_db()
