from blog.models import Post
from django.views.generic import ListView, DetailView
from . import views

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDV(DetailView):
    model = Post