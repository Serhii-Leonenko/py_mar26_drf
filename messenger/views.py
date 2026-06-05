from rest_framework import viewsets, filters
from django_filters import rest_framework as drf_filters

from messenger.filters import MessageFilter
from messenger.models import Message
from messenger.serializers import (
    MessageListSerializer,
    MessageDetailSerializer,
    MessageSerializer
)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.select_related("user")
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        drf_filters.DjangoFilterBackend
    ]
    search_fields = ["text", "tags__name", "user__username"]
    ordering_fields = ["created_at"]
    filterset_class = MessageFilter
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return MessageListSerializer

        if self.action == "retrieve":
            return MessageDetailSerializer

        return MessageSerializer
