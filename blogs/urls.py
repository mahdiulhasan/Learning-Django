from django.urls import path
from .views import save_blogs

urlpatterns = [
    path('save_blogs/',save_blogs,name='save_blogs')
]