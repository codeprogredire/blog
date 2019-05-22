from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'myblog/post_list.html',{'posts':posts})

def about(request):
    return render(request,'myblog/about.html',{})


def contact(request):
    return render(request,'myblog/contact.html',{})

    