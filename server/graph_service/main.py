from contextlib import asynccontextmanager
import socket
from time import time
from urllib.parse import urlparse

from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse

from graph_service.config import get_settings
from graph_service.custom_graphiti import initialize_graphiti
from graph_service.routers import ingest, retrieve


@asynccontextmanager
async def lifespan(_: FastAPI):
    settings = get_settings()
    await initialize_graphiti(settings)
    yield
    # Shutdown
    # No need to close Graphiti here, as it's handled per-request


app = FastAPI(lifespan=lifespan)
START_TIME = time()


app.include_router(retrieve.router)
app.include_router(ingest.router)


@app.get('/healthcheck')
async def healthcheck():
    return JSONResponse(
        content={
            'status': 'healthy',
            'service': 'graphiti-custom-server',
            'uptime_seconds': round(time() - START_TIME, 3),
        },
        status_code=200,
    )


@app.get('/live')
async def live():
    return JSONResponse(
        content={
            'status': 'alive',
            'service': 'graphiti-custom-server',
            'uptime_seconds': round(time() - START_TIME, 3),
        },
        status_code=200,
    )


@app.get('/ready')
async def ready():
    try:
        settings = get_settings()
        parsed = urlparse(settings.neo4j_uri)
        host = parsed.hostname or 'localhost'
        port = parsed.port or 7687
        with socket.create_connection((host, port), timeout=2):
            pass
        return JSONResponse(
            content={
                'status': 'ready',
                'service': 'graphiti-custom-server',
                'database_uri': settings.neo4j_uri,
                'uptime_seconds': round(time() - START_TIME, 3),
            },
            status_code=200,
        )
    except Exception as exc:
        return JSONResponse(
            content={
                'status': 'not_ready',
                'service': 'graphiti-custom-server',
                'reason': str(exc),
                'uptime_seconds': round(time() - START_TIME, 3),
            },
            status_code=503,
        )


@app.get('/metrics')
async def metrics():
    uptime = round(time() - START_TIME, 3)
    body = '\n'.join(
        [
            '# HELP graphiti_custom_server_up Service readiness flag',
            '# TYPE graphiti_custom_server_up gauge',
            'graphiti_custom_server_up 1',
            '# HELP graphiti_custom_server_uptime_seconds Process uptime in seconds',
            '# TYPE graphiti_custom_server_uptime_seconds gauge',
            f'graphiti_custom_server_uptime_seconds {uptime}',
        ]
    )
    return PlainTextResponse(body + '\n')
