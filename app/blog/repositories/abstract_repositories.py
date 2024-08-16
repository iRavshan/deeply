from abc import abstractmethod
from typing import List
from uuid import UUID
from common.repositories import AbstractBaseRepository
from ..models import Article, Tag

class AbstractArticleRepository(AbstractBaseRepository[Article]):
    
    @abstractmethod
    def get_by_slug(self, slug: str) -> Article:
        pass

    @abstractmethod
    def get_by_tag(self, tag_slug: str) -> List[Article]:
        pass

    @abstractmethod
    def get_most_read(self, n: int) -> List[Article]:
        pass

class AbstractTagRepository(AbstractBaseRepository[Tag]):
    
    @abstractmethod
    def get_by_slug(self, tag_slug: str) -> Tag:
        pass