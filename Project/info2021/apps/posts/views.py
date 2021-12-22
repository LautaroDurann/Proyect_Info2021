from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Comentario
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ListarPosts(LoginRequiredMixin, ListView):
	model = Post
	template_name = "postList.html"
	context_object_name = "posts"

class DetallePost(LoginRequiredMixin, DetailView):
	model=Post
	template_name="post_detail.html"
	def get_context_data(self, **kwargs):
		data = super().get_context_data(**kwargs)
		data['comentarios'] = Comentario.objects.all()
		return data
class CrearPost(CreateView):
	model=Post
	success_url='/lista'
	template_name = 'post_update_form.html'
	form_class = PostForm

class UpdatePost(UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'post_update_form.html'
	success_url='/posts'

