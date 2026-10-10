import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.config import STATIC_DIR
from app.routes import health, pages

logger = logging.getLogger(__name__)

app = FastAPI(title="Team and Guide Allocation")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
app.include_router(health.router)
app.include_router(pages.router)


@app.exception_handler(Exception)
async def handle_unexpected_error(
    request: Request, exc: Exception
) -> JSONResponse:
    logger.exception("Unhandled error while handling %s", request.url.path)
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred."},
    )
