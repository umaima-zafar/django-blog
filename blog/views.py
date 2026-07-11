from django.shortcuts import render
from blogs.models import Blog
from django.db.models import Q 

def home(req):
    featured_posts = Blog.objects.filter(is_featured=True).order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False, status='Published').order_by('-created_at')
    context = {
        'featured_posts' : featured_posts,
        'posts' : posts,
    }
    return render(req, 'home.html', context)

def search(req):
    keyword = req.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) |  Q(body__icontains=keyword) , status='Published')
    context = {
        'blogs' : blogs,
        'keyword' : keyword
    }
    return render(req, 'search.html', context)