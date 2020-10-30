from django.db import models
from django.core.management.utils import get_random_secret_key

class Submission(models.Model):
    SUBMISSION_STATUS = (
        ('IN_PROGRESS', 'IN PROGRESS'),
        ('COMPLETED', 'COMPLETED'),
    )
    query = models.CharField(max_length=2000)
    status = models.CharField(max_length=60, choices=SUBMISSION_STATUS)
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=60, null=True)
    index = models.IntegerField(null=True)
    description = models.CharField(max_length=100, null=True)
    protein = models.CharField(max_length=60, null=True)