from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Tasks(request):
    return render(request, "tasks.html")