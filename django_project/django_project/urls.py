from django.conf.urls import url, include
from django.contrib import admin
from djangobin import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'', include('djangobin.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)