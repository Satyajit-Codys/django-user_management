from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve

urlpatterns = [
    url(r"^", include("users.urls")),
    url(r"^admin/", admin.site.urls),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]