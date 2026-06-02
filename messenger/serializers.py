from django.contrib.auth import get_user_model
from rest_framework import serializers

from messenger.models import Message, Tag

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
       model = Message
       fields = (
           "id",
           "created_at",
           "user",
           "text_preview"
       )


# for retrieve action
class MessageDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ("id", "text", "created_at", "user")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")
