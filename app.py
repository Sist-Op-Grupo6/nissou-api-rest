from fastapi import FastAPI
from routes.product import product
from routes.user import user
from routes.publication import publication
from starlette.responses import RedirectResponse

app = FastAPI(
    title="Nissou API",
    description="Simple API made with FastAPI and MongoDB",
    version="1.0.0"
)

@app.get("/", include_in_schema=False)
def index():
    RedirectResponse(url="/docs")

app.include_router(product)
app.include_router(publication)
app.include_router(user)