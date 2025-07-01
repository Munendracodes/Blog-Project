from fastapi import FastAPI
from app.database.connection import engine
from app.models import blog_model, user_model

from app.routes import blog_route, user_route, auth

blog_model.Base.metadata.create_all(bind=engine)



app = FastAPI(
    title="My Blog API",
    description="Custom Blog API with User Auth and CRUD functionality.",
    version="1.0.0",
    docs_url="/docs",           # Change URL or disable with None
    redoc_url="/redoc",         # Optional: another UI
    openapi_url="/openapi.json" # Change or disable schema generation
    )

app.include_router(auth.router)
app.include_router(user_route.router)
app.include_router(blog_route.router)


