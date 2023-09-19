from django.http import HttpResponse
from django.shortcuts import render
from About_Us.models import teacher

# Create your views here.
def about_us(request):
    return render(request, 'about/about_us.html')

def teacher_info(request):
    teach = teacher.objects.all()
    return render(request, 'about/t.html', {'thr' : teach})
