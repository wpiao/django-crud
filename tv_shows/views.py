from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TvShow
from django.urls import reverse_lazy


class TvShowListView(ListView):
    template_name = 'tvshow_list.html'
    model = TvShow


class TvShowDetailView(DetailView):
    template_name = 'tvshow_detail.html'
    model = TvShow


class TvShowCreateView(CreateView):
    template_name = 'tvshow_create.html'
    model = TvShow
    fields = ['name', 'description', 'rating', 'rater']
    success_url = reverse_lazy('tvshow_list')


class TvShowUpdateView(UpdateView):
    template_name = 'tvshow_update.html'
    model = TvShow
    fields = ['name', 'description', 'rating', 'rater']
    success_url = reverse_lazy('tvshow_list')


class TvShowDeleteView(DeleteView):
    template_name = 'tvshow_delete.html'
    model = TvShow
    success_url = reverse_lazy('tvshow_list')
