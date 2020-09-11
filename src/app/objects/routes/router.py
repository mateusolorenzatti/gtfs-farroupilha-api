from fastapi import APIRouter, HTTPException, Path

router = APIRouter()

@router.get("/")
async def all_routes():
    
    return { 'routes': ['Nada por enquanto'] }

@router.post("/teste")
async def post_teste():
    
    return { 'teste': ['Nada por enquanto'] }

@router.delete("/teste")
async def delete_teste():
    
    return { 'teste': ['Nada por enquanto'] }