import os, sys, json
from time import sleep
import paramiko, subprocess
from datetime import date
from drf_yasg import openapi
from django.http import JsonResponse

from proxy_alpha import toolsa

from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

from proxy_alpha.models import Container
from proxy_alpha.serializers import ContainerSerializer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

@api_view(['POST'])
def configure_remove_proxy(request):
    containerId = request.POST.get('containerId')

    # Get Container Credentials
    containerData = Container.objects.get(id=containerId)

    ssh_ip = containerData.ssh_ip
    ssh_username = containerData.ssh_username
    ssh_password = containerData.ssh_password

    # https://www.geeksforgeeks.org/how-to-execute-shell-commands-in-a-remote-machine-using-python-paramiko/
    # Connect Through SSH to Remote Server
    ssh = paramiko.SSHClient()

    # Adding new host key to the local
    # HostKeys object(in case of missing)
    # AutoAddPolicy for missing host key to be set before connection setup.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    ssh.connect(ssh_ip, port=22, username = ssh_username, password = ssh_password, timeout=5)

    # Stop Proxy Container
    exec_ssh_cmd_recursive(ssh, "docker stop proxy_" + containerId)

    # Removing Docker Container
    exec_ssh_cmd_recursive(ssh, "docker container rm proxy_" + containerId)

    # Removing Docker
    exec_ssh_cmd_recursive(ssh, "apt-get remove docker.io -y")
    
    # Update Container Proxy isConfigured to False
    updateIsConfigured = Container.objects.get(id=containerId)
    updateIsConfigured.is_deployed = "F"
    updateIsConfigured.save()

    return JsonResponse({'status': True})

def exec_ssh_cmd_recursive(ssh, cmd):
    stdin, stdout, stderr = ssh.exec_command(cmd)

    notFinishStatus = True

    # Recursively Waiting for stdin Operation to finish
    while notFinishStatus:
        if stdout.readlines() != "":
            notFinishStatus = False
        else:
            sleep(2)

@api_view(['POST'])
def deploy_proxy_config(request):
    """
	Deploy squid Proxy to the Container/Server/Droplet
	"""
    containerId = request.POST.get('containerId')

    # Get Container Proxy Credentials
    containerData = Container.objects.get(id=containerId)

    ssh_ip = containerData.ssh_ip
    ssh_username = containerData.ssh_username
    ssh_password = containerData.ssh_password

    # https://www.geeksforgeeks.org/how-to-execute-shell-commands-in-a-remote-machine-using-python-paramiko/
    # Connect Through SSH to Remote Server
    ssh = paramiko.SSHClient()

    # Adding new host key to the local
    # HostKeys object(in case of missing)
    # AutoAddPolicy for missing host key to be set before connection setup.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    ssh.connect(ssh_ip, port=22, username = ssh_username, password = ssh_password, timeout=5)

    # apt update
    exec_ssh_cmd_recursive(ssh, "apt-get update")

    # Installing Docker
    exec_ssh_cmd_recursive(ssh, "apt-get install docker.io -y")

    # Creating Container Proxy Docker Container
    createContainerCmd = "docker run -it -d \
                            --name proxy_" + containerId + " \
                            --publish 3128:3128 \
                            --cap-add SYS_ADMIN \
                            --cap-add NET_ADMIN \
                            dordock/nazaproxy:latest"
  
    exec_ssh_cmd_recursive(ssh, createContainerCmd)

    # Start Squid Proxy Server
    exec_ssh_cmd_recursive(ssh, 'docker exec proxy_'+containerId+' bash -c "service squid start"')

    # Update Container Proxy is_deployed
    updateIsConfigured = Container.objects.get(id=containerId)
    updateIsConfigured.is_deployed = "T"
    updateIsConfigured.save()

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
    if request.method == 'POST':
        # Get Params from Headers
        user_id = request.POST.get('user_id')
        container_title = request.POST.get('container_title')
        container_info = request.POST.get('container_info')
        ssh_ip = request.POST.get('ssh_ip')
        ssh_username = request.POST.get('ssh_username')
        ssh_password = request.POST.get('ssh_password')

        # Add Container
        new_container = Container()
        new_container.id = toolsa.next_id(Container)
        new_container.creator_id = user_id
        new_container.container_title = container_title
        new_container.container_info = container_info
        new_container.ssh_ip = ssh_ip
        new_container.ssh_username = ssh_username
        new_container.ssh_password = ssh_password
        new_container.is_deployed = "F"
        new_container.save()

        # Serialize Container
        data_srz = ContainerSerializer(new_container).data

        return JsonResponse({
            'status': True,
            'data': data_srz
            })

    else:
        return JsonResponse({
            'status': True,
            'data': []
            })
