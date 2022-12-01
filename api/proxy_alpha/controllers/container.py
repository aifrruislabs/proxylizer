import json
from datetime import date
from drf_yasg import openapi
from django.http import JsonResponse

from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

from ..serializers import ContainerSerializer

@api_view(['POST'])
def deploy_proxy_config(request):
	"""
	Deploy squid Proxy to the Container/Server/Droplet
	"""
	return JsonResponse({
		'status': True
		})

@api_view(['POST'])
def delete_container(request):
	"""
	Delete Container
	"""
	return JsonResponse({
		'status': True
		})


@api_view(['POST'])
def edit_container(request):
	"""
	Edit Container
	"""
	return JsonResponse({
		'status': True
		})


@api_view(['GET'])
def read_all_container(request):
	"""
	Read All Containers
	"""
	return JsonResponse({
		'status': True
		})


@api_view(['GET'])
def read_container(request):
	"""
	Read Single Container
	"""
	return JsonResponse({
		'status': True
		})


@api_view(['POST'])
def create_container(request):
	"""
	Create Container
	"""
	return JsonResponse({
		'status': True
		})
