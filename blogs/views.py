from django.shortcuts import render,redirect
from .models import BlogTable
from django.contrib import messages

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


def delete_blogs(request,pk):
    # print(pk)
    # BlogTable.objects.filter(id=pk).delete()
    BlogTable.objects.get(id=pk).delete()
    messages.success(request,'Data successfully deleted')
    return redirect('deshboard')


def update_blogs(request,pk):
    print(pk)
    if request.method == 'POST':
        subject_name = request.POST['subject']
        contents_name = request.POST['content']
        try:
            # db_data = BlogTable.objects.get(id=pk)
            # db_data.subject = subject_name
            # db_data.content = contents_name
            # db_data.save()
            
            BlogTable.objects.filter(id=pk).update(subject=subject_name,content=contents_name)
            messages.success(request,'Data Successfully Updtated')
            
        except Exception as e:
            print(str(e))
            messages.error(request,str(e))
        return redirect('deshboard')
    else:
        context = {}
        try:
            db_data = BlogTable.objects.get(id=pk)
            # [{'id':1,'dubject':'abc'} {'id':1,'dubject':'abc'}]
            print(db_data)
            context['data'] = db_data
        except Exception as e:
            messages.error(request,str(e))
        return render(request,'update_blogs.html',context)