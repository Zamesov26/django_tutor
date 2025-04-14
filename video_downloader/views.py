from django.http import FileResponse, Http404
from django.shortcuts import render
import os
from django.conf import settings


def video_list(request):
    video_dir = os.path.join(settings.MEDIA_ROOT, 'videos')
    videos = []
    print(video_dir)
    if os.path.exists(video_dir):
        videos = [f for f in os.listdir(video_dir) if f.lower().endswith(('.mp4', '.avi', '.mov'))]
    
    return render(request, 'video_downloader/list.html', {'videos': videos})


def download_video(request, filename):
    video_dir = os.path.join(settings.MEDIA_ROOT, 'videos')
    file_path = os.path.join(video_dir, filename)
    
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
    
    raise Http404("Видео не найдено")
