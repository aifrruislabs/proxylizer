import json
from proxy_alpha import toolsa
from datetime import date
from drf_yasg import openapi
from django.http import JsonResponse

from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from proxy_alpha.models import Container
from proxy_alpha.serializers import ContainerSerializer

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
	if request.method == 'POST':
		# Get Params from Headers
		auth_user = request.POST.get('username')
		auth_token = request.POST.get('token')
        
        # Check if Token is Right
		userCheck = User.objects.filter(username=auth_user)

		if len(userCheck) == 1:
			# Validate Token
			token_data = Token.objects.filter(user_id=userCheck[0].id)

			if len(token_data) >= 1:

				if str(token_data[0].key) == auth_token:    
					token_data[0].delete()

					return JsonResponse({
                        'status': True,
                        'message': 'Logged Out Successfully'
                        })    
				else:
					return JsonResponse({
                        'status': True,
                        'message': 'Forged Token Error'
                        })    
			else:
				return JsonResponse({
                    'status': True,
                    'message': 'Token does not Exist'
                    })    
            
		else:
			return JsonResponse({
                'status': True,
                'message': 'Wrong Username / Auth Token'
                })    

@api_view(['POST'])
def auth_login(request):
	"""
	Authentication Account Login
	"""
	if request.method == 'POST':
		# Get Params | Form Data
		username = request.POST.get('username')
		password = request.POST.get('password')
	
		# Handling Json Data
		if username == None:
			body_data = toolsa.parse_data(request)

			username = body_data['username']
			password = body_data['password']

		if username != "" and username != None and password != "" and password != None:
			# Authenticate Credentials
			user = authenticate(username=username, password=password)

	        # When Auth Pass
			if user is not None:
				token = ""

	            # Set Auth Token for User
				try:
					token = Token.objects.create(user=user)
				except Exception:
					# Find Existing Token Data
					exist_token = Token.objects.filter(user_id=user.id)

					# Get Current Token
					token = exist_token[0]

				# Validate Password
				return JsonResponse({
	                'auth_token' : token.key,
	                'status': True
	            })
			else:
				return JsonResponse({
	                'message': 'Invalid Username & Password Combination',
	                'status': False
	            })
		else:
			return JsonResponse({
	                'message': post_endpoint_message,
	                'status': False
	            })
	