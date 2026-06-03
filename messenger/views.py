from rest_framework import  viewsets

from messenger.models import Message
from messenger.serializers import MessageListSerializer, MessageDetailSerializer, MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.select_related("user")

    def get_serializer_class(self):
        if self.action == "list":
            return MessageListSerializer

        if self.action == "retrieve":
            return MessageDetailSerializer

        return MessageSerializer
