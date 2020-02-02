from django.shortcuts import render
from .models import job
# Create your views here.
def home(request):
    return render(request,'job/home.html',{"jobs":job.objects.all()} )