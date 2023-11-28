from django.contrib import admin
from .models import BlogTable

# Register your models here.
class ShowFields(admin.ModelAdmin):
    # fields = ('id', 'subject', 'content', 'created_at',)
    list_display = ('id','subject','content','created_at')
    # list_filter = ('subject',)
    search_fields = ('subject',)
    

admin.site.register(BlogTable,ShowFields)