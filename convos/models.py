from django.db import models

# Create your models here.
class Credentials(models.Model):
    firstname = models.CharField(max_length=20, null=False, blank=False)
    lastname = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=20, null=False, blank=False)
    username = models.CharField(max_length=10, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    