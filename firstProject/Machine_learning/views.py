from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def machine_learning(request):
    teacher = {'names' : ['shakil', 'mezba', 'shohan']}
    return render(request, 'machine_learning/machine_learning.html', context=teacher)

def dtree(request):
    return render(request, 'machine_learning/DT.html')

def k_nearest(request):
    return render(request, 'machine_learning/knn.html')

def random(request):
    return render(request, 'machine_learning/random_forest.html')