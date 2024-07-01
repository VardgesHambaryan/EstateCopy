from django.urls import path
from .views import (
    HomeListView, GalleryListView, VorakListView
)


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('works/', GalleryListView.as_view(), name='gallery'),
    path('quality/', VorakListView.as_view(), name='vorak'),
]
