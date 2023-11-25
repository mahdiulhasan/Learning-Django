from django.shortcuts import render,redirect
from .models import BlogTable

# Create your views here.
def save_blogs(request):
    print('blog saved')
    subject_name = request.POST['subject']
    contents_name = request.POST['content']
    try:
        BlogTable.objects.create(subject=subject_name,content=contents_name)
    except Exception as e:
        print(str(e))
    return redirect('deshboard')