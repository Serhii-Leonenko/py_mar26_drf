from urllib.request import Request

from rest_framework import status, viewsets, mixins
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView

from messenger.models import Message, Tag
from messenger.serializers import MessageSerializer, TagSerializer


# @api_view(["GET", "POST"])
# def message_view(request: Request) -> Response:
#     if request.method == "GET":
#         messages = Message.objects.all()
#         serializer = MessageSerializer(messages, many=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == "POST":
#         serializer = MessageSerializer(data=request.data)
#
#         serializer.is_valid(raise_exception=True) # 400 if invalid
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class GenericView(APIView):
#     queryset = None
#     serializer_class = None
#
#     def get_queryset(self):
#         assert self.queryset is not None, "queryset is not defined"
#
#         return self.queryset.all()
#
#     def get_serializer_class(self):
#         assert self.serializer_class is not None, "serializer_class is not defined"
#
#         return self.serializer_class
#
#
# class CreateMixin:
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer_class()(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class ListMixin:
#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer_class()(queryset, many=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class ListCreateView(ListMixin, CreateMixin, GenericView):
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class MessageView(ListCreateView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer
#
#
# class TagView(ListCreateView):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
