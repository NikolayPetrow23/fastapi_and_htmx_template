from fastapi import APIRouter

from src.users import api_user_router, web_user_router


api_router = APIRouter(prefix="/api/v1")
web_router = APIRouter(prefix="")

# API Router
api_router.include_router(api_user_router)

# Web Router
web_router.include_router(web_user_router)