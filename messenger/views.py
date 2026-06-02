from rest_framework import  viewsets

from messenger.models import Message
from messenger.serializers import MessageSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
