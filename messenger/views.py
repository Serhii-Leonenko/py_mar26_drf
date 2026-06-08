from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, filters
from django_filters import rest_framework as drf_filters
from rest_framework.decorators import action
from rest_framework.response import Response

from messenger.filters import MessageFilter
from messenger.models import Message
from messenger.serializers import (
    MessageListSerializer,
    MessageDetailSerializer,
    MessageSerializer
)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.select_related(
        "user"
    ).prefetch_related(
        "liked_by",
        "tags"
    )
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

        if self.action == "like":
            return MessageListSerializer

        return MessageSerializer

    @extend_schema(
        request=None,
        responses={200: MessageListSerializer},
    )
    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        message = self.get_object()

        user = self.request.user
        if user in message.liked_by.all():
            message.liked_by.remove(user)
        else:
            message.liked_by.add(user)

        message.refresh_from_db(fields=["liked_by"])

        serializer = self.get_serializer(message)

        return Response(serializer.data)
