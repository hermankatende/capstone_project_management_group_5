from django.urls import path
from . import views

urlpatterns = [
    path('', views.participant_list, name='participant_list'),
    path('add/', views.participant_create, name='participant_create'),
    path('<int:pk>/edit/', views.participant_edit, name='participant_edit'),
    path('<int:pk>/delete/', views.participant_delete, name='participant_delete'),
]
