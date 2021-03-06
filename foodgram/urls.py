from django.conf.urls import handler404, handler500  # noqa
from django.contrib import admin
from django.urls import include, path

from foodgram.views import AboutAuthorView, AboutTechView

urlpatterns = [
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('about/author/', AboutAuthorView.as_view(), name='about-author'),
    path('about/technology/', AboutTechView.as_view(), name='about-tech'),
    path('', include('recipes.urls')),
]

handler404 = 'foodgram.views.page_not_found' # noqa
handler500 = 'foodgram.views.server_error' # noqa
