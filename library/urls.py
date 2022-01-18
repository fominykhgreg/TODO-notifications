from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet
from authapp.views import UserModelViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)

router1 = DefaultRouter()
router1.register('authapp', UserModelViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   path('api/', include(router.urls)),
   path('api/', include(router1.urls)),
]

