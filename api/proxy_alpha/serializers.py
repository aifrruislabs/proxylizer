from dataclasses import fields
from rest_framework import serializers

from .models import Container

# Container Serializer
class ContainerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Container 
		fields = '__all__'