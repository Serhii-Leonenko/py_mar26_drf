from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from base.serializers import CreatableSlugRelatedField
from messenger.models import Message, Tag

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


# --------------------------Message-----------------------
class MessageSerializer(serializers.ModelSerializer):
    tags = CreatableSlugRelatedField(
        many=True,
        slug_field="name",
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Message
        fields = (
            "id",
            "text",
            "user",
            "created_at",
            "tags",
            "image"
        )


class MessageListSerializer(serializers.ModelSerializer):
    tags = SlugRelatedField(many=True, slug_field="name", read_only=True)
    user = serializers.CharField(source="user.username")

    class Meta:
        model = Message
        fields = (
            "id",
            "text_preview",
            "created_at",
            "user",
            "tags",
        )


class MessageDetailSerializer(MessageSerializer):
    user = UserSerializer(many=False)
    tags = TagSerializer(many=True)
