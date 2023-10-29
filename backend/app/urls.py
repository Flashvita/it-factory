
from django.contrib import admin
from django.urls import path, include

from app.docs import urlpatterns as docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(docs_urls)),
    path('api/v1/', include("mainapp.urls")),
]

