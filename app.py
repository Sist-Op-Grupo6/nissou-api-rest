from fastapi import FastAPI
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

@app.get("/", include_in_schema=False)
def index():
    RedirectResponse(url="/docs")

app.include_router(product)
app.include_router(user)
app.include_router(comments)
app.include_router(publication)