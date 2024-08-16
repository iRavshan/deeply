from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from . import views

urlpatterns = i18n_patterns(
    path(_('adminim/'), admin.site.urls),
    path(_('courses/'), include('courses.urls')),
    path(_('blog/'), include('blog.urls')),
    path(_('user/'), include('users.urls')),
    path(_(''), views.home, name='home'),
    path(_(r'guide'), views.guide, name='guide')
)

handler404 = views.error_404
handler500 = views.error_500
handler403 = views.error_403
handler400 = views.error_400