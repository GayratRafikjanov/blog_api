from django.shortcuts import render
from .models import Post
from django.views import generic 
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class PostListView(generic.ListView):
  model = Post
  template_name = 'post_list.html'
  context_object_name = 'posts'

class PostDetailView(generic.DetailView):
  model = Post
  template_name = 'post_detail.html'
  context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, generic.CreateView):
  model = Post
  template_name = 'post_create.html'
  fields = ['title', 'body']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

  def get_success_url(self):
    return reverse_lazy('posts:detail', kwargs={'pk': self.object.pk})


    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
  model = Post
  template_name = 'post_update.html'
  context_object_name = "post"
  fields = ['title','body']

  def test_func(self):
    post = self.get_object()
    user = self.request.user
    if user == post.author:
      return True
    else:
      return False

  def get_success_url(self):
    return reverse_lazy('posts:detail', kwargs={'pk':self.object.pk})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
  model = Post
  template_name = 'post_delete.html'
  context_object_name = 'post'
  success_url = '/'

  def test_func(self):
    post = self.get_object()
    user = self.request.user
    if user == post.author:
      return True
    else:
      return False

class PostView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
  pass

    
  
