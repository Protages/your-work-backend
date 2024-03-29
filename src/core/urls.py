'''Root urls configuration'''

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
    path('__debug__/', include('debug_toolbar.urls')),
]

# To handle media paths
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# To handle static paths (if DEBUG=False it doesn't work)
urlpatterns += staticfiles_urlpatterns()
