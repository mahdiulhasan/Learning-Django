from django.contrib import admin
from .models import BlogTable

# Register your models here.
class ShowFields(admin.ModelAdmin):
    list_display = ('id','subject','content')
    # list_filter = ('subject',)
    search_fields = ('subject',)
    

admin.site.register(BlogTable,ShowFields)