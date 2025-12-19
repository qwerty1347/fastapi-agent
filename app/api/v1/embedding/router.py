from fastapi import APIRouter

from app.domain.services.vectordb_service import VectorDBService


router = APIRouter(prefix="/embedding", tags=["VectorDB"])
vectordb_service = VectorDBService()


@router.get('/images')
async def index():
    result = await vectordb_service.handle_fruits_images()

    return {"message": "Hello Embedding"}