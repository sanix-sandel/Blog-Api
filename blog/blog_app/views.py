from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BlogListView(ListView):
    model=Post
    template_name='home.html'

class BlogDetailView(DetailView):
    model=Post
    template_name='post_detail.html'

class BlogCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields=['title', 'author', 'body'] 

class BlogUpdateView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title', 'body']   

class BlogDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')  #     We use reverse_lazy as opposed to just reverse so that it won’t execute the URL
#redirect until our view has finished deleting the blog post.


# Create your views here.
