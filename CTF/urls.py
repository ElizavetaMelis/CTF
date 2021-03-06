from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from CTF import settings

schema_view = get_schema_view(
   openapi.Info(
      title="CTF",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/category/', include('applications.category.urls')),
    path('api/v1/difficulty/', include('applications.difficulty.urls')),
    path('api/v1/task/', include('applications.tasks.urls')),
    path('api/v1/main/', include('applications.main.urls')),
    path('api/v1/testing/', include('applications.testing.urls')),
    path('swagger(json|.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
