from django.conf.urls import url
from rest_framework import routers

from .views import GenerateOTP, ValidateOTP, UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^generateToken$', GenerateOTP.as_view(), name="generate"),
    url(r'^validateToken$', ValidateOTP.as_view(), name="validate"),
]

urlpatterns += router.urls