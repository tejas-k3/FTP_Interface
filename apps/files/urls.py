from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import include
from django.conf import settings
from . import views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"file", views.FileViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
