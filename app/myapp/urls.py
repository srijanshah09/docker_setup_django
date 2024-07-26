from django.urls import path
from myapp import views

urlpatterns = [
    path('health-check/', views.health_check, name='health_check'),
    path('', views.UploadMediaFiles.as_view(), name='upload_media_files'),
]