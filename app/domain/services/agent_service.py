from http import HTTPStatus
from fastapi import UploadFile
from sentence_transformers import SentenceTransformer

from app.domain.services.vectordb_service import VectorDBService
from common.utils.image import create_point_data, detect_confidence_objects
from common.utils.response import error_response
from common.utils.storage import get_sample_image_path
from config.embedding_model import EmbeddingModel


class AgentService():
    def __init__(self):
        self.vectordb_service = VectorDBService()
        pass


    async def handle_image(self, file: UploadFile):
        sample_image_path = get_sample_image_path()
        detected_objects = detect_confidence_objects(sample_image_path)
        point_data = create_point_data(sample_image_path, detected_objects)

        if point_data is None:
            return error_response(HTTPStatus.UNPROCESSABLE_ENTITY, "point_data is None")

        else:
            embedding_model = SentenceTransformer(EmbeddingModel.MODELS['hugging_face']['clip']['ViT-L-14']['name'])
            embedded = embedding_model.encode(point_data['crop'])

        result = await self.vectordb_service.qdrant.find_points(collection_name="fruits", query=embedded, limit=5)

        print(result)