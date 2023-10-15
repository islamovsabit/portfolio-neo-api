from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from .serializers import MessageSerializer
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView


class MessageView(ListAPIView):
    queryset = Email.objects.all()
    serializer_class = MessageSerializer


class MessageViewSet(CreateAPIView):
    queryset = Email.objects.all()
    serializer_class = MessageSerializer

# class MessageView(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Email.objects.all()
#         serializer = MessageSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Email.objects.all()
#         email = get_object_or_404(queryset, pk=pk)
#         serializer = MessageSerializer(email)
#         return Response(serializer.data)


# class MessageDetailIdView(viewsets.ReadOnlyModelViewSet):
#     pass
#
#
# class MessageViewSet(viewsets.ModelViewSet):
#     queryset = Email.objects.all()
#     serializer_class = MessageSerializer
#
#     # Custom action
#     @action(detail=True, methods=['POST'])
#     def custom_action(self, request, pk=None):
#         instance = self.get_object()  # Retrieve the specific object
#         # Perform custom action logic here
#         return Response({'message': 'Custom action performed on object with id {}'.format(instance.id)})