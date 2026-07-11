from django.contrib import admin
from django.urls import path, include
from blog.views import home, search
from blogs.views import blog_content
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('category/', include('blogs.urls')),
    path('<slug:slug>/', blog_content, name='blog_content'),
    path('blogs/search/', search, name='search')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)