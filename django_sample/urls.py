"""
URL configuration for Django Revolution tests.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django_revolution import add_revolution_urls, get_revolution_urls_info
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # Root redirect
    path(
        "", RedirectView.as_view(url="/schema/public/schema/swagger/", permanent=False)
    ),
]

# Add Django Revolution URL patterns automatically
# This creates:
# - /schema/public/schema/ (OpenAPI spec)
# - /schema/public/schema/swagger/ (Swagger UI)
# - /schema/public/redoc/ (Redoc UI)
# - /schema/private/schema/ (OpenAPI spec)
# - /schema/private/schema/swagger/ (Swagger UI)
# - /schema/private/redoc/ (Redoc UI)
# - /api/public/ (Public API endpoints)
# - /api/private/ (Private API endpoints)
# - /openapi/archive/latest/public.zip (Generated clients)
#
# Auto-generation command:
# poetry run python manage.py auto_generate

urlpatterns = add_revolution_urls(urlpatterns)

# Add static files serving for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Media files serving (both dev and prod)
urlpatterns += [
    path("media/<path:path>", serve, {"document_root": settings.MEDIA_ROOT}),
]

# OpenAPI archives serving
urlpatterns += [
    path(
        "openapi/archive/latest/<path:path>",
        serve,
        {"document_root": str(settings.BASE_DIR / "openapi/archive/latest")},
        name="openapi-archive-latest",
    ),
]

# Print Revolution URL info
revolution_info = get_revolution_urls_info()
if revolution_info:
    print("=" * 60)
    print("🚀 Django Revolution URL Integration")
    print(f"📦 Version: {revolution_info.get('version', 'unknown')}")
    print(f"📊 Zones: {revolution_info.get('total_zones', 0)}")
    print(f"📱 Apps: {revolution_info.get('total_apps', 0)}")
    print(f"🔗 API Prefix: /{revolution_info.get('api_prefix', 'apix')}/")
    print("=" * 60)
