from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    path('users/', include('users.urls')),
    path('questions/', include('questions.urls')),
    path('main/', include('main.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('workouts/', include('workouts.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)