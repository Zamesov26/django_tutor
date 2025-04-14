from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('download/<str:filename>/', views.download_video, name='download_video'),
]