from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from .repositories.repositories import ArticleRepository

articleRepository = ArticleRepository()

class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    i18n = True

    def items(self):
        return articleRepository.get_list()
    
    def lastmod(self, obj):
        return obj.updated_at