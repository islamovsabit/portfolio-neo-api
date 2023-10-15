from rest_framework import viewsets
from .models import Certificate
from .serializers import CertificateSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView


#################
class CertificateViewSet(ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


@api_view(['GET'])
def certificate_view_set(request):
    if request.method == 'GET':
        certificate = Certificate.objects.all()
        serializer = CertificateSerializer(certificate, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#################
class CertificateViewId(APIView):
    def get(self, request, id):
        try:
            certificate = Certificate.objects.get(id=id)
            serializer = CertificateSerializer(certificate, context={'request': request})
            return Response(serializer.data)
        except Certificate.DoesNotExist:
            return Response(status=404)


@api_view(['GET'])
def certificate_view_id(request, pk):
    try:
        certificate = Certificate.objects.get(pk=pk)
        serializer = CertificateSerializer(certificate)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Certificate.DoesNotExist:
        return Response("Certificate not found", status=status.HTTP_404_NOT_FOUND)


#################
