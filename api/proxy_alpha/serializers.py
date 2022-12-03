from dataclasses import fields
from rest_framework import serializers

from proxy_alpha.models import Container

# Container Serializer
class ContainerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Container 
		fields = '__all__'