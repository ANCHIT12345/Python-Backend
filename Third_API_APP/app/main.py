from fastapi import FastAPI, Request
from app.routes.access_routes import router
from app.config import APP_NAME, APP_VERSION, APP_ENV
from app.utils.logger import log_request   # ← THIS WAS MISSING

app = FastAPI(title=APP_NAME, version=APP_VERSION)

app.include_router(router)

# Middleware to log all requests
@app.middleware("http")
async def request_logger(request: Request, call_next):

    response = await call_next(request)

    log_request(
        endpoint=request.url.path,
        method=request.method,
        status=response.status_code
    )

    return response


# Debug endpoint only for dev
if APP_ENV != "prod":

    @app.get("/debug")
    def debug():
        return {"env": APP_ENV, "message": "Debug endpoint active"}