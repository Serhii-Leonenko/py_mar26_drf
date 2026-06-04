from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from users.views import UserViewSet

app_name = 'users'

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = router.urls
urlpatterns += [
    path("token/", views.obtain_auth_token, name="token")
]
