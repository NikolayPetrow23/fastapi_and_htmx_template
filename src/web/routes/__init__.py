from fastapi import APIRouter

from src.web.routes.pages import router


router_pages = APIRouter(prefix="", tags=["Web Pages"])

router_pages.include_router(router)
