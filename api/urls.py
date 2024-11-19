from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'progamer', views.ProgamerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]