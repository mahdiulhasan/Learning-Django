from django.urls import path
from .views import dashboard

urlpatterns = [
    path('home/', dashboard,name='deshboard')
]