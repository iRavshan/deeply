from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from .repositories.repositories import TopicRepository

topicRepository = TopicRepository()

class TopicSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    i18n = True

    def items(self):
        return topicRepository.get_list()
    
    def lastmod(self, obj):
        return obj.updated_at