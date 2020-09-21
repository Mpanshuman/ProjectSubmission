from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.registration, name = 'registration'),
    path('UserDetails', views.showDetails, name = 'Details'),
    path('option', views.option, name = 'option'),
    path('update', views.update, name = 'update'),
    path('delete', views.delete, name = 'delete'),
]
