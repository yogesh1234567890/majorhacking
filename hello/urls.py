from rest_framework import routers
from hello.api import LoginViewSet


router =routers.DefaultRouter()
router.register('api/login',LoginViewSet, 'login')

urlpatterns=router.urls