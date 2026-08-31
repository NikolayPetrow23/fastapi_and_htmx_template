import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.router import api_router, web_router
from src.web.routes import router_pages

# from sqladmin import Admin
# from src.admin.view import UsersAdmin
# from src.admin.auth import authentication_backend
# from src.database import engine

app = FastAPI(
    title="Template",
    version="0.0.1",
    # docs_url=None,    # Отключить Swagger UI
    # redoc_url=None,   # Отключить ReDoc
    # openapi_url=None  # Отключить OpenAPI JSON
)

app.mount(
    "/static",
    StaticFiles(directory="src/web/static"),
    name="static",
)

# API
app.include_router(api_router)

# Web router fragmetnts HTMX
app.include_router(web_router)

# Web Pages
app.include_router(router_pages)

# Admin Panel
# admin = Admin(app, engine, authentication_backend=authentication_backend)
# admin.add_view(UsersAdmin)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
