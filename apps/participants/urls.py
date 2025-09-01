from django.urls import path
from . import views

urlpatterns = [
    path('', views.participant_list, name='participant_list'),
    path('add/', views.participant_create, name='participant_create'),
    path('<int:pk>/edit/', views.participant_edit, name='participant_edit'),
    path('<int:pk>/delete/', views.participant_delete, name='participant_delete'),

    # Project assignments
    path('assign/<int:project_id>/', views.assign_participant, name='assign_participant'),
    path('remove/<int:assignment_id>/', views.remove_assignment, name='remove_assignment'),
]
