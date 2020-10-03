
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

home = APIRouter()

@home.get("/")
def go_docs():
    """
    Redicionar para /docs
    """
    return RedirectResponse("/docs")