from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *


class BiographySerializer(ModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'

