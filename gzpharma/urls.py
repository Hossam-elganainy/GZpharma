from django.contrib import admin
from django.urls import path,include
import users.urls as users_urls
import item.urls as item_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="GZPharama API 2f55a714a28f6eaffc579f41b8749b672478c203",
        default_version="v1",
        description="API documentation for the GZPharama project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="GZPharama@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include(users_urls)),
    path('api/items/', include(item_urls)),
    

    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)