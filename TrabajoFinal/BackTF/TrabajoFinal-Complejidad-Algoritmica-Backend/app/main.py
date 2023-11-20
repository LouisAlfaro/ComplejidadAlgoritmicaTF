from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.routers import graph_route, index


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],  # O especifica los orígenes permitidos en lugar de "*", como ["http://localhost", "https://tu-sitio.com"]
    allow_credentials=True,
    allow_methods=[
        "*"
    ],  # O especifica los métodos permitidos, como ["GET", "POST", "OPTIONS"]
    allow_headers=["*"],  # O especifica los encabezados permitidos
)


@app.get("/")
async def root():
    """
    Redirect to /docs.
    """
    return RedirectResponse(url="/docs")


app.include_router(index.router)
app.include_router(graph_route.router)
