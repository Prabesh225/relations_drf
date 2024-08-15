from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from relation import views

router = DefaultRouter()
router.register('singers', views.SingerViewSet, basename='singers')
router.register('songs', views.SongViewSet, basename='songs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # For the React app
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
