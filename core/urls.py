
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('newsletters/', include('newsletters.urls', namespace='newsletters')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
]
