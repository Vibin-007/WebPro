from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('eve/', views.events2_view, name='eve'),
    path('Reg/', views.register, name='Reg'),
    path('viewreg/', views.view_registrations, name='viewreg'),
    path('edit-registration/<int:registration_id>/', views.edit_registration, name='edit_registration'),
    path('delete-registration/<int:registration_id>/', views.delete_registration, name='delete_registration'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




