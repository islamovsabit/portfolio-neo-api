from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view


# biography all view
class BiographyView(ListAPIView):
    try:
        queryset = Biography.objects.all()
        serializer_class = BiographySerializer
    except Biography.DoesNotExist:
        raise Http404


# biography update id, class version
class BiographyDetailUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


# Biography detail update slug name #
class BiographyDetailUpdateSlugName(RetrieveUpdateDestroyAPIView):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer
    lookup_field = 'biography_slug'  # Set the lookup field to 'skills_slug'

    def get_object(self):
        # Use the 'skills_slug' from the URL to retrieve the object
        slug = self.kwargs.get('biography_slug')
        return Biography.objects.get(biography_slug=slug)


# biography id view, function version
@api_view(['GET'])
def biography_objects_view_id(request, pk):
    try:
        biography = Biography.objects.get(id=pk)
        serializer = BiographySerializer(biography)
        return Response(serializer.data)
    except Biography.DoesNotExist:
        return Response({'message': 'Biography not found'}, status=status.HTTP_404_NOT_FOUND)


# biography id view, class version
class BiographyIdView(ListAPIView):
    def get(self, request, pk):
        try:
            biography = Biography.objects.get(pk=pk)
            serializer = BiographySerializer(biography)
            return Response(serializer.data)
        except Biography.DoesNotExist:
            return Response(
                {"detail": "Biography item not found"},
                status=status.HTTP_404_NOT_FOUND
            )


# biography slug name view, function version
@api_view(['GET'])
def biography_view_slug_name(request, biography_slug):
    try:
        biography = Biography.objects.get(biography_slug=biography_slug)
        serializer = BiographySerializer(biography)
        return Response(serializer.data)
    except Biography.DoesNotExist:
        return Response({'message': 'Biography not found'}, status=status.HTTP_404_NOT_FOUND)


# biography slug name view, class version
class BiographySlugView(APIView):
    def get_object(self, biography_slug):
        try:
            return Biography.objects.get(biography_slug=biography_slug)
        except Biography.DoesNotExist:
            raise Http404

    def get(self, request, biography_slug):
        biography = self.get_object(biography_slug)
        serializer = BiographySerializer(biography)
        return Response(serializer.data)
