from django.shortcuts import render
from django.http import HttpResponse
from gpblog.models import *

# Create your views here.
def home(request):
    post=Post.objects.all()
    cats =Category.objects.all()
    # print(post)
    d={'post':post ,'cats':cats}
    # return HttpResponse("hiii")
    return render(request,'home.html',d)



def post(request ,url):
    post=Post.objects.get(url=url)
    cats =Category.objects.all()
    d={'post':post ,'cats':cats}
    return render(request, 'posts.html', d)




def category(request,url):
    cats =Category.objects.all()
    cat=Category.objects.get(url=url)
    post=Post.objects.filter(cat=cat)
    d={'post':post ,'cat':cat,'cats':cats }
    return render(request,'category.html',d)


def about(request):
    cats =Category.objects.all()
    return render (request,'about.html',{'cats':cats})


def contact(request):
    cats =Category.objects.all()
    return render (request,'contact.html',{'cats':cats})