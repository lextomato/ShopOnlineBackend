from django.contrib import admin
from django.urls import include, path

# We import Django REST Framework and the views 'Product' and 'Category'
from rest_framework import routers
from product import views

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'search', views.FilterViewSet)
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
]
