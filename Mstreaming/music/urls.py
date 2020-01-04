from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib import admin

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'song', views.SongViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
