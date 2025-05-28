from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('eve/', views.events2_view, name='eve'),
    path('Reg/', views.register, name='Reg'),
    path('viewreg/', views.view_registrations, name='viewreg'),]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




