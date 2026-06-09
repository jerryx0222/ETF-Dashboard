from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.http import HttpResponse
import os


def serve_spa(request, *args, **kwargs):
    index_file = os.path.join(settings.BASE_DIR, 'frontend_build', 'index.html')
    try:
        with open(index_file, 'rb') as f:
            return HttpResponse(f.read(), content_type='text/html')
    except FileNotFoundError:
        return HttpResponse('Frontend not available', status=404)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),
    path('api/', include('etf.urls')),
    re_path(r'^.*$', serve_spa),
]
