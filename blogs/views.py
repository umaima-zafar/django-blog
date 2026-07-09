from django.shortcuts import render, get_object_or_404
from blogs.models import Blog, Category

def posts_by_category(req, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts' : posts,
        'category': category
    }
    return render(req, 'posts_by_category.html', context)