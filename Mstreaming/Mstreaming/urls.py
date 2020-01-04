from django.urls import path, include

urlpatterns = [
    path('', include('music.urls')),
    path('api-auth/', include('rest_framework.urls')),
]