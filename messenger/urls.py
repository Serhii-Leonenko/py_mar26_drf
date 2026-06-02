from django.urls import path
from rest_framework.routers import DefaultRouter

from messenger.views import MessageViewSet

app_name = "messenger"

# urlpatterns = [
#     path("messages/", MessageView.as_view(), name="message-list"),
#     path("tags/", TagView.as_view(), name="tag-list"),
# ]

router = DefaultRouter()
router.register("messages", MessageViewSet)

urlpatterns = router.urls
