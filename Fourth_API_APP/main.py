from fastapi import FastAPI
from routes.v1.task_routes import router as v1_router
from routes.v2.task_routes import router as v2_router

app = FastAPI(
    title="Task Management API",
    version="1.0",
    description="API for managing tasks with versioning and dependency injection"
)

app.include_router(v1_router)
app.include_router(v2_router)