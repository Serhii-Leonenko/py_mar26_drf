from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

api_v1_patterns = [
    path("", include("users.urls")),
    path("", include("messenger.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/", include(api_v1_patterns)),
] + debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
