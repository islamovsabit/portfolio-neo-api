from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view


class ContactList(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


@api_view(['GET'])
def contact_filter_by_id(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        raise Http404
    serializer = ContactSerializer(contact)
    return Response(serializer.data)


class ContactFilterById(APIView):
    def get(self, request, pk):
        try:
            contact = Contact.objects.get(pk=pk)
            serializer = ContactSerializer(contact)
            return Response(serializer.data)
        except Contact.DoesNotExist:
            return Response(
                {"detail": "Contact item not found"},
                status=status.HTTP_404_NOT_FOUND
            )


@api_view(['GET'])
def contact_slug_view(request, contact_slug):
    try:
        contact = Contact.objects.get(contact_slug=contact_slug)
    except Contact.DoesNotExist:
        raise Http404

    serializer = ContactSerializer(contact)
    return Response(serializer.data)


class ContactSlugView(APIView):
    def get_object(self, contact_slug):
        try:
            return Contact.objects.get(contact_slug=contact_slug)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, contact_slug):
        contact = self.get_object(contact_slug)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)