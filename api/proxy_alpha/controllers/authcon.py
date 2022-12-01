import json
from datetime import date
from drf_yasg import openapi
from django.http import JsonResponse

from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

from ..serializers import ContainerSerializer

@api_view(['POST'])
def auth_reset_password(request):
	"""
	Authentication Reset Password
	"""
	return JsonResponse({
		'status': True
		})

@api_view(['POST'])
def auth_forgot_password(request):
	"""
	Authentication Forgot Password
	"""
	return JsonResponse({
		'status': True
		})

@api_view(['POST'])
def auth_new_account(request):
	"""
	Authentication Create New Account
	"""
	return JsonResponse({
		'status': True
		})

@api_view(['POST'])
def auth_logout(request):
	"""
	Authentication Account Logout
	"""
	return JsonResponse({
		'status': True
		})

@api_view(['POST'])
def auth_login(request):
	"""
	Authentication Account Login
	"""
	return JsonResponse({
		'status': True
		})