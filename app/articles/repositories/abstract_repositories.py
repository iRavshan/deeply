from common.repositories import AbstractBaseRepository
from ..models import Article

class AbstractArticleRepository(AbstractBaseRepository[Article]):
    pass