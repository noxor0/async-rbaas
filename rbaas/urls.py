from django.urls import include, path
from rest_framework import routers
from rbaas.boss import views

router = routers.DefaultRouter()
router.register(r'boss/', views.BossViewSet)
router.register(r'boss', views.BossViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]