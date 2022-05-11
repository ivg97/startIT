from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

from main import views

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('startIT.routers')),
    path('admin/', admin.site.urls),
    path('', views.Index.as_view(), name='index'),
    path('users/', include('users.urls')),
    path('questions/', include('questions.urls')),
    path('main/', include('main.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('workouts/', include('workouts.urls')),
    path('social/', include('social_django.urls',
                                    namespace='social')),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)