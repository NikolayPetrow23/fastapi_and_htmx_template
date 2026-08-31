from fastapi import APIRouter, Request

from src.base_jinja import templates

router = APIRouter(prefix="/users", tags=["Web users"])

@router.get("/list")
async def users_list(request: Request):
    ...