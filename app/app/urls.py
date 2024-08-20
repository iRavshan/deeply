from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import ArticleSitemap
from courses.sitemaps import TopicSitemap
from . import views

sitemaps = {
    'articles': ArticleSitemap,
    'topics': TopicSitemap
}

urlpatterns = i18n_patterns(
    path(_('adminim/'), admin.site.urls),
    path(_('courses/'), include('courses.urls')),
    path(_('blog/'), include('blog.urls')),
    path(_('user/'), include('users.urls')),
    path(_('django-check-seo/'), include('django_check_seo.urls')),
    path(_(''), views.home, name='home'),
    path(_('guide'), views.guide, name='guide'),
    path(_('robots.txt'), views.robots_txt, name='robotsTxt'),
    path(_('sitemap.xml'), 
         sitemap, 
         {'sitemaps': sitemaps}, 
         name='django.contrib.sitemaps.views.sitemap'),
)

handler404 = views.error_404
handler500 = views.error_500
handler403 = views.error_403
handler400 = views.error_400

admin.site.site_title = "TicketsPlus site admin (DEV)"
admin.site.site_header = "TicketsPlus administration"
admin.site.index_title = "Site administration"