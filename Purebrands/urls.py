"""Purebrands URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('accounts.urls'))
]

if settings.DEBUG:
    # serve media
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    from django.views.generic import RedirectView
    from .swagger import drf_yasg_swagger_view

    urlpatterns += [
        path('', RedirectView.as_view(url='api/swagger', permanent=True)),
        path('api/swagger', drf_yasg_swagger_view.with_ui('swagger', cache_timeout=0), name='drf_yasg_swagger_view'),

    ]