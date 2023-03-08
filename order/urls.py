from rest_framework.routers import DefaultRouter 
from django.urls import path,include
from order.views import OrderModelViewSet,OrderConfirmAPIView

router = DefaultRouter()
router.register('',OrderModelViewSet)

urlpatterns = [
    path('confirm/<uuid:code>/',OrderConfirmAPIView.as_view()),
    path('',include(router.urls))
]