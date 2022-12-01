from . import views

from django.urls import path, re_path, include
from rest_framework_swagger.views import get_swagger_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .controllers import authcon
from .controllers import container

urlpatterns = [
  
  # Auth APIS

  # Login
  path('/auth/auth_login', authcon.auth_login),

  # Logout
  path('/auth/auth_logout', authcon.auth_logout),

  # Create Account
  path('/auth/auth_new_account', authcon.auth_new_account),

  # Forgot Password
  path('/auth/auth_forgot_password', authcon.auth_forgot_password),

  # Reset Password
  path('/auth/auth_reset_password', authcon.auth_reset_password),

  # AUTH APIS

  # Container APIS

  # Deploy Proxy Config
  path('/container/deploy_proxy_config', container.deploy_proxy_config),

  # Create Container 
  path('/container/create_container', container.create_container),

  # Read Container 
  path('/container/read_container', container.read_container),

  # Read All Containers
  path('/container/read_all_container', container.read_all_container),

  # Edit Container
  path('/container/edit_container', container.edit_container),

  # Delete Container
  path('/container/delete_container', container.delete_container),

]