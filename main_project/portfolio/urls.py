from django.urls import path
from .views import *



app_name = 'portfolio'

urlpatterns = [
    path('', main, name='main'),
    path('project-details/<int:pk>/<slug:slug>/', project_details, name='project_details'),
    path('download_cv/', download_cv, name='downloadCV'),
]