from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info_views, name='info'),
    path('hobbies/', views.hobbies_views, name = 'hobbies'),
]
    