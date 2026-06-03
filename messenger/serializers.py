from django.contrib.auth import get_user_model
from rest_framework import serializers

from messenger.models import Message, Tag

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            "id",
            "text",
            "user",
            "created_at"
        )


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            "id",
            "text_preview",
            "created_at",
            "user",
        )


class MessageDetailSerializer(MessageSerializer):
    user = UserSerializer(many=False)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")
