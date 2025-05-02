from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webtechapp.urls')),
    # path('admin/', admin.site.urls),
    # path('eve/', include('eve.urls')),
]

