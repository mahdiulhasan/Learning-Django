from django.db import models

# Create your models here.
class BlogTable(models.Model):
    subject = models.CharField(max_length=255,null=False,blank=False)
    content = models.TextField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # imageField = models.ImageField(upload_to='/image',null=True,blank=True)
    
    def __str__(self):
        return self.subject