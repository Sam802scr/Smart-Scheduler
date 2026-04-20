from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('run/', views.run_scheduler, name='run_scheduler'),
    path('add-event/', views.add_event, name='add_event'),
    path('add-task/', views.add_task, name='add_task'),
]
