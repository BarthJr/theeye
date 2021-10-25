from django.urls import include, path
from rest_framework import routers

from .views import EventViewSet, EventErrorViewSet

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'errors', EventErrorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
