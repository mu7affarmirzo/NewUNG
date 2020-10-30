from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/news/', include('news.urls', 'news_api')),
    path('api/tenders/', include('tenders.urls', 'tenders_api')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)