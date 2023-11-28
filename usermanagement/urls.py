from django.urls import path
from .views import login_page,logout_session

urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('logout/', logout_session, name='logout_session_function')
]