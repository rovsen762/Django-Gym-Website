
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator
from . models import Blog



class BlogPageView(ListView):
    model = Blog
    template_name = 'blogs.html'
    paginate_by = 3

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogpage.html'
    
    