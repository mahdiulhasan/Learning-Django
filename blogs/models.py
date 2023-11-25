from django.db import models

# Create your models here.
class BlogTable(models.Model):
    subject = models.CharField(max_length=255,null=False,blank=False)
    content = models.TextField(null=False,blank=False)