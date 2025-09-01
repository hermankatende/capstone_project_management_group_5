from django.urls import path
from . import views

urlpatterns = [
    path('outcomes/', views.outcome_list, name='outcome_list'),
    path('outcomes/create/', views.outcome_create, name='outcome_create'),
    path('outcomes/<int:pk>/', views.outcome_detail, name='outcome_detail'),
    path('outcomes/<int:pk>/edit/', views.outcome_edit, name='outcome_edit'),
    path('outcomes/<int:pk>/delete/', views.outcome_delete, name='outcome_delete'),
]
