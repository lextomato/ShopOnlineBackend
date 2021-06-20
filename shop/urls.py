from django.contrib import admin
from django.urls import include, path

# We import Django REST Framework and the views 'Product' and 'Category'
from rest_framework import routers
from product import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'search', views.FilterViewSet)
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
