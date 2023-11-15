from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.product import product
from routes.user import user
from routes.comments import comments
from starlette.responses import RedirectResponse
from routes.publication import publication

app = FastAPI(
    title="Nissou API",
    description="Simple API made with FastAPI and MongoDB",
    version="1.0.0"
)

# Configuración para permitir todas las solicitudes CORS (debes ajustar según tus necesidades)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes especificar los dominios permitidos en lugar de "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
def index():
    RedirectResponse(url="/docs")

app.include_router(product)
app.include_router(user)
app.include_router(comments)
app.include_router(publication)