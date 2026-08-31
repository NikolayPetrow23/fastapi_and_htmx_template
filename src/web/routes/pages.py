from fastapi import Request
from fastapi import APIRouter

from src.base_jinja import templates

router = APIRouter(prefix="", tags=["Web Pages"])


@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/index.html",
    )
