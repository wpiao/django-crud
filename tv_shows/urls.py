from django.urls import path
from .views import TvShowListView, TvShowDetailView, TvShowCreateView, TvShowUpdateView, TvShowDeleteView

urlpatterns = [
    path('', TvShowListView.as_view(), name='tvshow_list'),
    path('<int:pk>', TvShowDetailView.as_view(), name='tvshow_detail'),
    path('new/', TvShowCreateView.as_view(), name='tvshow_create'),
    path('<int:pk>/edit', TvShowUpdateView.as_view(), name='tvshow_update'),
    path('<int:pk>/delete', TvShowDeleteView.as_view(), name='tvshow_delete'),
]
