from rest_framework.serializers import *
from .models import Certificate


# class CertificateSerializer(ModelSerializer):
#     class Meta:
#         model = Certificate
#         fields = '__all__'


class CertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = (
                  'id',
                  'certificate_name',
                  'certificate_created',
                  'certificate_img',
                  )
    certificate_img = SerializerMethodField()

    def get_certificate_img(self, obj):
        return f"http://127.0.0.1:8000{obj.certificate_image.url}"