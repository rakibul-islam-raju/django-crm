from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from leads.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    # landing page from leads app
    path('', LandingPageView.as_view(), name='landing-page'),

    path('leads/', include('leads.urls', namespace='lead')),
    path('', include('agents.urls', namespace='agent')),
    path('auth/', include('authentication.urls', namespace='auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
