from typing import List
from uuid import UUID
from django.shortcuts import get_object_or_404
from .abstract_repositories import AbstractArticleRepository, AbstractTagRepository
from ..models import Article, Tag

class TagRepository(AbstractTagRepository):

    def get_by_id(self, id: int | UUID) -> Tag:
        return super().get_by_id(id)
    
    def get_by_slug(self, tag_slug: str) -> Tag:
        return Tag.objects.get(slug=tag_slug)

    def get_list(self) -> List[Tag]:
        return Tag.objects.all()
    
    def create(self, **kwargs) -> Tag:
        return super().create(**kwargs)
    
    def update(self, id: int | UUID, **kwargs) -> Tag:
        return super().update(id, **kwargs)
    
    def delete(self, id: int | UUID) -> None:
        return super().delete(id)
    

class ArticleRepository(AbstractArticleRepository):
    
    def get_by_id(self, id: UUID) -> Article:
        return super().get_by_id(id)
    
    def get_by_slug(self, slug: str) -> Article:
        article = Article.objects.get(slug=slug)
        return article
    
    def get_list(self) -> List[Article]:
        return Article.objects.all()
    
    def get_by_tag(self, tag_slug: str) -> List[Article]:
        return Article.objects.filter(tags__slug=tag_slug)
    
    def get_most_read(self, n: int) -> List[Article]:
        most_viewed_articles = Article.objects.order_by('-views')[:n]
        return most_viewed_articles

    
    def create(self, **kwargs) -> Article:
        return super().create(**kwargs)
    
    def update(self, id: UUID, **kwargs) -> Article:
        return super().update(id, **kwargs)
    
    def delete(self, id: UUID) -> None:
        return super().delete(id)