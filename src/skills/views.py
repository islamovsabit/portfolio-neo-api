from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
# from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# skill detail view all #
class SkillsListCreateView(ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


# skill detail view id #
class SkillsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


# skill detail update slug name #
class SkillsDetailUpdateSlugName(RetrieveUpdateDestroyAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    lookup_field = 'skills_slug'  # Set the lookup field to 'skills_slug'

    def get_object(self):
        # Use the 'skills_slug' from the URL to retrieve the object
        slug = self.kwargs.get('skills_slug')
        return Skills.objects.get(skills_slug=slug)


# skills detail view id, function version #
@api_view(['GET'])
def skills_detail_view(request, pk):
    try:
        skill = Skills.objects.get(pk=pk)
    except Skills.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SkillsSerializer(skill)
    return Response(serializer.data)


# skills detail view id, class version #
class SkillsDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            skill = Skills.objects.get(pk=pk)
        except Skills.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SkillsSerializer(skill)
        return Response(serializer.data)


# get object slug name, function version #
@api_view(['GET'])
def skills_detail_view_slug(request, skills_slug):
    try:
        skill = Skills.objects.get(skills_slug=skills_slug)
        serializer = SkillsSerializer(skill)
        return Response(serializer.data)
        pass
    except Skills.DoesNotExist:
        return Response({'message': 'Skill not found'}, status=status.HTTP_404_NOT_FOUND)


# get object slug name, class version #
class SkillsDetailViewSlug(APIView):
    def get(self, request, skills_slug):
        try:
            skill = Skills.objects.get(skills_slug=skills_slug)
            serializer = SkillsSerializer(skill)
            return Response(serializer.data)
        except Skills.DoesNotExist:
            return Response({'message': 'Skill not found'}, status=status.HTTP_404_NOT_FOUND)