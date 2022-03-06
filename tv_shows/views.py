from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TvShow

# Create your views here.
class TvShowListView(ListView):
    template_name = 'tvshow_list.html'
    model = TvShow

class TvShowDetailView(DetailView):
    template_name = 'tvshow_detail.html'
    model = TvShow
