from django.urls import path
from . import views
urlpatterns = [
    path('', views.facility_list, name='facility_list'),
    path('add/', views.facility_create, name='facility_create'),
    path('<int:pk>/edit/', views.facility_edit, name='facility_edit'),
    path('<int:pk>/delete/', views.facility_delete, name='facility_delete'),
]
