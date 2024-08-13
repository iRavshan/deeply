from typing import List
from uuid import UUID
from abstract_repositories import AbstractArticleRepository
from ..models import Article

class ArticleRepository(AbstractArticleRepository):
    
    def get_by_id(self, id: UUID) -> Article:
        return super().get_by_id(id)
    
    def get_list(self) -> List[Article]:
        return super().get_list()
    
    def create(self, **kwargs) -> Article:
        return super().create(**kwargs)
    
    def update(self, id: UUID, **kwargs) -> Article:
        return super().update(id, **kwargs)
    
    def delete(self, id: UUID) -> None:
        return super().delete(id)