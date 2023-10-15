from django import forms
from .models import Email
from rest_framework.serializers import *


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'
