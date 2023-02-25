'''Root urls configuration'''

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

from core.openapi import schema_view
from core.views import redirect_to_docs


urlpatterns = [
    path('', redirect_to_docs),
    path('admin/', admin.site.urls),

    # Swagger UI
    re_path(
        r'^docs(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'docs/', 
        schema_view.with_ui('swagger', cache_timeout=0), 
        name='schema-swagger-ui'
    ),
    
    path('api/v1/', include('app.urls')),
    path('api/v1/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
