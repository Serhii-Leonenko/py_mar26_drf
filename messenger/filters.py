from django_filters import rest_framework as filters

from messenger.models import Message


class MessageFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Message
        fields = ["created_at", "user"]
