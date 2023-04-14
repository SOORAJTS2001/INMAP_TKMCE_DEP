from django.db import models

# Create your models here.
from django.db import models

class ApiAccounts(models.Model):
    organization = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    api_cred = models.CharField(max_length=255, unique=True)
    api_secret = models.CharField(max_length=255, unique=True)
    expected_requests = models.PositiveIntegerField(default=0)
    last_used_time = models.DateTimeField(auto_now=True)
    total_usage = models.PositiveIntegerField(default=0)
    usage_per_day = models.PositiveIntegerField(default=0)
