from django.urls import path,include
from spam.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('contact',ContactAPIView)

urlpatterns = [
    path('',include(router.urls)),
]