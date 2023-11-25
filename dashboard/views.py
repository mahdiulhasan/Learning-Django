from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.models import BlogTable


# Create your views here.
@login_required(login_url='/')
def dashboard(request):
    querydata = BlogTable.objects.all()
    # print(querydata)
    # for row in querydata:
        # print(row.subject)
    context = {
        'table_data' : querydata
    }
    return render(request, 'dashboard.html',context)