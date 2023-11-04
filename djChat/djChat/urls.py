from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    # drf-spectacular & Swagger
    path('api/docs/schema/', SpectacularAPIView.as_view(), name='schema'),  # to download schema
    path('api/docs/schema/ui/', SpectacularSwaggerView.as_view()),
]
