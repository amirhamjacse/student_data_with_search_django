from django.shortcuts import render
from .models import Students_Info
from django.db.models import Q
# Create your views here.
def home(request):
    searchinfo = None
    if request.method == 'GET':
        st = request.GET.get('search1')
        if st!= None:
            searchinfo = Students_Info.objects.filter(Q(class_name__icontains=st) | Q(result__icontains=st) | Q(name__icontains=st) | Q(roll__icontains=st))

    return render(request, 'studentinfo/index.html', {'search': searchinfo})
        