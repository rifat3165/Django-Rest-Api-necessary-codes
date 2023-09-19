from django.shortcuts import render
from django.http import HttpResponse
from . forms import TeacherRegistration

# Create your views here.
def blog(request):
    return render(request, 'blogs/blog.html')

def ShowFormData(request):
    if request.method == 'POST':
        fm = TeacherRegistration(request.POST)
        if fm.is_valid():
            password = fm.cleaned_data['password']
            repassword = fm.cleaned_data['repassword'] 
            print(password)
            print(repassword)
    else:
        fm = TeacherRegistration()
        print("this is GET statement")
    return render(request, 'blogs/form.html', {'form': fm})
