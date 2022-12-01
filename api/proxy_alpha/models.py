from django.db import models

# Container Table
class Container(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    creator_id = models.IntegerField(blank=True)
    container_title = models.CharField(max_length=200, blank=True)
    container_info = models.CharField(max_length=200, blank=True)
    ssh_ip = models.CharField(max_length=200, blank=True)
    ssh_username = models.CharField(max_length=200, blank=True)
    ssh_password = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'containers'