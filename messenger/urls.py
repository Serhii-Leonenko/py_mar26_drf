from rest_framework.routers import DefaultRouter

from messenger.views import MessageViewSet

app_name = "messenger"


router = DefaultRouter()
router.register("messages", MessageViewSet)

urlpatterns = router.urls
