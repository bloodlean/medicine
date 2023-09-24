from rest_framework import serializers
from app.models import Client, Blog, Sponsor

class ClientSerializer(serializers.Serializer):
    class Meta:
        model = Client
        fields = '__all__'

class BlogSerializer(serializers.Serializer):
    class Meta:
        model = Blog
        fields = '__all__'

class SponsorSerializer(serializers.Serializer):
    class Meta:
        model = Sponsor
        fields = '__all__'