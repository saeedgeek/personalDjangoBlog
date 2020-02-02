from django.shortcuts import render
from django.http import HttpResponse
from .models import blog as b
# Create your views here.
def blog(request):
    return render(request,"blog/blog.html",{"posts":b.objects.all()})

def blogDetail(request,postId):
    post=b.objects.filter(id=postId).first()

    return render(request,"blog/post.html",{"post":post})